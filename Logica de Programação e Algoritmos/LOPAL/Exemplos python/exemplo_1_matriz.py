matriz = [
    ["laranja", "romã", "maçã-verde", "limão", "caqui"],
    ["berinjela", "batata", "pimentão", "pimenta", "pepino"]
]
print(matriz[0])#imprime a primeira linha (frutas)
print(matriz[1])#imprime a segunda linha (legumes)

print(matriz[0][2]) #imprime maçã-verde
print(matriz[1][3]) #imprime pimenta

#Escrever todas as linhas e colunas
print("Frutas: ")
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[0][3])
print(matriz[0][4])

print("Legumes: ")
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[1][3])
print(matriz[1][4])

#Forma simplificada de imprimir a matriz

print("Matriz completa: ")
for i in range(2): #linhas
    for j in range(5): #colunas
       print(matriz[i][j])