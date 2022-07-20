def chinelo(pe_bill, l):
    l.sort()
    i = 0
    while ((i < len(l)) and (l[i] < pe_bill)):
        i+= 1
    if (i == len(l)):
        return - 1
    else:
        return i


pe = int(input())
lista = [int(i) for i in input().split()]
print(chinelo(pe, lista))