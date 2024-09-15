from motoristaDAO import MotoristaDAO
from corrida import Corrida
from motorista import Motorista
from passageiro import Passageiro


class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.create_motorista()
            elif choice == "2":
                self.read_motorista()
            elif choice == "3":
                self.update_motorista()
            elif choice == "4":
                self.delete_motorista()
            elif choice == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def create_motorista(self):
        nota_motorista = int(input("Nota do Motorista (int): "))
        corridas = []
        while True:
            nome_passageiro = input("Nome do Passageiro (string): ")
            documento_passageiro = input("Documento do Passageiro (string): ")
            nota_corrida = int(input("Nota da Corrida (int): "))
            distancia = float(input("Distância da Corrida (double): "))
            valor = float(input("Valor da Corrida (double): "))
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)
            add_more = input("Adicionar mais corridas? (s/n): ")
            if add_more.lower() != 's':
                break
        motorista = Motorista(nota_motorista, corridas)
        self.motorista_dao.create_motorista(motorista.to_dict())
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        query = {"nota_motorista": int(input("Nota do Motorista (int): "))}
        motorista = self.motorista_dao.read_motorista(query)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        query = {"nota_motorista": int(input("Nota do Motorista a ser atualizado (int): "))}
        new_nota_motorista = int(input("Nova Nota do Motorista (int): "))
        self.motorista_dao.update_motorista(query, {"nota_motorista": new_nota_motorista})
        print("Motorista atualizado com sucesso!")

    def delete_motorista(self):
        query = {"nota_motorista": int(input("Nota do Motorista a ser deletado (int): "))}
        self.motorista_dao.delete_motorista(query)
        print("Motorista deletado com sucesso!")