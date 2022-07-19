s = input()
min = False
mai = False
num = False

if((len(s) > 32) or (len(s) < 6)):
    print('Senha invalida.')
else:
    for i in s:
        if(((ord(i))>64) and ((ord(i))<91)):
            mai = True
        elif(((ord(i))>96) and ((ord(i))<123)):
            min = True
        elif(((ord(i))>47) and ((ord(i))<58)):
            num = True
        else:
            mai = False
            break
        
    if(mai and min and num):
        print('Senha valida.')
    else:
        print('Senha invalida.')