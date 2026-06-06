# escreva um programa que leia um valor em m(metros) , converta o mesmo em centímetros e milímetros


def calcularEmCm(value: float):
    return value * 100

def calcularEmmm(value: float):
    return value * 1000


if __name__ == "__main__":

    n1 = int(input("digite o valor em m: "))

    print("o valor em metros é {} \n o valor em cm é: {} \n o valor em mm é : {}".format(n1,calcularEmCm(n1),calcularEmmm(n1)))




