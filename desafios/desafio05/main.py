# faça um programa que leia um número inteiro e mostre na tela o seu sucesso e seu antecessor


if __name__ == "__main__":
    n1 = int(input("digite um valor: "))
    print("o seu sucessor é: {} \n o seu antecessor é: {}".format(n1+1,n1-1))