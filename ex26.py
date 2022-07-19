a = 0
b = 0
c = 0

n = int(input())

for i in range(n):
    x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    a += x
    b += y
    c += z

if a or b or c:
    print('NO')
else:
    print('YES')    
