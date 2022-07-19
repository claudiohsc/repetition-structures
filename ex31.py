n = int(input())

print('1 elefante incomoda muita gente...')
print('2 elefantes incomodam, incomodam muito mais...')
elefantes = 2

while elefantes <= n:
    print(str(elefantes) + ' elefantes incomodam muita gente...')
    print(str(elefantes+1) + ' elefantes incomodam', end = '')
    c = 1
    while c <= elefantes:
        print(', incomodam', end = '')
        c += 1
    print(' muito mais...')
    elefantes += 1