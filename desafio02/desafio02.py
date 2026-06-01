

def main():
    dia = input("digite o dia : \n")
    mes = input("digite o mês de nascimento: \n")
    ano = input("digite o ano: \n")

    dataformat=data(dia,mes,ano)
    print("o usuário nasceu em: ", dataformat)

def data(dia,mes,ano):
    return f'{dia} / {mes} / {ano}'

if __name__ == "__main__":
    main()
