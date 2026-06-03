## PARAM hello user
from os import name

## TODO: mensagem de saída para o usuário
def messageOut(name):
    return "é um prazer lhe conhecer {}".format(name)

def main():
    name:str = input("digite seu nome: ")
    print(messageOut(name))


if __name__ == "__main__":
    main()

