produtos = []

while True:
    try:
        menu = print("""
                    1 - Cadastrar produto
                    2 - Atualizar estoque
                    3 - Registrar venda
                    4 - Listar produtos
                    5 - Mostrar relatório
                    6 - Sair
    """)
        print(input('Escolha uma opção: '))
        if menu == 1:
            menu1 = int(input('Digite o nome do produto'))
            print(menu1)
        else:
            break

    except ValueError:
        print('Digite uma opção válida.')
        continue
