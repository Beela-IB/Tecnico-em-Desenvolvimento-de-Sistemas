vetor = []
qtd_pares = 0
qtd_impares = 0

for i in range(10):
    vetor.append(int(input("Digite números inteiros (Pares ou Ímpares): ")))

for numero in vetor:
    if numero %2 == 0:
       qtd_pares+=1
    else:
        qtd_impares+=1
print("Qtd pares: ", qtd_pares, "\n Qtd impares: ", qtd_impares)