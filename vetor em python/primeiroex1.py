vet = []
soma = 0
for i in range(5):
    vet.append(int(input('Informe um valor: '))) # adiciona um item no vetor

for i in range(5):
    soma += vet[i]
print('\nVetor')
print(soma)