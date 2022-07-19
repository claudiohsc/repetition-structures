def ppa(a, b):
    if a == 3 and b == 3:
        return 'Aniquilacao mutua'
    elif a == 2 and b == 2:
        return 'Ambos venceram'
    elif a == 1 and b == 1:
        return 'Sem ganhador'
    elif a == 3 or (a == 1 and b == 2):
        return 'Jogador 1 venceu'
    else:
        return 'Jogador 2 venceu'