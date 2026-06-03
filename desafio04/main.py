



if __name__ == '__main__':
    n = input("digite um valor: ")

    print("\n o seu tipe primitivo é {}".format(type(n)))
    print("\n é um número ? {}".format(n.isalnum()))
    print("\n pode ser printado ? {}".format(n.isprintable()))
    print("\n é um alfabético ? {}".format(n.isalpha()))
    print("\n é um alfa numérico ? {}".format(n.isalnum()))
    print("\n é um title ? {}".format(n.istitle()))
    print("\n está em minusculo ? {}".format(n.islower()))
    print("\n está em  maisuculo ? {}".format(n.isupper()))
    print("\n é um espaço ? {}".format(n.isspace()))
