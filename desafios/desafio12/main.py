# crie um algoritmo que leia o preço de um produto
## e mostre seu novo preço, com 5% de desconto

def calcularDesconto(value:float, desc):
    return value*(desc/100)

if __name__ == "__main__":

    preco = float(input("dgite o valor do produto: "))

    print("o valor do produto é: {} \n com 5% de desconto é: {}".format(preco,preco - calcularDesconto(preco,5)))

