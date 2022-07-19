n = int(input())

volta = [int(x) for x in input().split()]

maior = -1

for i in range(0,n):
  maior = max(maior,volta[i])

res = str(maior-volta[0])

for i in range(1,n):
  res = res + " " + str(maior-volta[i])

print(res)