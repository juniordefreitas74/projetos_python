# exe 74
import random

cont = 0
tupla = ()
num = ()
while True:
    gera = random.randint(0, 20)
    num2 = (gera,)
    num = num + num2

    # teste = num + tupla
    cont += 1

    if cont == 5:
        break
    ordem = sorted(num)

print(num)
print(f" O maior número é o {ordem[-1]}")
print(f"O menor número é o {ordem[0]}")
