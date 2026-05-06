#Leia 5 n ́umeros e verifique se existe algum n ́umero repetido.
vetor = []

for i in range(5):
    num = int(input("Digite um número: "))
    vetor.append(num)

    if(num == num):
        print("Não há números repetidos")
    else:
        ("Existem números repetidos")