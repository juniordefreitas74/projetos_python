# exe 72
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
ext = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezeseis",
    "dezesete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    entrada = int(input("Digite um número entre 0 e 20: "))
    if entrada >= 0 and entrada <= 20:
        pos = num.index(entrada)
        break
print(f"Você digitou o número {ext[pos]}")

# exe 73
brasileirao = (
    "São Paulo",
    "Palmeiras",
    "Fluminense",
    "Bahia",
    "Flamengo",
    "Cortiba",
    "Gremio",
    "Corinthians",
    "Bragentino",
    "Athletico-PR",
    "EC Vitória",
    "Chapecoense",
    "Santos",
    "Vasco da Gama",
    "Atlético-MG",
    "Botafogo",
    "Remo",
    "Cruzeiro",
    "Intenacional",
)
print(brasileirao[0:5])
print(brasileirao[-4:])
print(sorted(brasileirao))
poschap = brasileirao.index("Chapecoense")
print(f"A Chapecoense está na {poschap}ª posição.")

# exe 74
import random

cont = 0
tupla = ()
num = ()
while True:
    gera = random.randint(0, 20)
    num2 = (gera,)
    num = num + num2

    # teste = num + tupla
    cont += 1

    ordem = sorted(num)
    print(ordem)
    if cont == 5:
        break

print(*num, sep=" - ")
print(f" O maior número é o {ordem[-1]}")
print(f"O menor número é o {ordem[0]}")


# exe 75
cont = 0
tupla = ()
pares = []
while cont < 4:
    num = int(input("Digite um número: "))
    tupla += (num,)
    cont += 1
    if num % 2 == 0:
        pares += (num,)

num9 = tupla.count(9)
if 3 in tupla:
    pos3 = tupla.index(3) + 1
else:
    pos3 = "0"


print(tupla)
print(f"O número 9 aparece {num9} vezes.")
print(f"O número 3 apareceu na posição {pos3}")
print(f"Os números pares digitados foram {' '.join(map(str,pares))}")


# exe 76
produtos = (
    "Lápis",
    1.75,
    "Borracha",
    2,
    "Caderno",
    15.9,
    "Estojo",
    25,
    "Tranferidor",
    4.2,
    "Compasso",
    9.99,
    "Mochila",
    120.32,
    "Canetas",
    22.30,
    "Livro",
    34.90,
)
intem = produtos[0::2]
preco = produtos[1::2]
print("-" * 50)
print("LISTA DE PREÇOS".center(50))
print("-" * 50)
for c, d in zip(intem, preco):
    print(f"{c}".ljust(30, "."), "R$", f"{d:.2f}".rjust(6))
print("-" * 50)
