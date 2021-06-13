velocidade = int(input("digite a velocidade:" ))
if velocidade > 60:
    print("VOCÊ FOI MULTADO!")
    print(f"O valor da multa é de R$ {(velocidade - 60)*5:.2f}")
    
