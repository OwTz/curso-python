

n = input("\n digite o valor:")


if __name__ == '__main__':
    print("\n o valor é  {}".format(n))
    print("\n seu tipe é {}".format(type(n)))
    print("\n tem valor ? {}".format(bool(n)))
    valor = n.isalnum()
    print("\n é um valor numerico? {}".format(valor))