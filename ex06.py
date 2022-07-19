c = input()
n = list(map(int, input().split()))
m = min(n)
for i in n:
    print(i - m, end=" ")
