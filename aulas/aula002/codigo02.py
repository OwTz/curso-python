<<<<<<< HEAD

# CALCULADORA DE IMC

def main():
    print("iniciando a calculadora de IMC... \n")
    
    name = input("digite seu nome: \n")

    idade = input("digite sua idade: \n")

    peso = input("digite seu peso: \n")

    altura = input("digite sua altura: \n")

    imc = calcularIMC(peso,altura)

    print(f'Olá {name}, sua idade é {idade}, e seu IMC é {imc} \n')

# TODO calcular o IMC do usuário
def calcularIMC(peso, altura):
    # TODO convertendo para float
    peso = float(peso)
    altura = float(altura)
    # IMPORTANT: formula Imc = peso / (altura * altura) 
    return peso / pow(altura,2) 

# TODO inicializando o SCRIPT
if __name__ == "__main__":
=======

# CALCULADORA DE IMC

def main():
    print("iniciando a calculadora de IMC... \n")
    
    name = input("digite seu nome: \n")

    idade = input("digite sua idade: \n")

    peso = input("digite seu peso: \n")

    altura = input("digite sua altura: \n")

    imc = calcularIMC(peso,altura)

    print(f'Olá {name}, sua idade é {idade}, e seu IMC é {imc} \n')

# TODO calcular o IMC do usuário
def calcularIMC(peso, altura):
    # TODO convertendo para float
    peso = float(peso)
    altura = float(altura)
    # IMPORTANT: formula Imc = peso / (altura * altura) 
    return peso / pow(altura,2) 

# TODO inicializando o SCRIPT
if __name__ == "__main__":
>>>>>>> c0b6397c5cab73ab1e6b6687d3ff72d8c8fda0aa
    main()