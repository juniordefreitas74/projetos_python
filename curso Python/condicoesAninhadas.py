# exrecicio 36
valor_casa = float(input("Qual o valor da casa que vc quer financiar: R$"))
salario = float(input("Qua o seu salário? R$"))
anos = int(input("Em quantos anos quer financiar? "))

prestacao_mensal = valor_casa / (anos * 12)
parcela_maxima = salario * 0.3

if prestacao_mensal > parcela_maxima:
    print("\033[1;31m Empréstimo Negado \033[m")
    print(
        f"Sua parcela máxima é de R${parcela_maxima:.2f} e o valor do financiamento é de R${prestacao_mensal:.2f}"
    )
else:
    print("\033[1;32m Empréstimo aprovado \033[m")
    print(f"Sua parcela será de {prestacao_mensal:.2f}")

# exercicio 37

numero = int(input("Digite um número inteiro: "))
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

escolha = int(
    input(
        """
Digite o número referente a qual base você deseja converter
1 - Binário
2 - Octal
3 - Hexadecimal

Digite: """
    )
)
if escolha == 1:
    print(f"O número {numero} em binário é {binario}")
elif escolha == 2:
    print(f"O número {numero} em Octal é {octal}")
elif escolha == 3:
    print(f"O númer0 {numero} em Hexadcimal é {hexadecimal}")
else:
    print("Escolha errada digite 1,2 ou 3")


# exercicio 38

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O primeiro número é maior.")
elif n2 > n1:
    print("O segundo número é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")

# exercicio 39
import datetime

nasc = int(input("Digite o ano do seu nascimento:"))
anoAtual = datetime.date.today().year
idade = anoAtual - nasc
if idade < 18:
    print(f"Você ainda não precisa se alistar pois vc tem {idade} anos")
    print(f"e ainda faltam {18-idade} anos para o alistamento")
    print(f"Você terá que se alistar no ano de {(18-idade)+anoAtual}")

elif idade == 18:
    print(f"Você precisa se alistar pois vc tem {idade} anos")
else:
    print(f"Você já passou da época de alistar pois vc tem {idade} anos")
    print(f"Você deveria ter se alistada há {idade-18} anos atrás")
    print(f"Você deveria ter se alistado em {anoAtual-(idade-18)}")

# exercicio 40
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2
if media < 5:
    print(
        f"Você tirou {n1} e {n2} Sua média foi de {media:.1f} \033[1;31m ALUNO REPROVADO \033[m"
    )
elif media >= 5 and media < 6.9:
    print(
        f"Você tirou {n1} e {n2} Sua média foi de {media:.1f} \033[1;33m ALUNO EM RECUPERAÇÃO \033[m"
    )
else:
    print(
        f"Você tirou {n1} e {n2} Sua média foi de {media:.1f} \033[1;32m ALUNO APROVADO \033[m"
    )

# exercicio 41
import datetime

ano = int(input("Digite o ano de nascimento: "))
idade = datetime.date.today().year - ano
if idade <= 9:
    print(f"você tem {idade} anos e sua categoria é MIRIM")
elif idade <= 14:
    print(f"você tem {idade} anos e sua categoria é INFANTIL")
elif idade <= 19:
    print(f"Você tem {idade} anos e sua categgoria é JUNIOR")
elif idade <= 20:
    print(f"Você tem {idade} anos e sua categoria é SÊNIOR")
else:
    print(f"VOCÊ TEM {idade} anos e sua categoria é MASTER")

# exercicio 42

# desafio 35
# a<b+c
# 𝑏<𝑎+𝑐
# c<a+b
a = float(input("Digite o tamanho da primeira reta: "))
b = float(input("Digite o tamanho da segunda reta: "))
c = float(input("Digite o tamanho da terceira reta: "))
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c:
        print("Forma triângulo Equilátero")
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print("Forma um triâgulo Isóceles")
    else:
        print("Forma um triâgulo Escaleno")


else:
    print("Não forma um triâgulo")

