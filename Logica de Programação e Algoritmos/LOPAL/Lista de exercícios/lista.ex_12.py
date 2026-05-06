#Leia 5 nomes e armazene em um vetor. Exiba os nomes em ordem inversa.

vetor = []

for i in range(5):
    nome = input("Digite um nome: ")
    vetor.append(nome)
for nome in reversed(vetor):
    print(nome)