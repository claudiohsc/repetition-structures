n = int(input())

for i in range(n):
    s = input()
    
    g = 0
    cont = 0
    ativo = False
    
    for i in s:
        if i == '1':
            g += cont
            cont = 0
            ativo = True
        elif ativo:
            cont += 1
    print(g)