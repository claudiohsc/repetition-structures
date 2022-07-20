n = int(input())

res = 0
for i in range(n):
	a, b, c = [int(x) for x in input().split()]
	s = a + b + c
	if s >= 2:
	    res += 1

print(res)

