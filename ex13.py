soma = 0
cont = 0
while True:
    x = int(input())
    if x == -1:
        break
    soma += x
    cont += 1
print(soma // cont)