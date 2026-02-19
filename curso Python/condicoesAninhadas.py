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
validacao = anoAtual - nasc
if validacao < 18:
    print(f"Você ainda não precisa se alistar pois vc tem {validacao} anos")
elif validacao == 18:
    print(f"Você precisa se alistar pois vc tem {validacao} anos")
else:
    print(f"Você já passou da época de alistar pois vc tem {validacao} anos")
