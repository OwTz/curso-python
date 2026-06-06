
# faça um programa que leia um número inteiro qualquer e mostre sua tabuada na tela.



def showTabuada(value:int):
   i = 0
   while(i <= 10):
       print("{}  x {} = {}".format(value,i,value*int(i)))
       i += 1


if __name__ == "__main__":
    n1 = int(input("digite um valor: "))
    showTabuada(n1)

