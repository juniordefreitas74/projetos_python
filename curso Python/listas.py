# exe78
lista = []
for val in range(0, 5):
    print(f"digite o valor da posição {val}: ", end="")
    lista.append(int(input("")))
print(f"Você digitou os valores {lista}")
print(
    f"O maior valor digitado foi {max(lista)} nas posições {(lista.index(max(lista)))}... "
)
print(f"O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}")

# exe78
lista = []
maior = 0
menor = 0

for val in range(0, 5):
    print(f"digite o valor da posição {val}: ", end="")
    lista.append(int(input("")))
    if val == 0:
        maior = lista[val]
        menor = lista[val]
    else:
        if lista[val] > maior:
            maior = lista[val]
        if lista[val] < menor:
            menor = lista[val]

print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end="")
print(f"\nO menor valor digitado foi {min(lista)} nas posições ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}....", end="")


# exe 79
continuar = "s"
numeros = []
while continuar == "s":
    num = int(input("Digite um valor: "))
    if num in numeros:
        print("Número duplicado! Não vou adicionar...")
    else:
        numeros.append(num)
        print("Número cadastrado com sucesso!")
    cond = str(input("Você deseja continuar? [S/N]")).lower().strip()[0]
    if cond == "n":
        continuar = "n"
print(("=-" * 50))
print(f"Você digitou os valores {sorted(numeros)}")


# exe 80
numeros = []
cont = 0
while cont < 5:
    valor = int(input("Digite um valor: "))
    if cont == 0:
        numeros.append(valor)
        print(" adicionado no final da lista...")
        cont += 1
    elif cont > 0:
        if valor < numeros[0]:
            numeros.insert(0, valor)
            numeros.sort
            pos = numeros.index(valor)
            print(numeros)
            print(f"Adicionado na posição {pos} da lista...")
            cont += 1
        elif valor > numeros[-1]:
            numeros.append(valor)
            numeros.sort
            pos = numeros.index(valor)
            print(numeros)
            print(f"Adicionado na posição {pos} que é o final da lista...")

            cont += 1
        else:
            numeros.insert(1, valor)
            print("Adicionado na posição 1 da lista...")
            print(numeros)
            print("oi")
            cont += 1
print(f"Os valores digitados em ordem foram {sorted(numeros)}")

# exe 80
lista = []
for c in range(0, 5):
    numero = int(input("Digite um número: "))
    if c == 0:
        lista.append(numero)
        print("Adicionado ao final da lista")
    elif numero > lista[-1]:
        lista.append(numero)
        print("Adicionado ao final da lista")
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f"Adicionado na posição {posicao} da lista...")
                break
            posicao += 1
print("+:" * 30)
print(f"Os valores digitados foram {sorted(lista)}")


# exe 81
cont = 0
lista = []
valor5 = 0
pare = "s"
while pare == "s":
    num = int(input("Digite um número: "))
    print("Você deseja continuar [S/N]: ", end="")
    cond = str(input("")).lower().strip()[0]
    if num == 5:
        valor5 += 1

    lista.append(num)
    cont += 1
    if cond == "n":
        pare = "n"
print("=:" * 50)
print(f"Você digitou {cont} elementos.")
print(f"Os valores em ordem decrescente foram {(sorted(lista))[::-1]}")
if valor5 > 0:
    print(f"O valor 5 faz parte da lista!")
else:
    print(" O valor 5 não foi encontrado na lista!")

# exe 82
saida = "s"
lista = []
par = []
impar = []
while saida == "s":
    num = int(input("Digite um número: "))
    lista.append(num)

    cond = str(input("Deseja continuar [S/N]: ")).lower().strip()[0]
    if cond == "n":
        saida = "n"
for p in lista:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")

# exe 83
abre = 0
fecha = 0
exp = str(input("Digite uma expressão: "))
a = exp.count("(")
abre = a
f = exp.count(")")
fecha = f
if abre == fecha:
    print("Sua expressão é válida!")
else:
    print(" Sua expressão está errada!")

# exe 83
lista = []
abre = 0
fecha = 0
exp = str(input("Digite uma expressão: "))
for c in exp[:]:
    lista.append(c)
a = lista.count("(")
abre = a
f = lista.count(")")
fecha = f
if abre == fecha:
    print("Sua expressão é válida!")
else:
    print(" Sua expressão está errada!")
