#Criando uma variável numérica
numero = 10

#Criando uma variável textual
nome = "Isabela"

#Usuário inserir um texto
nome_completo = input("Digite um nome: ")

#Usuário inserir um número inteiro
idade = int(input("Digite sua idade: "))

#Usuário inserir um número decimal
salario = float(input("Digite seu salário: "))

#Estruturas condicionais - IF
if(salario > 1500 and idade >= 18):
    print("Você pode tirar carta!")
elif(salario < 1500 or idade < 18):
    print("Você não pode tirar carta!")
else:
    print("Inválido")

#Estruturas condicionais exemplo 2
turno = input("Digite seu turno (M/V/N): ")

if(turno == "M"): #Utilize dois iguais para comparar
    print("Bom dia! ")
elif(turno == "V"):
    print("Boa tarde! ")
elif(turno == "N"):
    print("Boa noite! ")
else: #Else não tem parênteses
    print("Inválido")

#Estrutura de repetição

#0 -> 10
for i in range(11):
    print(i)

#1 -> 15
for i in range(1, 16): #Vai do 1 ao 15
    print(i)

#5 -> 65 (aumentando de 5 em 5)
for i in range(5,66,+5): 
    print(i)

#122 -> 0 (tirando de 2 em 2)
for i in range(122,-1,-2): 
    print(i)

#Usuário escolhe o início e o fim
#inicio -> fim

inicio = int(input("Início: "))
fim = int(input("Fim: "))

for i in range(inicio,fim+1):
    print(i)

#Vetores

nomes = []

#Sempre utilizar para preencher o vetor 
for i in range(5):
    nomes.append(input("Digite um nome: "))

#Sempre utilizar para exibir o vetor
for nome in nomes:
    print(nome)