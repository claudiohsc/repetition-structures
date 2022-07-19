dolar = float(input())
qtd = int(input())
lote = int(input())

valor = dolar * qtd * 1.025
for i in range(lote):
    print(f'Lote: {i+1} - Total da venda: R$ {valor:.2f}')