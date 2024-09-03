from pymongo import MongoClient

from simpleCLI import SimpleCLI


class LivrosCLI(SimpleCLI):
    def __init__(self):
        super().__init__()
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["Biblioteca"]
        self.collection = self.db["Livros"]
        self.add_command("criar", self.criar_livro)
        self.add_command("ler", self.ler_livro)
        self.add_command("atualizar", self.atualizar_livro)
        self.add_command("deletar", self.deletar_livro)

    def criar_livro(self):
        _id = input("Digite o ID: ")
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        ano = int(input("Digite o ano: "))
        preco = float(input("Digite o preço: "))
        livro = {
            "_id": _id,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "preco": preco
        }
        self.collection.insert_one(livro)
        print("Livro criado com sucesso!")

    def ler_livro(self):
        _id = input("Digite o ID: ")
        livro = self.collection.find_one({"_id": _id})
        if livro:
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preço: {livro['preco']}")
        else:
            print("Livro não encontrado.")

    def atualizar_livro(self):
        _id = input("Digite o ID: ")
        titulo = input("Digite o novo título: ")
        autor = input("Digite o novo autor: ")
        ano = int(input("Digite o novo ano: "))
        preco = float(input("Digite o novo preço: "))
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "preco": preco
        }
        self.collection.update_one({"_id": _id}, {"$set": livro})
        print("Livro atualizado com sucesso!")

    def deletar_livro(self):
        _id = input("Digite o ID: ")
        self.collection.delete_one({"_id": _id})
        print("Livro deletado com sucesso!")