numero = int(input("Digite um numero: "))
numerosDigitados = 0
soma = 0
while numero!= 0:
    numerosDigitados=numerosDigitados+1
    soma += numero
    numero = int(input("Digite um numero: "))
    continue
print(f"foram digitados {numerosDigitados} numeros")
print(f"a soma dos numeros digitados foi de {soma}")
print(f"a média aritimética dos números digitados foi de {int(soma/numerosDigitados)}")
    
