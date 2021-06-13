codigo = int(input("Digite o código do produto: "))
valorTotal = 0
while codigo!= 0:
    qtd = int(input("Digite a quantidade deste produto: "))
    if codigo == 1:
        valorTotal += (5.00 * qtd)
    elif codigo == 2:
        valorTotal += (8.00 * qtd)
    elif codigo == 3:
        valorTotal += (10.00 * qtd)
    elif codigo == 5:
        valorTotal += (13.00 * qtd)
    elif codigo == 9:
        valorTotal += (16.00 * qtd)
    else:
        print("Código inválido")
    codigo = int(input("Digite o código do produto: "))
    continue
print(f"Valor total = R$ {valorTotal:.2f}")
        
