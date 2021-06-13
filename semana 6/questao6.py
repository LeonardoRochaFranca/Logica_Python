divida = float(input("digite o valor da divida: "))
juros = int(input("digite o valor da taxa de juros: "))
pagamentoMensal = float(input("digite a parcela mensal:"))
periodo = int(divida / pagamentoMensal)
print(f"O número de meses para que a dívida seja paga é de: {periodo} meses")
totalJuros = 0
totalPago = 0
for i in range(periodo):
    totalJuros = totalJuros+(pagamentoMensal*(juros/100))        
    totalPago = totalPago + (pagamentoMensal+(pagamentoMensal*(juros/100)))
    continue
print(f"O total pago foi de R$ {totalPago:.2f}")
print(f"O total pago em juros foi de R$ {totalJuros:.2f}")
