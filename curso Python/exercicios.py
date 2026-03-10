# ex 65
veri = True
media = 0
soma = 0
lista = []
while veri == True:
    digi = int(input("Digite um número: "))
    media += 1
    soma += digi
    lista.append(digi)
    send = True
    while send == True:
        op = input("Quer continuar [S]/[N]: ").lower()
        if op == "s":
            break

        elif op == "n":
            send = False
            veri = False

        else:
            print("tetente novamente")
            send = True

print(
    f"A media é de {soma/media:.1f} o maior valor é {max(lista)} e o menor é {min(lista)}"
)
