matriz = []
maiores_5 = 0

for i in range(2):
    linha =[]
    for j in range(3):
        linha.append(int(input("Digite um valor inteiro: ")))
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i in range(2):
    for j in range(3):
        if(matriz[i][j] > 5):
            maiores_5+=1

print(maiores_5)