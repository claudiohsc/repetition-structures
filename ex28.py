def maior_menor(l):
    pt_menor, pt_maior = 0, 0
    for i in range(len(l)):
        if(l[i] < l[pt_menor]):
            pt_menor = i
        if(l[i] > l[pt_maior]):
            pt_maior = i
    print(l[pt_menor], pt_menor)
    print(l[pt_maior], pt_maior)
    print(*l, sep = " ") 

l = [int(i) for i in input().split()]
maior_menor(l)