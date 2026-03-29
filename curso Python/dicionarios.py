# exe 90
aluno = {}
aluno["nome"] = str(input("Nome: "))
aluno["media"] = int(input(f"Média de {aluno['nome']}: "))
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
if aluno["media"] >= 7:
    print("A situação é igual a APROVADO")
else:
    print("A situação é igual a REPROVADO")
# exe 91
import random
import time

ordem = []
ind = 0
lista = []
sorteio = {}
for j in range(1, 5):
    sorteio["jogador"] = random.randint(1, 6)
    lista.append(sorteio.copy())
    print(f"O jogador {j} tirou {sorteio['jogador']}")
    time.sleep(0.7)
for p in lista:
    print(p["jogador"])
    if p["jogador"] > ind:
        ind = p["jogador"]
    else:
        print("oi")
print(f"O vencedor foi {ind}")
# for j in sorteio.copy():
#     print(f"Em {j}º lugar tirou {j} ")
# print(sorteio)
print(lista)

# exe 92
import datetime

geral = {}
geral["nome"] = str(input("Nome: "))
geral["ano"] = int(input("Ano de nascimento: "))
geral["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
idade = datetime.date.today().year - geral["ano"]
while True:
    if geral["ctps"] == 0:
        print(f'Nome tem o valor {geral["nome"]}')
        print(f"A idade tem o valor {idade} ")
        print(f'Ctps tem o valor {geral["ctps"]}')
        break
    else:

        geral["contratacao"] = int(input("Ano de caontratação: "))
        geral["salario"] = float(input("Salário: "))
        print(geral)
        print(f'Nome tem o valor {geral["nome"]}')
        print(f"A idade tem o valor {idade} ")

        print(f'Ctps tem o valor {geral["ctps"]}')
        print(f'Contratação tem o valor {geral["contratacao"]}')
        print(f'Salário tem o valor {geral["salario"]}')
        tempo = datetime.date.today().year - geral["contratacao"]
        apo = (35 - tempo) + idade
        print(f"Você vai se aposentar com {apo} anos")
        break

# exe 93
geral = {}
geral["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f'Quantas partidas {geral["nome"]} jogou: '))
gols = []
totalgol = 0
for p in range(0, partidas):
    gol = int(input(f"Quantos gols na partida {p}? "))
    gols.append(gol)
    totalgol += gol
geral["gols"] = gols
geral["total"] = totalgol

print("=-" * 30)
print(geral)
print("=-" * 30)
print()

print(f'O campo nome tem o valor {geral["nome"]}.')
print(f"O campo gols tem o valor {geral['gols']}.")
print(f'O campo total tem o valor {geral["total"]}.')
print()

print("=-" * 30)

print()

print(f'O jogador {geral["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(geral["gols"]):
    print(f"    => Na partida {i}, ele fez {g} gols.")
print(f'Foi um total de {geral["total"]} gols.')


print()

# exe 94
pessoa = {}
grupo = []
mulheres = []
soma = 0
acima = []
while True:
    pessoa["nome"] = str(input("Nome: ")).upper()
    pessoa["sexo"] = str(input("Sexo: [F/M] ")).upper().strip()[0]
    pessoa["idade"] = int(input("Idade: "))
    grupo.append(pessoa.copy())
    if pessoa["sexo"] == "F":
        mulheres.append(pessoa.copy())

    pessoa.clear()
    resposta = str(input("Quer continuar? [S/N] ")).lower().strip()[0]
    if resposta == "n":
        break


for m in grupo:
    soma += m["idade"]
media = soma / len(grupo)
for h in grupo:
    if h["idade"] >= media:
        acima.append(h.copy())
print("=-" * 35)
print()
print(f"O grupo tem {len(grupo)} pessoas.")
print(f"A média de idade é de {media:.2f} anos.")
print("As mulheres cadastradas foram: ", end=" ")
for m in mulheres:
    print(m["nome"], end=" ")
print()
print("Lista das pessoas acima da média:")
for p in acima:
    for i, n in p.items():
        print(f" {i} = {n};", end="")
    print()

print("=-" * 35)
print()


# exe 95
geral = {}
total = []
while True:
    geral["nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {geral["nome"]} jogou: '))
    gols = []
    totalgol = 0
    for p in range(0, partidas):
        gol = int(input(f"Quantos gols na partida {p}? "))
        gols.append(gol)
        totalgol += gol
    geral["gols"] = gols
    geral["total"] = totalgol
    total.append(geral.copy())
    geral.clear()
    resposta = str(input("Quer continuar? [S/N] ")).lower().strip()[0]
    if resposta == "n":
        break
print("-=" * 20)
print(f"{'Cod':<6}{'Nome':<10}{'Gols':<15}{'Total':^5}")
print("-" * 40)

for i, p in enumerate(total):
    # print(p)
    print(f"{i:<6}{p['nome']:<10}{str(p['gols']):<15}{p['total']:^5}")
print("-" * 40)
print()
while True:
    dados = int(input("Mostrar dados de qual jogador? (999 papa parar)"))
    if dados == 999:
        break
    else:
        for i, p in enumerate(total):
            if dados == i:
                print(f"-- LEVANTAMENTO DO JOGADOR {p['nome']}:")
                for m, l in enumerate(p["gols"]):
                    print(f"No jogo {m} ele fez {l} gols.")
