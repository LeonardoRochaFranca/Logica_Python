kmPercorridos = int(input("Digite a quantidade de KMs percorridos: "))
diasAlugados = int(input("Digite a quantidade de dias alugado: "))
precoTotal = (kmPercorridos*0.15) + (diasAlugados*60.00)
print(f"Preço a pagar: R$ {precoTotal:.2f}")
