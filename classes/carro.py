class Carro:
    def __init__(self, velocidade_inicial):
        self.velocidade = velocidade_inicial

    def acelera(self):
        self.velocidade += 1

    def freio(self):
        self.velocidade -= 1

    def exibir_velocidade(self):
        print(f"velocidade atual: {self.velocidade} km/h")
