x = int(input())
for i in range(x): 
    a = input()
    b = ''
    flag = False
    for c in a:
        if(65 <= ord(c) <= 90 or 97 <= ord(c) <= 122):
            if(flag):
                print(candidate * int(b), end='')
                b = ''
            flag= False
            candidate = c
        elif(48 <= ord(c) <= 57):
            flag = True
            b += c
    print(candidate * int(b))