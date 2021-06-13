salario = float(input())
if salario <= 1250.00:
    print(f"O aumento foi de {salario*0.15:.2f}")
    print(f"O novo salário é de {salario*1.15:.2f}")
else:
    print(f"O aumento foi de {salario*0.10:.2f}")
    print(f"O novo salário é de {salario*1.10:.2f}")
