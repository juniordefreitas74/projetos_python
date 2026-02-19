num = int(input("Digite um numero: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é igual a {raiz:.2f}")

########################################################
nume = float(input("Digite um numero decimal: "))
inteiro = math.floor(nume)
print(f"0 número {nume} tom a parte Inteira {inteiro}")

#######################################################
import math

comprimentoco = float(input("Dimensão cateto oposto: "))
comprimentoca = float(input("Dimensão cateto adjacente: "))
# c2 = a2 + b2
ca = comprimentoca**2

co = comprimentoco**2
hip = math.sqrt(ca + co)
print(
    f"Cateto adjacente de {comprimentoca} cm e o cateto opsto de {comprimentoco} cm terá uma hipotenusa de {hip:.2f} cm"
)
sen = comprimentoco / hip
print(f"Valor de seno é {sen:.3f}")
cos = comprimentoca / hip
print(f"Ovalor do cosseno é de {cos:.3f}")
tang = comprimentoco / comprimentoca
print(f"Ovalor da tangente é de  {tang:.3f}")

angulo = math.degrees(math.atan(tang))
print(f"O angulo é de {angulo:.2f}º")
# print("#" * 50)
# ########################################################
from math import hypot

co = float(input("Dimensão cateto oposto: "))
ca = float(input("Dimensão cateto adjacente: "))
hi = (co**2 + ca**2) ** (1 / 2)
print(f"A hipotenusa vai ser {hi:.2f}")

hip2 = hypot(co, ca)
print(f"A hipotenusa vai ser agora {hip2:.2f}")


########################################################
import math

angulo = float(input("Digite o angulo desejado: "))
radianos = math.radians(angulo)
sen = math.sin(radianos)
print(f"O seno para o âgulo de {angulo}º é de {sen:.3f}")
cos = math.cos(radianos)
print(f"O cosseno para o âgulo de {angulo}º é de {cos:.3f}")
tang = math.tan(radianos)
print(f"A tangente para o ângulo de {angulo}º é de {tang:.3f}")

########################################################
import math

ang = float(input("Digite o ângulo... "))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(
    f"Para o ânguloc{ang}º o seno será {sen:.2f}, o cosseno {cos:.2f} e a tangente {tan:.2f}."
)

########################################################
import random


aluno1 = input("Digite o nome do 1º aluno: ")
aluno2 = input("Digite o nome do 2º aluno: ")
aluno3 = input("Digite o nome do 3º aluno: ")
aluno4 = input("Digite o nome do 4º aluno: ")

outros = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(outros).capitalize()
print(f"O aluno sorteado para apagar a lousa foi {sorteio}")

########################################################

import random


aluno1 = input("Digite o nome do 1º aluno: ")
aluno2 = input("Digite o nome do 2º aluno: ")
aluno3 = input("Digite o nome do 3º aluno: ")
aluno4 = input("Digite o nome do 4º aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
# print(lista)
for ordem, aluno in enumerate(lista, start=1):

    print(ordem, "-", aluno)

########################################################
from random import shuffle

n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("digite o nome do segundo aluno: ")
n3 = input("digite o nome do terciro aluno: ")
n4 = input("digite o nome do quarto aluno: ")

lista = [n1, n2, n3, n4]

shuffle(lista)
print(f"a dordem de apresentação será")
print(lista)

########################################################

import pygame

pygame.init()  # inicia o pygame
pygame.mixer.init()  # inicia o sistema de áudio

pygame.mixer.music.load("teste.mp3")  # carrega o mp3
pygame.mixer.music.play()  # toca
pygame.mixer.music.set_volume(0.3)

input("Pressione ENTER para parar...")

########################################################
import math

num = float(input("Digite um numero fracionado... "))
inteiro = math.trunc(num)
intmodo = int(num)
print(f" o valor digitado foi{num} e o inteiro dele é {inteiro} ou {intmodo}")
