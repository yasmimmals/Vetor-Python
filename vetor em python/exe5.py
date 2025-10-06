vetor1 = []
vetor2 = []
vetsoma = []


tamVet = 50


print(f"--- Digite os {tamVet} elementos do primeiro vetor ---")
for i in range(tamVet):
  while True:
    try:
      numero = int(input(f"Digite o {i+1}º número do vetor 1: "))
      vetor1.append(numero)
      break
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"\n--- Digite os {tamVet} elementos do segundo vetor ---")
for i in range(tamVet):
  while True:
    try:
      numero = int(input(f"Digite o {i+1}º número do vetor 2: "))
      vetor2.append(numero)
      break
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

for i in range(tamVet):
  soma = vetor1[i] + vetor2[i]
  vetsoma.append(soma)

print("\n--- Vetor resultante da soma ---")
print(vetsoma)
