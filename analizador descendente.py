def process_sentence(sentence):
    keywords = ["+", "-", "*", "/", "(", ")", "num", "\0"]
    original_stack = ["\0"]
    words = sentence.split()

    for word in reversed(words):
        if word in keywords:
            original_stack.append(word)
        else:
            original_stack.append("id")
    return original_stack

def process_q(original_stack):
    print("Contenido de la pila original en process_q:", original_stack)
    new_stack = ["\0", "E"]

    transition_table = {
        "E": { "(": ["T", "E'"], "num": ["T", "E'"], "id": ["T", "E'"] },
        "E'": { "+": ["+", "T", "E'"], "-": ["-", "T", "E'"], ")": [], "\0": [] },
        "T": { "(": ["F", "T'"], "num": ["F", "T'"], "id": ["F", "T'"] },
        "T'": { "+": [], "-": [], ")": [], "\0": [], "*": ["*", "F", "T'"], "/": ["/", "F", "T"] },
        "F": { "(": ["(", "E", ")"], "num": ["num"], "id": ["id"] }
    }

    while original_stack and new_stack:
        top_new = new_stack[-1]
        top_original = original_stack[-1]

        if top_new == "\0" and top_original == "\0":
            print("Sin errores sintácticos")
            break

        if top_new == top_original:
            new_stack.pop()
            original_stack.pop()
        elif top_new in transition_table and top_original in transition_table[top_new]:
            new_stack.pop()
            for symbol in reversed(transition_table[top_new][top_original]):
                new_stack.append(symbol)
        else:
            print("Error sintáctico")
            break

        print("Contenido de la nueva pila", new_stack)
        print("Contenido de la pila original", original_stack)
        print("-----------------------\n")

user_input = input("Entrada: ")
processed_stack = process_sentence(user_input)
print("\nContenido de la pila original:")
print(processed_stack)
print("\n")
process_q(processed_stack.copy())
