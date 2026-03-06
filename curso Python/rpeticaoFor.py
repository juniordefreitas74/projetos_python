# exercicio 46
import time


for c in range(10, -1, -1):
    print(c, "...")
    time.sleep(1)
print("*****FELIZ ANO NOVO!*****")


# exercicio 47
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
print("fim")

# exercicio 47
for c in range(2, 51, 2):
    print(c)
print("fim")


# exercicio 48
s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        contador += 1
        # print(c)
        # print(c)
print("a soma é: ", s)
print(contador)

print("fim")

# exercicio 49
tab = int(input("Digite a tabuada que quer saber: "))
for t in range(1, 11):
    print(f"{tab}x{t}={t * tab}")

# exercicio 50
soma = 0
for d in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares é: \033[1;32m{soma}\033[m")

# exercicio 51
# an=a1+(n-1).r
# Onde:
# an = termo que você quer descobrir
# 𝑎1= primeiro termo (qual numero começa)
# n = posição do termo (qual posição vc quer achar)
# r = razão (valor que soma ou subtrai a cada termo)de quanto em quanto pula
a1 = int(input("Digite o primeiro termo:"))
r = int(input("Digite a razão: "))
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(f" {n}º termo = {an}")

# exercicio 52
primo = 0
n = int(input("Digite um número: "))
for p in range(1, n + 1):
    teste = n % p
    if teste != 0:
        primo += 1

if primo == n - 2:
    print(f" o número {n} é primo")
elif primo != n:
    print(f"O número {n} não é primo")

# exercicio 53
frase = str(input("digite um palindromo: "))
frase2 = frase.replace(" ", "")
lista = list(frase2)
corte = lista

if lista[::] == lista[::-1]:
    print(f"A frase {frase} é um palindromo.")
else:
    print(f"a frase: {frase} não é um palindromo")

# exercicio 54
import datetime

maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input("Digite o ano de nascimento (exemplo 1974: )"))
    idade = datetime.date.today().year - ano
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1


print(f"Temos {maior} pessoas maiores de 21 anos e {menor} pessoas menores de 21 anos.")

# exercicio 55
lista = []
for p in range(1, 6):
    peso = float(input(f"Qual o peso da {p}ª pessoa: "))
    lista.append(peso)

print(f" A pessoa mais leve tem {min(lista)}Kg e a mais pesada tem {max(lista)}Kg")

# exercicio 56
media = 0
soma = 0
homem = []
idhomem = 0
idmulher = 0
for p in range(1, 5):
    print(f"------{p}ª Pessoa ------")
    nome = str(input("Nome:"))
    idade = int(input("Idade: "))
    soma += idade
    sexo = str(input("Sexo [M/F]: ")).lower()
    media = soma / p
    if sexo == "m" and idade > idhomem:
        idhomem = idade
        homem = nome
    elif sexo == "f" and idade < 20:
        idmulher += 1
print(f"O homem mais velho é {homem} com {idhomem} anos")
print(f"A média de idade do grupo é {media}")
print(f"Temos {idmulher} mulher(es) menor(es) de 20 anos.")
