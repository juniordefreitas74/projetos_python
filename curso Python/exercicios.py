# ex 58
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
        adic = int(input("Qual número deseja adicionar: "))
        numero.append(adic)
        print(numero)
    elif menu == 5:
        ok = False
    else:
        print("\033[1;41mDigite uma opção válida!!\033[m")
print("fim")
