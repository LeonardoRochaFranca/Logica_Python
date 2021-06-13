preco = float(input("Digite o valor do produto: "))
desconto = int(input("digite o valor de desconto (%): "))
print(f"O novo preço do produto é: R$ {(preco-(desconto/100)*preco):.2f}")
