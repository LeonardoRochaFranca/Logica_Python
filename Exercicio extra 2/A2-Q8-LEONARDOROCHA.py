alunos=int(input("Digite a quantidade de alunos da turma: "))
aprovado = 0
reprovado = 0
provaFinal = 0
mediaGeral = 0
for i in range (alunos):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1+n2)/2
    print(f"A média do aluno {i} foi: {media}")
    mediaGeral+=media
    if media <= 2.0:
        print("Reprovado")
        reprovado=reprovado+1
    elif media <7.0:
        print("Prova final")
        provaFinal=provaFinal+1
    else:
        print("Aprovado")
        aprovado=aprovado+1

print(f"O total de alunos aprovados foi: {aprovado}")
print(f"O total de alunos que vão para a final: {provaFinal}")
print(f"O total de alunos reprovados foi: {reprovado}")
print(f"A média geral de classe é de: {mediaGeral / alunos}")
        
