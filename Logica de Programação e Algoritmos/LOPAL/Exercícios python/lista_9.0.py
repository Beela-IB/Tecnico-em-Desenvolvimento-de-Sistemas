nomes = []

for i in range(6):
    nomes.append(input("Digite os nomes: "))

nome_busca = input("Digite um nome para buscar no vetor: ")
for nome in nomes:
    if(  nomes == nome_busca):
        print("Nome encontrado!")