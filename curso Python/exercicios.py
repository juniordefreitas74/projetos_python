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
