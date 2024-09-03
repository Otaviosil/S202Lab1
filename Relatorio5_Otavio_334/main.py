from livrosCLI import LivrosCLI


if __name__ == "__main__":
    livros_cli = LivrosCLI()
    print("Bem-vindo ao CLI de Livros!")
    print("Comandos disponíveis: criar, ler, atualizar, deletar, sair")
    livros_cli.run()