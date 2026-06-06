## crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
## com 15% de aumento



def calcularAumento(valor:float,aum):
    return valor*(aum/100)

if __name__ == "__main__":
    salario = float(input("digite o valor de salário: "))

    print("o valor do salário antigo é: {} \n com aumento de 15% é:  {} ".format(salario,salario + calcularAumento(salario,15)))