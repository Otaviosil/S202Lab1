from passageiro import Passageiro


class Corrida:
    def __init__(self, nota_corrida, distancia, valor, passageiro):
        self.nota_corrida = nota_corrida
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def to_dict(self):
        return {
            "nota_corrida": self.nota_corrida,
            "distancia": self.distancia,
            "valor": self.valor,
            "passageiro": self.passageiro.to_dict()
        }
