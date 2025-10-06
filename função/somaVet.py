vet = []
for i in range (10):
    vet.append(int(input(f"Digite o {i+1}º número: ")))
def somaVet(vet):
    soma = 0
    for i in vet:
        soma += i
    
    print(f'A soma dos valores da função é: {soma}')


somaVet(vet)