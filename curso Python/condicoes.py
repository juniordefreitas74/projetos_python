# desafio 28
import random

num = [0, 1, 2, 3, 4, 5]
sort = random.choice(num)
# print(sort)
adv = int(input("Adivinha que número estou pensando de 0 a 5: "))
if sort == adv:
    print(f"Parabéns você adivinhou que meu número era {sort}")
else:
    print(f"Que pena você não acertou, eu pensei no número {sort}")
print("Tchau!! Até a proxima vez!!")

# desafio 28

import random
import time

pc = random.randint(0, 5)
print("-=-" * 20)
print("Tente adivinhar o número que vou pensar entre 0 e 5")
print("-=-" * 20)
adv = int(input("Adivinha que número estou pensando: "))
print("PROCESSANDO...")
time.sleep(1.3)
if adv == pc:
    print(f"Parabéns você adivinhou que meu número era {pc}")
else:
    print(f"Que pena você não acertou, eu pensei no número {pc}")
print("Tchau!! Até a proxima vez!!")


# desafio 29
velo = int(input("Qual a velocidade do carro? "))
if velo > 80:
    multa = (velo - 80) * 7
    print("Você foi multado por excesso de velocidade! ")
    print(f"Você passou a {velo}Kh em uma estrada de 80 Kh!")
    print(f"Sua multa será no valor de R${multa:.2f}")
else:
    print("Voce passou abaixo da velocidade permitida.")

# desafio 29
velo = int(input("Qual a velocidade do carro? "))
if velo > 80:
    multa = (velo - 80) * 7
    print("Você foi multado por excesso de velocidade! ")
    print(f"Você passou a {velo}Kh em uma estrada de 80 Kh!")
    print(f"Sua multa será no valor de R${multa:.2f}")

print("Tenha um bom dia, dirija com segurança.")


# desafio 30
num = int(input("Digite um número inteiro: "))
cond = num % 2
if cond == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")

# desafio 31

dist = int(input("Quantos Km você vai percorrer? "))
if dist <= 200:
    print(f"Sua passagem será no valor de R${dist*0.5:.2f} pq vc rodará {dist} Km")
else:
    print(f"Sua passagem custará R${dist*0.45:.2f} pq vc rodará {dist} Km")

# desafio 32
ano = int(input("Digite um ano inteiro (Ex. 2020): "))
biss = ano % 4
# print(biss)
if biss == 0:
    print(f"O ano de de {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto")

# desafio 32
import datetime

ano = int(input("Digite um ano inteiro ou coloque 0 para analizar o ano atual: "))
if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de de {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto")

# desafio 33
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lista = [n1, n2, n3]
print(f"O maior número digitado foi {max(lista)} e o menor foi {min(lista)}.")


# desafio 34
s = float(input("Digite o valor de seu salário:"))
if s > 1250:
    print(
        f"Você terá um aumento de 10% R${(s*1.1)-s:.2f} e seu novo salário será de R${s*1.1:.2f}"
    )
else:
    print(
        f"Você terá uma aumento de 15% R${(s*1.15)-s:.2f} e seu novo salário será de R${s*1.15:.2f}"
    )


# desafio 35
# a<b+c
# 𝑏<𝑎+𝑐
# c<a+b
a = float(input("Digite o tamanho da primeira reta: "))
b = float(input("Digite o tamanho da segunda reta: "))
c = float(input("Digite o tamanho da terceira reta: "))
if a < b + c and b < a + c and c < a + b:
    print("Forma triângulo")
else:
    print("Não forma um triâgulo")
