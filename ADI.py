def process_sentence(sentence):
    # Palabras clave y operadores
    keywords = ["+", "-", "*", "/", "(", ")", "num", "\0"]

    # Inicializar la pila original
    original_stack = ["\0"]

    # Dividir la oración en palabras
    words = sentence.split()

    for word in reversed(words):
        if word in keywords:
            # Si la palabra es una palabra clave u operador, la agregamos a la pila original
            original_stack.append(word)
        else:
            # Si no, consideramos la palabra como un id y la agregamos a la pila original
            original_stack.append("id")
    return original_stack
 
def process_q(original_stack):
    # Mostrar el contenido de la pila original (depuración)
    print("Contenido de la pila original en process_q:", original_stack)
    new_stack=["\0"]
    new_stack.append("E")
    
    print("Contenido de la pila nueva", new_stack)
    while original_stack or new_stack:
        #print("valores a comparar nueva pila: "+new_stack[-1]+" pila original: "+original_stack[-1])
        if new_stack and original_stack:
            if new_stack[-1] == "\0" and original_stack[-1] == "\0":
                print("Sin errores sintacticos")
            if new_stack[-1] == original_stack[-1]:
                original_stack.pop()
                new_stack.pop() 
            elif new_stack[-1]=="E" and (original_stack[-1] == "(" or original_stack[-1] == "num" or original_stack[-1] == "id"):
                new_stack.pop()  
                new_stack.append("E'")
                new_stack.append("T")  
            elif new_stack[-1]=="E'" and original_stack[-1] == "+":
                new_stack.pop() 
                new_stack.append("E'")
                new_stack.append("T") 
                new_stack.append("+") 
            elif new_stack[-1]=="E'" and original_stack[-1] == "-":
                new_stack.pop() 
                new_stack.append("E")
                new_stack.append("T") 
                new_stack.append("-")
            elif new_stack[-1]=="E'" and (original_stack[-1] == ")" or original_stack[-1] == "\0"):
                new_stack.pop()
            elif new_stack[-1]=="T" and (original_stack[-1] == "(" or original_stack[-1] == "num" or original_stack[-1] == "id"):
                new_stack.pop()
                new_stack.append("T'")
                new_stack.append("F")
            elif new_stack[-1]=="T'" and (original_stack[-1] == "+" or original_stack[-1] == "-" or original_stack[-1] == ")" or original_stack[-1] == "\0"):
                new_stack.pop()
            elif new_stack[-1]=="T'" and original_stack[-1] == "*":
                new_stack.pop()
                new_stack.append("T'") 
                new_stack.append("F")   
                new_stack.append("*") 
            elif new_stack[-1]=="T'" and original_stack[-1] == "/":
                new_stack.pop()
                new_stack.append("T") 
                new_stack.append("F")   
                new_stack.append("/")
            elif new_stack[-1]=="F" and original_stack[-1] == "(":
                new_stack.pop()
                new_stack.append(")")
                new_stack.append("E") 
                new_stack.append("(")   
            elif new_stack[-1]=="F" and original_stack[-1] == "num":
                new_stack.pop()
                new_stack.append("num") 
            elif new_stack[-1]=="F" and original_stack[-1] == "id":
                new_stack.pop()
                new_stack.append("id") 
            else:
                print("error sintactico")
                break

            print("Contenido de la nueva pila", new_stack)
            print("Contenido de la original pila", original_stack)   
            print("-----------------------\n")     



user_input = input("Entrada: ")

processed_stack = process_sentence(user_input)
print("\nContenido de la pila original:")

print("\n")
process_q(processed_stack.copy())
