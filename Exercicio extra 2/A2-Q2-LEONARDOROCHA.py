salario = float(input("Digite o salário base:"))
bonificacao = 0
if(salario<=500.00):
    bonificacao = salario*0.05
elif(salario<=1200.00):
    bonificacao = salario*0.12

if(salario<=600.00):
    bonificacao+=150.00
else:
    bonificacao+=100.00

print(f"O salário do funcionário com os beneficios é de R$ {salario+bonificacao:.2F}")
