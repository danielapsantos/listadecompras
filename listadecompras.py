def listadecompras():
    while True:
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
        if selecionar not in ['1','2','3']:
            print("Opção inválida! Tente novamente!")
            continue