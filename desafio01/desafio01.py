

def main():
    print("Inicializando programa... \n")

    name = input("digite seu nome: \n")
    print(message(name))

def message(userName):
    return f'Olá usuário {userName}, que bom em te conhecer!'


# TODO inicializando o SCRIPT
if __name__ == "__main__":
    main()