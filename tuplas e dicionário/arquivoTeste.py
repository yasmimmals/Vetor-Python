"""ARQUIVO DE TESTE"""
# from google.colab import drive
# drive.mount('/content/drive')

# #nome = input('Enter file:')
arquivo = open('tuplas e dicionário/teste.txt', 'r')

for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        print(palavra)