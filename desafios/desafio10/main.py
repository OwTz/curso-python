
# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar


def converterEmDolar(valorReais:float):
    return (valorReais)/3.27

if __name__ == "__main__":
    n1 = float(input("digite o valor em R$ (reais) : "))
    print("você consegue comprar: {} $$ dólares \n contendo o valor de {} R$ reais".format(converterEmDolar(n1),n1))


