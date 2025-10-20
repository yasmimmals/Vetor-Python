def somatorio(n):
    s = 1
    for i in range (2, n+1, 1):
        s += (i/i**2)
    return s
n = int(input('Digite um número: '))
result = somatorio(n)
print(f'Resultado = {result}')

#2
def main():
    N = int(input("digite o valor de um numero"))
    return N

def somatoria(N): 
    S =0

    for i in range(1,N+1):
        S= i /(i*i)
        print(f"{S} = {i}/{i*i}")
        
    
N= main()
soma = somatoria(N)

print(f"o valor da somatoria é {soma}")