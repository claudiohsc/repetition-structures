import math

x = int(input())

if x < 0:
    sinal = True
    x = x * -1
else:
    sinal = False

dim = 10 ** int(math.log(x, 10))

res = 0
while x > 0:
    res += (x%10) * dim
    dim //= 10
    x //= 10
    
if sinal:
    print(-1 * res)
else:
    print(res)