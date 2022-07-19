n1, n2 = [int(x) for x in input().split()]

if n1 > n2:
    n1,n2 = n2,n1

while n1 > 0:
    resto = n2 % n1
    n1,n2 = resto,n1

mdc = n2
if n2 == 1:
    print('Sao co-primos.')
else:
    print('Nao sao co-primos!')