def main():
    vet = []
    for i in range(5):
        vet.append(int(input(f"Digite o valor do {i+1}º número do vetor: ")))
    return vet

def Pmaior(vet):
    maior = vet[0]
    for i in range(len(vet)):
        if vet[i] > maior:
            maior = vet[i]
    return maior

def SegMaior(vet, maior):
    seg_maior = vet[0]
    for i in range(len(vet)):
        if vet[i] != maior:
            if seg_maior < vet[i]:
                seg_maior = vet[i]
    return seg_maior


vet = main()
maior = Pmaior(vet)
seg = SegMaior(vet, maior)

print(f"O maior número do vetor é {maior}")
print(f"O segundo maior número do vetor é {seg}")
