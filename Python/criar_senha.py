import random


letras = "abcdefghijklmnopqsrtuvwxyz"
numeros = "0123456789"
especiais = "! @ # $ % & * "
letras_lista = letras.split()
numeros_lista = numeros.split()
especiais_lista = especiais.split()
def criar_senha():
    l1 = []
    
    for i in range(5):
        e = random.choice(letras)
        l1.append(e)
        s = random.choice(numeros)
        l1.append(s)
    for i in range(2):
        t = random.choice(especiais_lista)
        l1.append(t)

    random.shuffle(l1)
    l2 = ''.join(l1)
    return l2
Quest = input("Voce quer criar uma senha? S/N  ").strip().upper()
if Quest == "S" :
    print(criar_senha())
else:
    print("Programa encerrado.")
    