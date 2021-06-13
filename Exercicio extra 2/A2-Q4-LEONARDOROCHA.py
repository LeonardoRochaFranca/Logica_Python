valorCompra = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o seu salário: "))
parcelas = int(input("Digite a quantidade de parcelas desejadas: "))
mensalidade = valorCompra/parcelas
if mensalidade > salario*0.3:
    print("Financiamento não aprovado")
else:
    print("Financiamento aprovado")
