#Leia uma matriz 2x3 e exiba a soma de cada coluna.

linhas = 2
colunas = 3
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

print("Digite os elementos da matriz 2x3 (linha por linha):")
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input("Elemento [{i}][{j}]: "))

print("\nSoma de cada coluna:")
for j in range(colunas):
    soma_coluna = 0
    for i in range(linhas):
        soma_coluna += matriz[i][j]
    print("Coluna {j}: {soma_coluna}")