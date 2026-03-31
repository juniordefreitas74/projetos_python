# EXE 96


def area():
    mult = conta[0] * conta[1]
    print(f"A área do terreno {conta[0]} x {conta[1]} é de {mult:.2f} m²")


conta = []
print("Controle de terrenos")
print("-" * 20)
conta.append(float(input("LARGURA (m): ")))
conta.append(float(input("COMPRIMENTO (m): ")))

area()

# EXE 96


def area(larg, comp):
    a = larg * comp
    print(f"A área do terreno {larg} x {comp} é de {a:.2f} m²")


print("Controle de terrenos")
print("-" * 20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)


# EXE 97
def escreva():
    print("↦" * len(frase))
    print(f"{frase}")
    print("↤" * len(frase))


frase = str(input("digite uma palavra: "))
escreva()


# EXE 97
def escreva(msg):
    frase = len(msg) + 4
    print("↦" * frase)
    print(f"{msg}".center(frase))
    print("↤" * frase)


escreva("Junior de Freitas")
escreva("São Paulo Futebol Clube")
escreva("FF")

# EXE 98
import time


def contmais(i, f, p):

    print("↦" * 35)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    for i in range(1, 11):
        print(i, end=" ", flush=True)
        time.sleep(0.4)
    print("FIM!")
    print("↦" * 35)


def contmenos(i, f, p):
    print("↦" * 35)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    for i in range(10, -1, -2):
        print(i, end=" ", flush=True)
        time.sleep(0.4)
    print("FIM!")
    print("↦" * 35)


def contador(ini, fim, passo):

    print("↦" * 35)
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}")
    if ini < fim and passo > 0:
        for i in range(ini, fim + 1, passo):
            print(i, end=" ", flush=True)
            time.sleep(0.4)
    elif fim < ini and passo > 0:
        for i in range(ini, fim - 1, -passo):
            print(i, end=" ", flush=True)
            time.sleep(0.4)
    elif fim < ini and passo < 0:
        for i in range(ini, fim - 1, passo):
            print(i, end=" ", flush=True)
            time.sleep(0.4)
    elif fim < ini and passo == 0:
        for i in range(ini, fim - 1, time.sleep(0.4) - 1):
            print(i, end=" ", flush=True)
            time.sleep(0.4)
    elif fim > ini and passo == 0:
        for i in range(ini, fim + 1, 1):
            print(i, end=" ", flush=True)
            time.sleep(0.4)

    print("FIM!")
    print("↦" * 35)


contmais(1, 10, 1)

contmenos(10, 0, 2)
print("Agora é sua vez de personalizar a contagem")
contador(int(input("Ínicio: ")), int(input("Fim: ")), int(input("Passo: ")))


# EXE 99
import time


def maior(*num):
    cont = maior = 0
    print("=-" * 30)
    print("Analisando os valores passados...")
    for i in num:
        print(i, end=" ", flush=True)
        time.sleep(0.3)
        if i > maior:
            maior = i
        cont += 1
    print(f"Foram adicionados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


# EXE 100
import random


lista = []


def sorteio():
    for i in range(0, 5):
        num = random.randint(0, 100)
        lista.append(num)
    print("Sorteando 5 valores da lista: ", end="")
    for j in lista:
        print(j, end=" ")
    print("PRONTO!")


def pares():
    print("Somando os valores pares de ", end="")
    print(f"{lista}, temos ", end="")
    soma = 0
    for j in lista:
        if j % 2 == 0:
            soma += j
    print(f"{soma} ")
    print()


sorteio()
pares()

# EXE 100
import random
import time


numeros = []


def sorteio(teste):
    print("Sorteando 5 valores da lista:")
    for i in range(0, 5):
        n = random.randint(0, 20)
        teste.append(n)
        print(f"{n}", end=" ", flush=True)
        time.sleep(0.4)
    print("PRONTO!")


def somapar(lista):
    soma = 0
    for s in lista:
        if s % 2 == 0:
            soma += s
    print(f"Somando os valores pares da {lista}, temos {soma}")


sorteio(numeros)
somapar(numeros)
