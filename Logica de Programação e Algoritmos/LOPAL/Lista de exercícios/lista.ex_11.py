#Leia 7 n ́umeros e armazene em um vetor. Exiba a soma dos elementos.

vetor = []
soma = 0

for i in range(7):
    num = int(input("Digite um número: "))
    vetor.append(num)
    soma = soma + num
print("A soma de todos os números é: ", soma)