# ex 57
p = True
while p == True:
    sexo = input("Digite o sexo [F/M]: ").lower()
    if sexo != "m" and sexo != "f":
        print("Digite a opção correta.")
    else:
        p = False
print("fim")

# ex 58
import random

tentativas = 0
acerto = True
pc = random.randint(0, 10)
while acerto == True:
    numero = int(input("Adivinhe o número estou pensando de 1 a 10:"))
    tentativas += 1
    if numero == pc:
        print(
            f"\033[31mParabéns\033[m você acertou em \033[32m{tentativas}\033[m tentaivas!"
        )
        acerto = False
    else:
        print("Não foi esse número que eu pensei, tente novamente!")
