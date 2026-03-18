# exe 75
cont = 0
tupla = ()
pares = []
while cont < 4:
    num = int(input("Digite um número: "))
    tupla += (num,)
    cont += 1
    if num % 2 == 0:
        pares += (num,)

num9 = tupla.count(9)
if 3 in tupla:
    pos3 = tupla.index(3) + 1
else:
    pos3 = "0"


print(tupla)
print(f"O número 9 aparece {num9} vezes.")
print(f"O número 3 apareceu na posição {pos3}")
print(f"Os números pares digitados foram {' '.join(map(str,pares))}")
