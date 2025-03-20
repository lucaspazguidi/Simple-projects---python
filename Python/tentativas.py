import random

Numero = random.randint(1,100)

tentativas = 0 

while True:
    Quest = int(input("Digite o numero que acha que foi escolhido: "))
    tentativas +=1
    if Quest == Numero:
        print(f"Parabens! Voce acertou o numero {Numero} em {tentativas} tentativas")
        break
    else:
        if Quest < Numero:
            print("O numero escolhido esta abaixo, tente novamente")
        if Quest > Numero:
            print("O numero escolhido esta acima, tente novamente")