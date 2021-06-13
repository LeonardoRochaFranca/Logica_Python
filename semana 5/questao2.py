preco = float(input("Digite o valor do produto: "))
vendaMedia = int(input("Digite o valor de venda mensal média: "))
if vendaMedia < 500 or preco < 30.00:
    print ("aumento de 10%")
elif (vendaMedia >= 500 and vendaMedia < 1200) or (preco >= 30.00 and preco < 80.00):
    print ("aumento de 15%")
elif vendaMedia >= 1200 or preco >=80.00:
    print("diminuição de 20%")
