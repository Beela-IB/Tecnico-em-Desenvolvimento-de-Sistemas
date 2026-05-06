#Leia 8 n ́umeros e exiba apenas os maiores que a m ́edia.

numeros = []
soma = 0
media = 0

for i in range(8):
    num = int(input("Digite um número: "))
    numeros.append(num)
    soma = soma + num

media = soma / 8 
for numero in numeros:
    if(numero > media):
        print(numero,">",media)