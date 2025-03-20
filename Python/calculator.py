num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor:  "))
operador = input("Digite qual a operacao que gostaria de realizar:  + ,- ,x ,/. ").strip()

def calculadora():
        if operador == "+":
            resultado =  num1 + num2
            print(f"o resultado é {resultado}") 
        elif operador == "-":
            resultado = num1 - num2
            print(f"o resultado é {resultado}")    
        elif operador == "x":
            resultado = num1 * num2
            print(f"o resultado é {resultado}")    
        elif operador == "/":
            resultado = num1 / num2
            print(f"o resultado é {resultado:.1f}")
        else:
             print("Operador invalido!")
calculadora()