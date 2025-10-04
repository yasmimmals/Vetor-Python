soma = 0
media = 0
alunos = 0
notas = []
notaMaior = 0

alunos = int(input("Entre com a quantidade de aluno: "))
for num in range(0, alunos, 1):
        notas.append(int(input(f"Digite a {num+1}º nota: ")))
        soma += notas[num]
        
        
media = soma / alunos 
for num in range(alunos):
    if notas[num] > media:
        notaMaior += 1
print("--- MÉDIA ---")
print(f"\nA média da turma é: {media}")
print("---Nota acima da média---")
print(f"A nota acima da média é: {notaMaior}")

