palavras = []
qtd_5 = 0

for i in range(8):
    palavras.append(input("Digite uma palavra: "))

for palavra in palavras:
    if(len(palavra) > 5):
        print(palavra)
        qtd_5 +=1
print("Quantidade de palavras maiores que cinco: ", qtd_5)