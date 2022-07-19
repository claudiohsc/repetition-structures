a = int(input())
menor = 100000
maior = -100000
i = 0
while i < a:
    n = int(input())
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    i += 1
print('Menor: ' + str(menor))
print('Maior: ' + str(maior))