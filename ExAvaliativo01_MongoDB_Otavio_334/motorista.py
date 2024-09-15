from corrida import Corrida


class Motorista:
    def __init__(self, nota_motorista, corridas=None):
        self.nota_motorista = nota_motorista
        self.corridas = corridas if corridas is not None else []

    def to_dict(self):
        return {
            "nota_motorista": self.nota_motorista,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }