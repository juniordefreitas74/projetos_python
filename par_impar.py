

print('Exercício 1 — Saudação inteligente\n')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade = int(idade)
idade_futura = idade + 10
print(f'Olá {nome}, você tem {idade} anos e em 10 anos terá {idade_futura}! ')

print('\nExercício 2 — Par ou Ímpar\n')

numero_digitado = int(input('Digite um número inteiro: '))
numero = numero_digitado % 2
if numero == 0:
    print('Seu número é Par')


else:
    print('Seu número é impar')
