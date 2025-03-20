class Imc:
    def __init__(self,peso,altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    def mostrar_imc(self):
        imc = self.calcular_imc()
        print(f"Seu imc é {imc:.2f}")

Quest = float(input("Digite seu peso: "))
Quest2 = float(input("Digite sua altura: "))

pessoa = Imc(Quest,Quest2)
pessoa.mostrar_imc()