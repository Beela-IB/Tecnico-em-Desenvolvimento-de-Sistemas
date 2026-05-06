#Leia 6 n ́umeros e substitua os negativos por 1.

vetor = []

for i in range(6):
    num = int(input("Digite um número: "))

    if(num < 0):
        vetor.append(1)
    else:
        vetor.append(num)

print(vetor)