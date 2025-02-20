def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles: +, -, *, /")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        operador = input("Ingrese la operación (+, -, *, /, %): ")
        num2 = float(input("Ingrese el segundo número: "))
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '%':
            resultado = num1 % num2
        elif operador == '/':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
                return
            resultado = num1 / num2
        else:
            print("Operador no válido.")
            return
        
        print(f"El resultado es: {resultado}")
    except ValueError:
        print("Error: Ingrese un número válido.")

calculadora()
