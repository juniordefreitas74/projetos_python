# exercicio 45
import random
import time

print(
    """ Vamos jogar Jokenpô!
      ======> Escolha <=====
      1- Para PEDRA
      2- Para PAPEL
      3- Para TESOURA
      """
)
jogador = int(input("Digite a sua escolha: "))
escolha = ["PEDRA", "PAPEL", "TESOURA"]
sorteio = random.choice(escolha)
print(f"{"JO":.<6}")
time.sleep(1)
print(f"{"KEN":.^6}")
time.sleep(1)
print(f"{"PO!":.>6}")
time.sleep(0.3)
sorteio = "PAPEL"

if sorteio == "PEDRA":
    if jogador == 1:
        print(f"\033[43m EMPATOU \033[m")
        jogador = "PEDRA"

    elif jogador == 2:
        print(f"\033[42m VOCÊ GANHOU \033[m")
        jogador = "PAPEL"

    elif jogador == 3:
        print(f"\033[41m VOCÊ PERDEU! \033[m")
        jogador = "TESOURA"

    else:
        print("JOGADA INVÁLIDA!")


if sorteio == "PAPEL":
    if jogador == 2:
        print(f"\033[43m EMPATOU \033[m")
        jogador = "PAPEL"

    elif jogador == 3:
        print(f"\033[42m VOCÊ GANHOU \033[m")
        jogador = "TESOURA"

    elif jogador == 1:
        print(f"\033[41m VOCÊ PERDEU! \033[m")
        jogador = "PEDRA"

    else:
        print("\033[35m JOGADA INVÁLIDA! \033[m")
        sorteio = "nenhuma opção"
        jogador = "OPÇAO ERRADA"

print(f"Você escolheu {jogador} e o computador escolheu {sorteio}!")
