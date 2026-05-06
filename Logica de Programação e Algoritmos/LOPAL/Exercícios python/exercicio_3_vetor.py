print("-------------------------")
numeros = []
soma = 0
for i in range(4):
    num = int(input("Digite um número: "))
    numeros.append(num)

for numero in numeros:
    soma = soma + numero
media = (soma)/4

if(media < 4):
    print("Reprovado")
elif(media >=4 and media <=7):
    print("Recuperação")
else:
    print("Aprovado")
