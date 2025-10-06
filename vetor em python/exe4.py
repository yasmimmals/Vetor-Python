vetor = []
print("Digite 10 números inteiros:")
for i in range(10):
  while True:
     numero = int(input(f"Digite o {i+1}º número: "))
     vetor.append(numero)
     break
   
vetorMult= []
for numero in vetor:
    vetorMult.append(numero * 3)

print("\nO vetor com cada número multiplicado por 3 é:")
print(vetorMult)
