

def maiorDeIdade(value:int):
    return value>=18

def main():
    print("este é meu primeiro programa em Python...")

    name = input("digite seu nome: \n")
    
    idade = int(input("digite sua idade: \n"))

    print("você é maior de idade? ", maiorDeIdade(idade))


if __name__ == "__main__":
    main()



