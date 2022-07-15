def soma_harmonica(x):
  if x == 1:
    return 1
  else:
    soma = 0
    for i in range(1, x+1):
      soma += 1/i
      i += 1
    
    return soma

