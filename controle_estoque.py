produtos = []
produto = {"nome": "", "preco": 0, "estoque": 0, "vendidos": 0}

while True:
    menu_principal = """
    ##### Menu Principal #####

    1 - Cadastrar produto
    2 - Atualizar estoque
    3 - Atualizar preço
    4 - Registrar venda
    5 - Listar produtos
    6 - Mostrar relatório
    7 - Sair
    """
    continuar = True
    print(menu_principal)
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:

        existe = False
        while continuar:

            novo_produto = input(" Digite o produto:    ").lower()
            for duplicado in produtos:
                if novo_produto == duplicado["nome"]:
                    print("\n### O produto já foi cadastrado no estoque. ###\n")
                    existe = True
                    break
            if existe:
                break

            novo_preco = float(input("Digite o valor do produto: "))
            novo_estoque = int(input("Digite a quantidade de estoque: "))
            insere_cadastro = {
                "nome": novo_produto,
                "preco": novo_preco,
                "estoque": novo_estoque,
                "vendidos": 0,
                "vendas": 0,
            }

            produtos.append(insere_cadastro)

            while True:

                novo_cadstro = input("quer inserir mais no estoque S/N? ").lower()

                if novo_cadstro == "n":
                    continuar = False
                    break
                elif novo_cadstro == "s":
                    break

                else:
                    print("digite S ou N para continuar...")
        # for produtos_cadastrados in produtos:
        # print(
        #     f"Produto - {produtos_cadastrados['nome']} | preço R${produtos_cadastrados['preco']:.2f} | Estoque: {produtos_cadastrados['estoque']} "
        # )
    elif menu == 2:
        consulta_estoque = input(
            "Digite o produto que quer alterar ou consultar estoque: "
        )
        encontrado = False

        for lista_estoque in produtos:

            if consulta_estoque == lista_estoque["nome"]:
                print(
                    f"{lista_estoque['nome']} tem {lista_estoque['estoque']} unidades em estoque."
                )
                atualizar_estoque = input(
                    "Você deseja alterar a quantidade em estoque S/N?: "
                ).lower()
                if atualizar_estoque == "n":
                    break
                elif atualizar_estoque == "s":
                    entrada_estoque = input(
                        "Digite a nova quantide do estoque para esse produto: "
                    )
                    lista_estoque["estoque"] = int(entrada_estoque)
                    print(
                        f"Agora {lista_estoque['nome']} tem {lista_estoque['estoque']} unidades em estoque."
                    )
                    encontrado = True
                    break
                else:
                    print("Opção errada, digite S ou N para continuar...")
                    break
        if not encontrado:

            print("Produto não cadastrado!")
    elif menu == 3:
        consulta_estoque = input(
            "Digite o produto que quer alterar ou consultar preço: "
        )
        encontrado = False

        for lista_estoque in produtos:

            if consulta_estoque == lista_estoque["nome"]:
                print(
                    f"{lista_estoque['nome']} tem o preço cadastrado de R${lista_estoque['preco']:.2f}"
                )
                atualizar_preco = input("Você deseja alterar o valor S/N?: ").lower()
                if atualizar_preco == "n":
                    break
                elif atualizar_preco == "s":
                    novo_valor = input("Digite o novo preço para esse produto: ")
                    lista_estoque["preco"] = int(novo_valor)
                    print(
                        f"Agora {lista_estoque['nome']} tem o valor de R${lista_estoque['preco']:.2f} "
                    )
                    encontrado = True
                    break
                else:
                    print("Opção errada, digite S ou N para continuar...")
                    break
        if not encontrado:

            print("Produto não cadastrado!")
    elif menu == 5:
        print("""       ### LISTA DE PRODUTOS CADASTRADOS ###""")
        for lista_cadastrada in produtos:

            print(
                f"""
                  {lista_cadastrada['nome']} | {lista_cadastrada['estoque']} unid | R${lista_cadastrada['preco']:.2f}"""
            )
    elif menu == 4:

        print(produtos)
        encontrado2= False

        venda = input("Digite o nome do produto: ")
        quantidade_venda = int(input("Quantidade: "))
        for atual_venda in produtos:
            if atual_venda["nome"] == venda:
            atual_venda["estoque"] -= quantidade_venda
            atual_venda["vendidos"] += quantidade_venda
            atual_venda["vendas"] += 1

            print(atual_venda)
           


    else:
        break
    print("teste github")

>>>>>>> 042274f48434ef5e3ee833b99c61ffd8b9eabee7
