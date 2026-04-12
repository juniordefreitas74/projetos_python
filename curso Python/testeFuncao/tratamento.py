def trata(num=0, cifra="R$"):
    return f"{cifra}{num:.2f}".replace(".", ",")
