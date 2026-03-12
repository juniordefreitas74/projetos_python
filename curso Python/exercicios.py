# ex 65
op = "s"
media = 0
soma = 0
cont = 0
maior = 0
menor = 0
while op == "s":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    op = str(input("Digite [S] para continuar e [N] para parar: ")).lower()
media = soma / cont

print(f"  A media é de {media:.2f} o maior valor é {maior} e o menor é {menor} ")