# exercicio 43
# peso / (altura x altura)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
altura = altura / 100
imc = peso / (altura**2)
if imc < 18.5:
    print(f"Seu Imc é de {imc:.1f} e você está ABAIXO do peso")
elif imc >= 18.5 and imc < 25:
    print(f"Seu Imc é de {imc:.1f} e você está com o PESO IDEAL.")
elif imc >= 25 and imc < 30:
    print(f"Seu Imc é de {imc:.1f} e você está com o SOBRE PESO.")
elif imc >= 30 and imc < 40:
    print(f"Seu Imc é de {imc:.1f} e você está com OBESIDADE")
else:
    print(f"Seu Imc é de {imc:.1f} e você está com OBESIDADE MÓRBIDA")

# exercicio 44
print(
    """O fone de ouvido custa R$ 50,00, escolha a forma de pagamento!
      0- À vista dinheiro ou cheque
      1- À vista no cartão
      2- 2x no cartão de crédito
      3- 3x ou mais no cartão de crédito
      """
)
escolha = int(input("Digite a opção desejada: "))
fone_de_ouvido = 100
if escolha == 0:
    print(
        f"O fone custa R${fone_de_ouvido:.2f} e com o desconto de 10% fica\033[32m R${fone_de_ouvido*0.9:.2f}\033[m"
    )
elif escolha == 1:
    print(
        f"O fone custa R${fone_de_ouvido:.2f} e com o desconto de 5% fica\033[32m R${fone_de_ouvido*0.95:.2f}\033[m"
    )
elif escolha == 2:
    print(
        f"O fone custa R${fone_de_ouvido:.2f} e você pagara\033[32m R${fone_de_ouvido:.2f}\033[m em 2x de R${fone_de_ouvido/2:.2f}"
    )
elif escolha == 3:
    print(
        f"O fone custa R${fone_de_ouvido:.2f} e você pagara\033[32m R${fone_de_ouvido*1.2:.2f}\033[m em 3x de R${(fone_de_ouvido*1.2)/3:.2f}"
    )

# exercicio 45
import random

print(
    """ Vamos jogar Jokenpô!
      ======> Escolha <=====
      1- Para PEDRA
      2- Para PAPEL
      3- Para TESOURA
      """
)
digite = int(input("Digite a sua escolha: "))
escolha = ["PEDRA", "PAPEL", "TESOURA"]
sorteio = random.choice(escolha)


if digite == 1 and sorteio == "PAPEL":
    print(f"Você \033[31mPERDEU\033[m eu escolhi \033[1;33m{sorteio}\033[m")
elif digite == 1 and sorteio == "PEDRA":
    print(f" \033[33mEMPATE\033[m eu também escolhi \033[1;33m{sorteio}\033[m")
elif digite == 1 and sorteio == "TESOURA":
    print(f"Você \033[32mGANHOU\033[m eu escolhi \033[1;33m{sorteio}\033[m")

elif digite == 2 and sorteio == "TESOURA":
    print(f"Você \033[31mPERDEU\033[m eu escolhi \033[1;33m{sorteio}\033[m")
elif digite == 2 and sorteio == "PAPEL":
    print(f" \033[33mEMPATE\033[m eu também escolhi \033[1;33m{sorteio}\033[m")
elif digite == 2 and sorteio == "PEDRA":
    print(f"Você \033[32mGANHOU\033[m eu escolhi \033[1;33m{sorteio}\033[m")

elif digite == 3 and sorteio == "PEDRA":
    print(f"Você \033[31mPERDEU\033[m eu escolhi \033[1;33m{sorteio}\033[m")
elif digite == 3 and sorteio == "TESOURA":
    print(f" \033[33mEMPATE\033[m eu também escolhi \033[1;33m{sorteio}\033[m")
elif digite == 3 and sorteio == "PAPEL":
    print(f"Você \033[32mGANHOU\033[m eu escolhi \033[1;33m{sorteio}\033[m")
