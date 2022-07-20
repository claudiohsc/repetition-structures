n = int(input())
s = input()

res = n -1
for i in range(1, n):
    if s[i] < s[i-1]:
        res = i - 1
        break

print(s[:res] + s[res+1:])