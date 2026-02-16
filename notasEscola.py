alunos = []
media_final = []
qtd_aprovados = 0
qtd_recuperacao = 0
qtd_reprovados = 0
continuar = True
while continuar:
    try:
        nome_aluno = input('Digite o nome do aluno:')
        while True:
            primeira_nota = float(input('Digite primeira nota:'))
            if primeira_nota >= 0 and primeira_nota <= 10:

                break
            else:
                print('A nota tem que estar entre 0 e 10!')
        while True:
            segunda_nota = float(input('Digite segunda nota:'))
            if segunda_nota >= 0 and segunda_nota <= 10:

                break
            else:
                print('A nota tem que estar entre 0 e 10!')
        while True:
            terceira_nota = float(input('Digite terceira nota:'))
            if terceira_nota >= 0 and terceira_nota <= 10:

                break
            else:
                print('A nota tem que estar entre 0 e 10!')

    except ValueError:
        print('Digite uma nota válida!')
        continue
    total = (primeira_nota + segunda_nota + terceira_nota)
    media = (total/3)
    if media >= 7:
        aprovacao = 'Aprovado'
    elif media >= 5:
        aprovacao = 'Recuperação'
    else:
        aprovacao = 'Reprovado'

    if aprovacao == 'Aprovado':
        qtd_aprovados += 1
    elif aprovacao == 'Recuperação':
        qtd_recuperacao += 1
    else:
        qtd_reprovados += 1

    # print(f'A média do aluno {nome_aluno} é de {media:.2f}')
    cadastro_aluno = {'nome': nome_aluno, '1ª nota': primeira_nota,
                      '2ª nota': segunda_nota, '3ª nota': terceira_nota, 'Total= ': total, 'média=': media, 'aprovado': aprovacao}
    alunos.append(cadastro_aluno)
    media_final.append(media)
    soma_medias = sum(media_final) / len(media_final)
    for amediaFinal in alunos:
        print(
            f"O aluno(a) {amediaFinal['nome']},\ntem a média final de {amediaFinal['média=']:.2f} e está {amediaFinal['aprovado']}")
    print(
        f'A media geral da turma é: {soma_medias:.2f} e temos {qtd_aprovados} aprovados, {qtd_recuperacao} de recuperação e {qtd_reprovados} reprovados')

    while True:
        novo_cadastro = input(
            'Quer cadastrar outro aluno? Digite "S" para sim e "N" para não: ').lower()

        if novo_cadastro == "n":
            print("Encerrando o cadastro...")
            continuar = False
            break
        elif novo_cadastro == "s":
            break
        else:
            print("Opção inválida! Por favor, digite apenas 'S' ou 'N'.")
