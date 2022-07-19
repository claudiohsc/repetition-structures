n = int(input())

din = 0
for i in range(n):
        x = int(input())
        din += max(0, 1000-x)

print(din)
