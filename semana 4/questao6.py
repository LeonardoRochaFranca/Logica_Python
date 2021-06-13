distancia = int(input("Qual a distância (km) você deseja percorrer?: " ))
if distancia <= 200:
    print(f"O valor será de: R${distancia*0.50:.2f}")
else:
    print(f"O valor será de: R${distancia*0.45:.2f}")
