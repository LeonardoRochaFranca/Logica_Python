x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
qtd = 0
for i in range(x,y-1,-1):
    if i%7 == 0:
        qtd+=1
        print(i)
        
print(qtd)
