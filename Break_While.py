# exe 66
n = s = c = 0

while True:
    n = int(input("digite um numero (999 para parar): "))
    if n == 999:
        break
    s += n
    c += 1
print(f"A soma dos {c} valores foi {s}!")

# exe 67
while True:
    num = int(input("Digite uma tabuada que quer saber: "))
    if num < 0:
        break
    cont = 1
    while True:
        tab = num * cont
        print(f"{num} X {cont} = {tab}")
        cont += 1
        if cont == 11:
            break

print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")

# exe 67
while True:
    num = int(input("Digite uma tabuada que quer saber: "))
    print("*" * 30)
    if num < 0:
        break
    cont = 1
    for t in range(1, 11):
        print(f"{num} x {t} = {num*t}")
    print("*" * 30)

print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")


# exe 68
import random

so = 0
eu = "p"
resultado = "ganhou"
print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR".center(30))
print("=-" * 15)
while resultado == "ganhou":
    valor = int(input("Digite um valor: "))
    condicao = str(input("Você escolhe PAR ou ÍMPAR [P/I]: ")).lower().strip()[0]
    if condicao == "p":
        eu = "p"
    elif condicao == "i":
        eu = "i"
    pc = random.randint(0, 10)
    soma = valor + pc
    if soma % 2 == 0 and eu == "p":
        print("VOCÊ VENCEU!!")
        print(f"Eu escolhi {pc} e você {valor} a soma é {soma} que é PAR ")
        print("Vamos jogar novamente...")
        so += 1
    elif soma % 2 != 0 and eu == "i":
        print("VOCÊ VENCEU!!")
        print(f"Eu escolhi {pc} e você {valor} a soma é {soma} que é IMPAR ")
        print("Vamos jogar novamente...")
        so += 1
    elif soma % 2 != 0 and eu == "p":
        print("VOCÊ PERDEU!!")
        print(f"Eu escolhi {pc} e você {valor} a soma é {soma} que é IMPAR ")
        break
    elif soma % 2 == 0 and eu == "i":
        print("VOCÊ PERDEU!!")
        print(f"Eu escolhi {pc} e você {valor} a soma é {soma} que é PAR ")
        break

print(f"GAME OVER! Você venceu {so} vezes.  ")

# exe 68
import random

vit = 0
print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR".center(30))
print("=-" * 15)
while True:
    jogador = int(input("Digite um valor: "))
    pc = random.randint(1, 10)
    soma = jogador + pc
    escolha = " "
    while escolha not in "pi":
        escolha = (
            str(input("Escolha [P] para par e [I] para impar: ")).lower().strip()[0]
        )
    print(f"Você jogou {jogador} e o computador {pc} . Total de {soma}")
    print("Voce escolheu PAR" if escolha == "p" else "Você escolheu IMPAR")
    print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR")
    if escolha == "p":
        if soma % 2 == 0:
            print(f"{soma} é PAR e você venceu!!!")
            vit += 1
        else:
            print(f"{soma} é IMPAR e você perdeu!!")
            break
    elif escolha == "i":
        if soma % 2 != 0:
            print(f"{soma} é IMPAR e você venceu!!!")
            vit += 1
        else:
            print(f"{soma} é PAR e você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {vit} vezes.")

# exe 69
continuar = ""
maior = homem = mulher20 = 0

while continuar != "n":
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        maior += 1

    sexo = str(input("Digite o Sexo [M/F]: ")).lower().strip()[0]
    if sexo == "m":
        homem += 1
    if idade < 20 and sexo == "m":
        mulher20 += 1
    continuar = str(input("Você deseja continuar? [S/N]:")).lower().strip()[0]

print(f"Temos {maior} pessoas maiores de 18.")
print(f"Temos {homem} homens cadastrados.")
print(f"Temos {mulher20} mulheres menores de 20 anos.")

# exe 69
maior = homem = mulher20 = 0
while True:
    sexo = " "
    idade = int(input("Digite a idade: "))
    while sexo not in "mf":
        sexo = str(input("Digite o Sexo [M/F]: ")).lower().strip()[0]
    if idade >= 18:
        maior += 1

    if sexo == "m":
        homem += 1
    if idade < 20 and sexo == "m":
        mulher20 += 1
    continuar = " "
    while continuar not in "sn":
        continuar = str(input("Você deseja continuar? [S/N]:")).lower().strip()[0]
    if continuar == "n":
        break

print(f"Temos {maior} pessoas maiores de 18.")
print(f"Temos {homem} homens cadastrados.")
print(f"Temos {mulher20} mulheres menores de 20 anos.")


# exe 70

produtoB = ""
cont = 0
valorb = 0
total = 0
continuar = ""
maior1000 = 0
barato = ""
valorBarato = 0

print("=->" * 10)
print("LOJAS BARATÃO".center(30))
print("=->" * 10)

while continuar != "n":
    nome = str(input("Digite o nome do produto: "))

    valor = float(input("Digite o valor do produto R$ "))
    total += valor
    if valor > 1000:
        maior1000 += 1
    if cont == 0:
        valorb = valor
        print(valorb)
    if cont > 0 and valor < valorb:
        valorb = valor
        barato = nome
        valorBarato = valor
    cont += 1

    continuar = str(input("VOCÊ QUER CONTINUAR [S/N]: ")).lower().strip()[0]

print("-+" * 15)
print("FIM DO PROGRAMA".center(30))
print("-+" * 15)

print(f"O total da compra foi R${total:.2f}")
print(f"Temos {maior1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${valorBarato}")

# exe 70
print("=->" * 10)
print("LOJAS BARATÃO".center(30))
print("=->" * 10)
total = qtd = cont = valorBarato = 0
produtoBarato = " "
while True:
    continuar = " "
    nome = input("Digite o produto: ")
    preco = int(input("Digite o preço: "))
    total += preco
    cont += 1
    if cont == 1 or preco < valorBarato:
        produtoBarato = nome
        valorBarato = preco
    if preco > 1000:
        qtd += 1
    while continuar not in "sn":
        continuar = input("Deseja continuar? [S/N]: ").lower().strip()[0]
    if continuar == "n":
        break
print(f"O total da compra é R${total:.2f}")
print(f"{qtd} produtos custam mais de R$1000,00")
print(f"O produto mais barato é o {produtoBarato} que custa R${valorBarato:.2f}")
print("\n{:-^40}".format("FIM DO PROGRAMA"))


# exe 71
print("=" * 30)
print("BANCO FF".center(30))
print("=" * 30)
saque = int(input("\nQual valor você quer sacar? R$"))
nota50 = int(saque / 50)
resto50 = saque % 50
nota20 = int(resto50 / 20)
resto20 = resto50 % 20
nota10 = int(resto20 / 10)
resto10 = resto20 % 10
nota1 = int(resto10 / 1)
print("=" * 20)
print(f"Total de {nota50} notas de R$50")
print(f"Total de {nota20} notas de R$20")
print(f"Total de {nota10} notas de R$10")
print(f"Total de {nota1} notas de R$1")
print("=" * 30)
print("Volte sempre ao BANCO FF")
print("Tenha um bom dia!")

# exe 71
print("=" * 30)
print("BANCO FF".center(30))
print("=" * 30)
saque = int(input("\nQual valor você quer sacar? R$"))
total = saque
cedula = 50
cont = 0
while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f"Total de {cont} cédulas de {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break

print("=" * 30)
print("VOLTE SEMPRE".center(30))
print("=" * 30)
