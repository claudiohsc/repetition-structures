n = int(input())
k = 0
i = 0
while i < n:
	s = input()
	if s[1] == '+':
		k += 1
	else:
		k -= 1
	i += 1

print(k)
