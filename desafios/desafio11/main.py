

## faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantiade de tinta necesária
## para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².


def calcularArea(largura:float, altura:float):
    return largura*altura;

if __name__ == "__main__":
    largura = float(input("digite a largura: "))
    altura = float(input("digite a altura: "))

    area = calcularArea(largura,altura)
    print("o valor da área é: {}".format(area))

    print("você precisará de {} baldes de tinta para pintar".format(int(area/2)))

