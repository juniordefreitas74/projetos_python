# exe 84
pessoa = list()
grupo = list()
pesado = []
leve = []
while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Peso: ")))
    grupo.append(pessoa[:])
    pessoa.clear()
    resposta = str(input("Quer continua[S/N]: "))
    if resposta == "n":
        break
for i, p in enumerate(grupo):
    if i == 0:
        pesado.append(p)
    else:
        if p[1] > pesado[0][1]:
            pesado.clear()
            pesado.append(p)
        elif p[1] == pesado[0][1]:
            pesado.append(p)

for i, l in enumerate(grupo):
    if i == 0:
        leve.append(l)
    else:
        if l[1] < leve[0][1]:
            leve.clear()
            leve.append(l)
        elif l[1] == leve[0][1]:
            leve.append(l)

print("+:" * 30)
print(f"\nO maior peso foi de {pesado[0][1]} Kg. Peso de  ", end="")
for p in pesado:
    print(f"{p[0]}...", end="")
print(f"\nO menor peso foi de {leve[0][1]} Kg. Peso de ", end="")
for q in leve:
    print(f"{q[0]}...", end="")
print(f"\nForam cadastradas {len(grupo)} pessoas.")

# exe 85


geral = [[], []]

for n in range(1, 8):
    num = int(input(f"Digite o {n}º número:"))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)
print(f"Os valores pares digitados foram{sorted(geral[0])}")
print(f"Os valores ímpares digitados foram{sorted(geral[1])}")

# exe 86
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o  valor para [{l}, {c}]: "))
print("=-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^5} ]", end="")
    print()

# exe 87
pares = coluna3 = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o  valor para [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        coluna3 += matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print("=-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^5} ]", end="")
    print()
print(f"A soma dos valores pares são {pares}")
print(f" A soma dos valores da terceira coluna é {coluna3}")
print(f"O maior valor da segunda linha é {maior}")


# exe 88
import random
import time

print("=-" * 17)
print("JOGA NA MEGA SENA".center(30))
print("=-" * 17)
sorteados = []
qtd = 0
pergunta = int(input("Quantos jogos você quer gerar?: "))
for j in range(1, pergunta + 1):
    print(f"Jogo {j}: ", end="")
    jogo = []
    while qtd != 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            qtd += 1
    time.sleep(1)
    print(f"{sorted(jogo)}")
    qtd = 0
print("=-" * 17)


# exe 89
geral = list()
while True:
    nome = str(input("Nome: ")).upper()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    geral.append([nome, nota1, nota2, media])
    perg = str(input("Quer continuar? [S/N] ")).lower().strip()[0]
    if perg == "n":
        break
print("=-" * 15)
print(f'{"Nº":<4}{'NOME':<10}{"MÉDIA":^8}')
print("-" * 30)
for i, b in enumerate(geral):
    print(f"{i:<4}{b[0]:<10}{b[3]:^8.2f}")
while True:
    ind = int(input("Mostrar notas de qual aluno? (999 para interromper )"))
    if ind == 999:
        break
    for i, b in enumerate(geral):
        if i == ind:
            print(f"Notas de {b[0]} são {[b[1],b[2]]}")
print("FINALIZANDO...")
print("<<< VOLTE SEMPRE >>>")
