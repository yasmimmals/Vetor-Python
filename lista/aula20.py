n = int(input('Digite o número de alunos: '))
lista = []
soma = 0
maior = 0
for i in range (n):
    lista.append(int(input(f"Digite a nota do {i+1}º aluno: ")))
maior = lista[0]

for i in lista:
    soma += i
    if i > maior:
        maior = i

media = soma/n

print(f'A média das notas é {media}')
print(f'A maior nota é {maior}')