sum = 0
cont = 0
while True:
    x = int(input())
    if x == -1:
        break
    sum += 1 / x
    cont += 1
print(int(cont/sum))