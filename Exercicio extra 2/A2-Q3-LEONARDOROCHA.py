altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
if(altura < 1.20):
    if(peso <= 60.0):
        print("A")
    elif(peso <=90.0):
        print("D")
    else:
        print("G")
elif(altura <= 1.70):
    if(peso <= 60.0):
        print("B")
    elif(peso <=90.0):
        print("E")
    else:
        print("H")
else:
    if(peso <= 60.0):
        print("C")
    elif(peso <=90.0):
        print("F")
    else:
        print("I")
