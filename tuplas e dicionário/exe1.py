nome = input('Digite o nome do arquivo de texto: ')
arquivo = open(f"tuplas e dicionário/{nome}.txt", 'r')
dic = {}

for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        dic.get(palavra, 0)
        dic[palavra] = dic.get(palavra,0)+1
        print(palavra)
print(dic)