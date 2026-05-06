#Leia uma matriz 3x2 e exiba apenas os n ́umeros maiores que 10.

matriz = []

print("Digite os elementos da matriz: ")
for i in range(3):
    linha = []
    for j in range(2):
        valor = float(input("Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\n Números maiores que 10")
for i in range(3):
    for j in range(2):
        if matriz[i][j] > 10:
            print(matriz[i][j])