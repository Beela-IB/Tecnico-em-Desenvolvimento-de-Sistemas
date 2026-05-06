#Leia uma matriz 2x2 e exiba a soma de todos os elementos.

matriz = [[0, 0], [0, 0]]
soma_total = 0

print("Preencha a matriz 2x2:")
for i in range(0, 2):
    for j in range(0, 2):
        matriz[i][j] = int(input(f"Digite o valor para [{i},{j}]: "))

for i in range(0, 2):
    for j in range(0, 2):
        soma_total += matriz[i][j]

print("\nA soma de todos os valores da matriz é:",soma_total)