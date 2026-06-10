#Sistema de cadastro de usuários e produtos
#O sistema deverá permitir 
# - Cadastrar
# - Listar 
# - Deletar

#Criação das listas
usuarios = []
produtos = []

#--------------------------------------------------
#Função Menu Usuários

def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("-----Menu Usuários-----")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuário")
        print("3 - Deletar usuário")
        print("4 - Voltar")

        opcao_menu_usuario = int(input("Digite uma opção: "))

        match opcao_menu_usuario:

            case 1:
                nome = input("Digite o nome:")
                telefone = input("Digite o telefone:")
                email = input("Digite o email:")
                
                #Criação do json de usuários
                usuario = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                }

                #Adicionar json no array
                usuarios.append(usuario)
                print(f"Usuário {usuario["nome"]} cadastrado com sucesso!")

            #Listar usuários
            case 2:
                print("\n Lista de Usuários: ")

                if(len(usuarios) == 0):
                    print("Nenhum usuário cadastrado!")
                else:
                    for usu in usuarios:
                        print("\n")
                        print("Nome", usu["nome"])
                        print("Telefone", usu["telefone"])
                        print("Email", usu["email"])
            #Deletar usuário

            case 3:
                nome_deletar = input("Digite o nome do usuário que deseja deletar: ")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("Usuário removido com sucesso!")
                
                if(encontrado == False):
                    print("Usuário não encontrado!")

             #Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break

#--------------------------------------------------
#Função Menu Produtos

def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_produto != 5):
        print()
        print("-----Menu Produtos-----")
        print("1 - Cadastrar produto")
        print("2 - Listar produto")
        print("3 - Deletar produto")
        print("4 - Calcular total")
        print("5 - Voltar")

        opcao_menu_produto = int(input("Digite uma opção: "))

        match opcao_menu_produto:
            #Cadastrar produto
            case 1:
                nome = input("Digite o nome:")
                descricao = input("Digite a descrição:")
                quantidade = input("Digite a quantidade:")
                valor = input("Digite o valor:")
                
                #Criação do json de produtos
                produto = {
                    "nome": nome,
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "valor": valor
                }

                #Adicionar json no array
                produtos.append(produto)
                print(f"Produto {produto["nome"]} cadastrado com sucesso!")

            #Listar produtos
            case 2:
                print("\n Lista de Produtos: ")

                if(len(produtos) == 0):
                    print("Nenhum produto cadastrado!")
                else:
                    for pro in produtos:
                        print("\n")
                        print("Nome", pro["nome"])
                        print("Descrição", pro["descricao"])
                        print("Quantidade", pro["quantidade"])
                        print("Valor", pro["valor"])

            #Deletar usuário
            case 3:
                produto_deletar = input("Digite o nome do produto que deseja deletar: ")
                encontrado = False

                for pro in produtos:
                    if(pro["nome"] == produto_deletar):
                        produtos.remove(pro)
                        encontrado = True
                        print("Produto removido com sucesso!")
                
                if(encontrado == False):
                    print("Produto não encontrado!")

            #Calcular 

             #Voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break

#--------------------------------------------------
#---- Menu Principal ----

opcao_menu = 0
while(opcao_menu != 3):
    print("------ Menu - Sistema de cadastro ------")
    print("1 - Usuários")
    print("2 - Produtos")
    print("3 - Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu: 
        #Menu usuários
        case 1:
            menu_usuarios()
        #Menu produtos
        case 2:
            menu_produtos()
        case 3:
            print("Até logo!")
        case _:
            print("Opção inválida!")

        