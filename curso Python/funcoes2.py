def contador(i, f, p):
    """
    DOCSTRINGS
    Faz uma contagem e mostra na tela

    Args:
        i : inicio da contagem
        f : fim da contagem
        p : passo da contagem
    """
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM")


contador(0, 15, 3)
help(contador)


# exe101
def voto(ano):
    import datetime

    idade = datetime.date.today().year - ano
    if idade < 18:
        return f"com {idade} anos: NÃO VOTA"
    elif idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    else:
        return f"Com {idade} anos: VOTO OPICIONAL"


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))


# exe102
import math


def fatorial(n, show=False):
    if show:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f
    elif not show:
        print(n, end="")
        for c in range(n, 1, -1):
            print(f" X {c-1}", end="")
        print(f" = {math.factorial(n)}")


a = int(input("Digite o fatorial: "))


while True:
    b = (
        str(input("Digite [S] para mostra conta e [N] para mostrar resultado: "))
        .lower()
        .strip()[0]
    )
    if b == "n":
        h = fatorial(a, show=True)

        break
    elif b == "s":
        h = fatorial(a, show=False)
        break
    else:
        print("Digite uma opção valida!!!")

print(h)


# exe102
def fatorial(n, show=False):
    """calcula o fatorial de um número

    Args:
        n (_type_):O númerro a ser calculado
        show (bool, optional): (opicional) Mostrar ou não a conta ).

    Returns:O valor fatorial de n

    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print("X", end=" ")
            else:
                print("=", end=" ")
        f *= c
    return f


print(fatorial(5, show=True))


# exe103
def ficha(nome="<desconhecido>", gol=0):
    print(f"O jogador {nome} fez {gol} gol(s) no campeonato.")


n = str(input("Nome do Jogador: "))
g = str(input("Números de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == "":
    ficha(gol=g)
else:
    ficha(n, g)


# exe104
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31mERRO! Digite um número inteiro válido\033[m")
        if ok:
            break
    return valor


n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}")


# exe105
def notas(*n, sit=False):
    """
    Calcula estatísticas de notas informadas.

    Parâmetros:
    *n : float
        Uma ou mais notas do aluno.
    sit : bool, opcional
        Indica se deve incluir a situação do aluno com base na média.
        Por padrão é False.

    Retorno:
    dict
        Um dicionário contendo:
        - total: quantidade de notas
        - maior: maior nota informada
        - média: média das notas
        - situação: (opcional) avaliação da média:
            "BOA"       -> média >= 7
            "RAZOÁVEL"  -> 5 <= média < 7
            "RUIM"      -> média < 5

    Exemplo:
    >>> notas(5, 7, 8, sit=True)
    {'total': 3, 'maior': 8, 'média': 6.67, 'situação': 'RAZOÁVEL'}
    """

    total = maior = cont = 0
    teste = {}

    for c in n:
        total += c
        cont += 1
        if c > maior:
            maior = c

    media = total / cont
    teste["total"] = cont
    teste["maior"] = maior
    teste["média"] = media
    if sit:
        if media >= 7:
            teste["situação"] = "BOA"
        elif media >= 5:
            teste["situação"] = "RAZOÁVEL"
        elif media < 5:
            teste["situação"] = "RUIM"

    return teste


j = [3.5, 6, 6.5, 2, 7, 4]
resp = notas(*j, sit=False)

print(resp)
help(notas)


# exe105
def notas(*n, sit=False):

    teste = {}

    teste["total"] = sum(n)
    teste["maior"] = max(n)
    teste["menor"] = min(n)
    teste["média"] = sum(n) / len(n)
    if sit:
        if teste["média"] >= 7:
            teste["situação"] = "BOA"
        elif teste["média"] >= 5:
            teste["situação"] = "RAZOÁVEL"
        elif teste["média"] < 5:
            teste["situação"] = "RUIM"

    return teste


resp = notas(8, 6, sit=True)

print(resp)
# help(notas)
