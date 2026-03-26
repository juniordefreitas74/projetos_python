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
