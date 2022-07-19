n, preco = input().split()
sum = 0
for i in range(int(n)):
    x = int(input())
    sum += x

print(f'media: {int(sum/int(n))}')
print('o rock reinara mais uma vez' if sum/int(n) >= int(preco) else "rockeiros trabalhando ja")
