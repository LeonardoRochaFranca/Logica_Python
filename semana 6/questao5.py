deposito = float(input("digite o valor: "))
taxaJuros = int(input("digite o valor: "))
meses = int(input("digite a quantidade de meses para conferência:"))

for i in range (meses):
    print(f'O ganho com Juros no mês {i+1} foi de {deposito * (taxaJuros/100):.2f}')
    print(f'O total em deposito é de {deposito+(deposito * (taxaJuros/100)):.2f}')
    deposito = deposito+(deposito * (taxaJuros/100))
    print("")
    
