def contrario(l):
    l.pop()
    lista = l[::-1]
    print(*lista, sep=" ")

l = [int(i) for i in input().split()]
contrario(l)