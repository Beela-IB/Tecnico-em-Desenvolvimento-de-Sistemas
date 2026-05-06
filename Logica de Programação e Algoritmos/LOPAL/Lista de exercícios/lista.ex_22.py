#Leia 5 palavras e exiba apenas as que come ̧cam com a letra “A”.

for i in range(5):
    palavra = input("Digite uma palavra: ")
    if(palavra[0] == "A" or palavra[0] == "a"):
        print(palavra)
