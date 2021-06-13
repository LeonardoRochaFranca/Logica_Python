print("Bem vindo!")
print("---------------------")
print("Digite 1 para adicionar")
print("Digite 2 para subtrair")
print("Digite 3 para multiplicar")
print("Digite 4 para dividir")
print("Digite 0 para encerrar o programa")
print("---------------------")
cont = int(input("Digite o código da operação: "))
while cont != 0:
    x = int(input("Digite o número: "))
    y = int(input("Digite o número: "))
    if cont == 1:
        print("Adição")
        print(x+y)
    elif cont == 2:
        print("Subtração")
        print(x-y)
    elif cont == 3:
        print("multiplicação")
        print(x*y)
    elif cont == 4:
        print("Divisão")
        print(x/y)
    else:
        print("Digite um código válido")
    cont = int(input("Digite o código da operação: "))

print("Programa encerrado")
