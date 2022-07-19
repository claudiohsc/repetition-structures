lista = list(map(int, input().split()))

n = len(lista)
t = 0

for i in range(n - 1):
    for j in range(n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            t += 1

print(t)