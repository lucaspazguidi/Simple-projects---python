import re 


def verificar_senha(senha):
    força = 0
    
    if len(senha) >= 8:
        força +=1
    if re.search(r"[A-Z]", senha):
        força += 1
    if re.search(r"[a-z]", senha):
        força +=1
    if re.search(r"[!@#$%&*]" , senha):
        força +=1
    if força < 3:
        print("Senha Fraca")
    if força == 3:
        print("Senha média")
    if força > 3:
        print("Senha forte")

Quest = input("Digite a sua senha: ")
resultado = verificar_senha(Quest)
