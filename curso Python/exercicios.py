c = (
    "\033[m",
    "\033[0;30;41m ",
    "\033[0;30;42m ",
    "\033[0;30;43m ",
    "\033[0;30;44m ",
    "\033[0;30;45m ",
    "\033[7;30m ",
)
# cor 0  # cor1 vermelho

print(c)


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[6], end="")
    help(com)
    print(c[0])


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end="")


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.lower() == "fim":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)
