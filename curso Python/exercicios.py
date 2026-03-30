# exe 95


jogador = {}
total = []
while True:
    jogador["nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gols = []
    totalgol = 0
    for p in range(0, partidas):
        gol = int(input(f"Quantos gols na partida {p}? "))
        gols.append(gol)
        totalgol += gol
    jogador["gols"] = gols
    jogador["total"] = totalgol
    total.append(jogador.copy())
    jogador.clear()
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
