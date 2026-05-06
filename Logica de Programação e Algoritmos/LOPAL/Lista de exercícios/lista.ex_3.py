#Leia um n ́umero e verifique se ele  ́e m ́ultiplo de 5.

num = int(input("Digite um número: "))

if(num % 5 == 0):
    print(num," é múltiplo de 5!")
else:
    print(num," não é múltiplo de 5!")
