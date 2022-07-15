def aprovacao(a1, a2, a3, i):
  media = (float(a1) + float(a2) + float(a3)) / 3
  if media >= 7.0:
    print(f'O ALUNO {i} FOI APROVADO')
  else:
    print(f'O ALUNO {i} FOI REPROVADO')

alunos = int(input())
for i in range(0, alunos):
  notas = input().split()
  aprovacao(notas[0], notas[1], notas[2], i)

