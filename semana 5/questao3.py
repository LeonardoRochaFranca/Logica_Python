custoFabrica = float(input("digite o valor: "))
if custoFabrica <= 20000.00:
    print(f"Preço do carro: {custoFabrica+(custoFabrica*0.05):.2f}")
elif custoFabrica <= 30000.00:
    print(f"Preço do carro: {custoFabrica+(custoFabrica*0.10)+(custoFabrica*0.15):.2f}")
elif custoFabrica > 30000.00:
    print(f"Preço do carro: {custoFabrica+(custoFabrica*0.15)+(custoFabrica*0.20):.2f}")
