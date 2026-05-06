#Leia 6 idades e exiba quantas s ̃ao maiores de idade.

idades = []
maior = 0

for i in range(6):
    idade = int(input("Digite a idade: "))
    idades.append(idade)

    if idade >= 18:
        maior = maior + 1

print(maior," pessoas são maiores de idade.")