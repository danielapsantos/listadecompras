def listadecompras():

    lista = []

    while True:
        listar_produtos(lista)
        print()
        print("Lista de Compras Simples")
        print()
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Pesquisar produto")
        print("S - Sair")
        selecionar = input("Selecione uma opção ou S para sair.")

        if selecionar == 's' or selecionar == 'S':
            print("Obrigada por utilizar a Lista de Compras.")
            break

        if selecionar == "1":
            lista.append(adicionar_produto())
        elif selecionar == "2":
            # remover_produto()
            print("remover")
        elif selecionar == "3":
            print("pesquisar")
            # pesquisar_produto()
        elif selecionar not in ['1','2','3']:
            print("Opção inválida! Tente novamente!")
            continue
            

def adicionar_produto():
    nome = input("Digite o nome do item:")
    
    print("Qual a unidade de medida?")
    print("1 - Quilograma")
    print("2 - Grama")
    print("3 - Mililitro")
    print("4 - Unidade")
    print("5 - Metro")
    print("6 - Centímetro")
    opcao = input("Digite a opção:")
    while opcao not in ['1','2','3','4','5','6']:
        if opcao not in ['1','2','3','4','5','6']:
            print("Opção inválida! Tente novamente!")
            opcao = input("Digite a opção:")

    if opcao == "1":
        unidade_medida = "Quilograma"
    elif opcao == "2":
        unidade_medida = "Grama"
    elif opcao == "3":
        unidade_medida = "Mililitro"
    elif opcao == "4":
        unidade_medida = "Unidade"
    elif opcao == "5":
        unidade_medida = "Metro"
    elif opcao == "6":
        unidade_medida = "Centímetro"
         
    quantidade = input("Digite a quantidade:")
    descricao = input("Digite a descrição:")

    return {"Nome":nome, "Unidade":unidade_medida, "Quantidade":quantidade, "Descrição":descricao}

def listar_produtos(lista):
    for i in range(len(lista)):
        print(lista[i])


listadecompras()