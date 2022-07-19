def ortogonais(v1, v2):
    x = 0
    for i in range(len(v1)):
        x += v1[i] * v2[i]
    if x != 0:
        print(x)
    else:
        print('ortogonais')

n = int(input())
  
v1 = list(map(int,input().split()))[:n]
v2 = list(map(int,input().split()))[:n]

ortogonais(v1, v2)