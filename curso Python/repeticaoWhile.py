# ex 57
p = True
while p == True:
    sexo = input("Digite o sexo [F/M]: ").lower()
    if sexo != "m" and sexo != "f":
        print("Digite a opção correta.")
    else:
        p = False
print("fim")

# ex 58
import random

tentativas = 0
acerto = True
pc = random.randint(0, 10)
while acerto == True:
    numero = int(input("Adivinhe o número estou pensando de 1 a 10:"))
    tentativas += 1
    if numero == pc:
        print(
            f"\033[31mParabéns\033[m você acertou em \033[32m{tentativas}\033[m tentaivas!"
        )
        acerto = False
    else:
        print("Não foi esse número que eu pensei, tente novamente!")

# ex 59
numero = []
for n in range(1, 3):
    num = int(input(f"Digite o {n}º número: "))
    numero.append(num)
print(numero)
ok = True
while ok == True:
    print(
        """
======== MENU ========
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
=======================
"""
    )
    menu = int(input("Digite a opção desejada: "))
    if menu == 1:
        som = sum(numero)
        print(f"\nA soma dos números é = \033[31m{som}\033[m")
    elif menu == 2:
        teste = 1
        for i in range(len(numero)):
            mult = (numero[i]) * teste
            teste = mult
        print(f"A multiplicação dos números é = \033[1;31m{teste}\033[m")
    elif menu == 3:
        maior = max(numero)
        print(f"\nO maior número digitado foi \033[31m{maior}\033[m")
    elif menu == 4:
        numero = []
        for n in range(1, 3):
            adic = int(input("Qual número deseja adicionar: "))
            numero.append(adic)
    elif menu == 5:
        ok = False
    else:
        print("\033[1;41mDigite uma opção válida!!\033[m")
print("fim")


# ex 60
# num = int(input("Digite um número: "))

# for n in range(1, num):
#     oi = num
#     print(f"oi {oi}")
#     fat = oi * n
#     print(f" fat {fat}")
#     num += fat
#     print(f"num {num}")
# print("=", oi)

num = int(input("Digite um número: "))
oi = 1
tete = num
while oi < (num - 1):
    soma = tete * oi
    tete += soma
    oi += 1
print(f"O fatorial de {num} é {tete}")

# ex 61
# exercicio 51
# an=a1+(n-1).r
# Onde:
# an = termo que você quer descobrir
# 𝑎1= primeiro termo (qual numero começa)
# n = posição do termo (qual posição vc quer achar)
# r = razão (valor que soma ou subtrai a cada termo)de quanto em quanto pula

a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = 1
while termo <= 10:
    an = a1 + (termo - 1) * r
    print(f"O {termo}º termo é = {an}.")
    termo += 1
print("fim")

# ex 62

a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = 1
num = 10
while termo <= num:
    an = a1 + (termo - 1) * r
    print(f"O {termo}º termo é = {an}.")
    termo += 1
conf = True

while conf == True:

    print(
        """
    ===== ESCOLHA UMA DAS OPÇÕES =====
    [1] DESEJA ADICIONAR MAIS TERMOS
    [0] ENCERRAR
    """
    )
    escolha = int(input("Digite a opção: "))
    if escolha == 1:
        termos = int(input("Quantos termos quer adicionar: "))
        num2 = num + termos
        while termo <= num2:
            an = a1 + (termo - 1) * r
            print(f"O {termo}º termo é = {an}.")
            termo += 1
            num = num2

    elif escolha == 0:
        print("Obrigado e até mais!!!")
        conf = False

    else:
        print("Digite a opção correta!!")

# ex 63
num = int(input("digite um número: "))
inicio = 0
numero = 1
fibo = []
f = 0
print(f"A sequência de {num} números fibonaccis são:")
while f < num:
    fibo.append(inicio)
    soma = inicio + numero
    # print(soma, end=" ")
    numero = inicio
    inicio = soma
    f += 1
print(*fibo)

# ex 64
soma = 0
qtd = 0
veri = True
while veri == True:
    num = int(input("digite um número: "))
    if num == 999:
        veri = False
    else:
        soma += num
        qtd += 1

print(f"Foram digitados {qtd} números e a soma deles é {soma}.")


# ex 64
soma = 0
qtd = 0
veri = True
while veri == True:
    num = int(input("digite um número: "))
    if num == 999:
        veri = False
    else:
        soma += num
        qtd += 1

print(f"Foram digitados {qtd} números e a soma deles é {soma}.")

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
