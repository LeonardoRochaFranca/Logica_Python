cargo = int(input("Digite o código do cargo: "))
salario = float(input("Digite o salário do funcionário: "))
if cargo == 1:
    print("Escriturário")
    print(f"VALOR DO AUMENTO: R$ {salario*0.50:.2f}")
    print(f"NOVO SALÁRIO: R$ {salario+(salario*0.50):.2f}")
elif cargo == 2:
    print("Secretário")
    print(f"VALOR DO AUMENTO: R$ {salario*0.35:.2f}")
    print(f"NOVO SALÁRIO: R$ {salario+(salario*0.35):.2f}")
elif cargo == 3:
    print("Caixa")
    print(f"VALOR DO AUMENTO: R$ {salario*0.20:.2f}")
    print(f"NOVO SALÁRIO: R$ {salario+(salario*0.20):.2f}")
elif cargo == 4:
    print("Gerente")
    print(f"VALOR DO AUMENTO: R$ {salario*0.10:.2f}")
    print(f"NOVO SALÁRIO: R$ {salario+(salario*0.10):.2f}")
elif cargo == 5:
    print("Diretor")
    print("Este cargo não recebe aumento")
