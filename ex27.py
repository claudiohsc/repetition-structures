def ehPrimo(x):

    for i in range(2, x):
        if x % i == 0:
            return 0

    return 1

def divisoresPrimos(x):

    qtd = 0

    for i in range(2, x):
        if x % i == 0 and ehPrimo(i):
            qtd += 1

    return qtd
