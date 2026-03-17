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
