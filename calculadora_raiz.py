import math  # Se importo libreria math para que se pueda hacer uso de la función sqrt para las raices 

def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles: +, -, *, /, raiz")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        operador = input("Ingrese la operación (+, -, *, /, raiz): ")
        
        if operador == 'raiz':
            if num1 < 0:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")  # Se agrego primera opción de que no pueda realizar raices negativas.
                return
            resultado = math.sqrt(num1)
        else:
            num2 = float(input("Ingrese el segundo número: "))
            
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
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
