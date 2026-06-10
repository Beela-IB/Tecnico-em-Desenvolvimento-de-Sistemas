tipo_corrida = print("Digite o tipo de corrida desejada: \n 1 - Econômica \n 2 - Conforto \n 3 - Luxo \n")

opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print("Categoria escolhida = Econômica")
    case 2:
        print("Categoria escolhida = Conforto")
    case 3:
        print("Categoria escolhida = Luxo")
    case _:
        print("Opção inválida!")