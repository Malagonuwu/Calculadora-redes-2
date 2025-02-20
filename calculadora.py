def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles: +, -, *, /")
    
    continuar = True
    decision = 'limpiar'
    while(continuar):
        try:
            if decision == 'limpiar':
                num1 = float(input("Ingrese el primer número: "))
            else: 
                num1 = resultado
                print(f"Primer número: {num1}")
                decision = 0
                
            operador = input("Ingrese la operación (+, -, *, /): ")
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
                print("Operador no válido. Vuelva a intentarlo. ")
                continue

            print(f" {num1} {operador} {num2} = {resultado}")
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

        
        decision = input("Si desea continuar, ingrese 'si': ")

        if(decision.lower() == 'si'):
            decision = input(f"Si desea operar sobre su anterior resultado ({resultado}), ingrese 'si': ")
            if (decision.lower() != 'si'): decision = 'limpiar'; 
        else: continuar = False
    
    print("Apagando calculadora...")



calculadora()
