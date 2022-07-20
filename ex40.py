x = int(input())

i = 2
primo = True

while i*i <= x and primo:
    if x%i == 0:
        primo = False
    i += 1
    
if primo and x>1:
    print('Emidio')
else:
    print('Faina')