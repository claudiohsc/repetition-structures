pa, pb, ta, tb = input().split()

pa, pb = int(pa), int(pb)
ta, tb = float(ta) /  100, float(tb) / 100

if (ta < tb):
    print('A nunca alcancara B.')
elif (int(pa * ta) == 0):
    print('A nunca alcancara B.')
else:
    anos = 0
    comp = False
    while pa < pb:
        pa += int(pa * ta)
        pb += int(pb * tb)
        anos += 1
        if anos == 1000:
            comp = True
            break
    if comp:
        print('Mais de um milenio.')
    else:
        print(f'Vai alcancar em {anos} ano(s).')