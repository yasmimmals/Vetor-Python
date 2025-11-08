contProva = 0
soma = 0
bimestre = 0
media = 0
acima = 0
somaTotal = 0
vet = []
alunos = int(input('Digite a quantidade de alunos: '))
for i in range(alunos):
    trab = float(input(f'Digite a nota do trabalho do {i+1} aluno: '))
    prova = float(input(f'Digite a nota da prova do {i+1} aluno: '))
    if prova > trab:
        contProva += 1
    soma = prova + trab
    if soma >= 6.0:
        bimestre +=1
    somaTotal += prova + trab
    vet.append(soma)
media = somaTotal/alunos
for i in range(alunos):
     if vet[i] > media:
        acima += 1
print('---Resultado---')
print(f'A quantidade de alunos com a nota bimestral maior ou igual a seis é: {bimestre}')
print(f'A média é: {media}')
print(f'A quantidade de alunos que possuem nota acima da média da turma é {acima}')