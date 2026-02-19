# Fatiamento
frase = "Curso em Vídeo Python"
print(frase)
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise
frase = "Curso em Vídeo Python"
print(len(frase))  # tamanho da frase
print(frase.count("o"))  # contar quantos o tem na frase
print(frase.count("o", 0, 13))  # contar quantos da posição  0 a 12
print(frase.find("deo"))  # onde começa o DEO
print(frase.find("Android"))  # vai retornar -1 pq não encontrou
print("Curso" in frase)  # perguntando se tem a palavra Curso em frase

# transformação
frase = "Curso em Vídeo Python"
print(frase.replace("Python", "Android"))  # substitui a palavra python por android
print(frase.upper())  # tudo maisculo
print(frase.lower())  # tudo minusculo
print(frase.capitalize())  # só a primeira letra em maiscula
print(frase.title())  # primeira letra de cada paravra em maiuscula

# transformação 2
frase = "   Aprenda Python  "
print(len(frase))
print(frase.strip())  # tira todos os espaços antes e depois da frase
print(frase.rstrip())  # tira os espaços a direita da frase
print(frase.lstrip())  # tira os espaços a esquerda da frase

# transformação 3

frase = "Curso em Vídeo Python"
print(frase.split())  # divide a frase e a cada palavra coloca separado em uma lista
print(frase.split())  # divide a frase e a cada palavra coloca separado em uma lista
eu = frase.split()
print("|".join(eu))

# desafio 22
nome = str(input("Digite seu nome completo: "))
print(nome.upper())
print(nome.lower())
nome2 = nome.replace(" ", "")
print(f"O nome completo possue {len(nome2)} letras.")
nome3 = nome.split()
print(f"O primeiro nome possue {len(nome3[0])} letras")

# desafio 23
num = int(input("Digite um numero de 0 a 9999: "))
u = int(num // 1 % 10)
d = int(num // 10 % 10)
c = int(num // 100 % 10)
m = int(num // 1000 % 10)

print(f"Unidade = {u}")
print(f"Dezena  = {d}")
print(f"Centena = {c}")
print(f"Milhar  = {m}")


# desafio 23
continuar = True
while True:
    print("\nPara sair aperte ENTER sem digitar nada!!\n")
    num = input("Digite um numero entre 0 e 9999: ")
    texto = str(num)

    if len(texto) == 4:
        print(
            f"""
            unidade: {texto[3]}
            dezena:  {texto[2]}
            centena: {texto[1]}
            milhar:  {texto[0]}
            """
        )

    elif len(texto) == 3:
        print(
            f"""
            unidade: {texto[2]}
            dezena:  {texto[1]}
            centena: {texto[0]}
            """
        )

    elif len(texto) == 2:
        print(
            f"""
            unidade: {texto[1]}
            dezena:  {texto[0]}
            """
        )

    elif len(texto) == 1:
        print(
            f"""
            unidade: {texto[0]}
            """
        )

    elif len(texto) == 0:
        continuar = False
        print("\n\nSaindo do sistema...\n\n")
        break

    else:
        print("\n##### O número digitado é maior que 9999! #### \n")


# exercico 24

cid = str(input("Digite o nome de uma cidade... ")).lower().strip()
cid2 = cid.split()
ver = "santo" in cid2[0]
if ver == True:
    print(f"A cidade de {cid.capitalize()} começa com a palavra 'Santo'")
else:
    print(f"A cidade {cid.capitalize()} não começa com palavra Santo")

    # exercico 24

cid = str(input("Digite o nome de uma cidade... ")).lower().strip().split()

ver = "santo" in cid[0]
if ver == True:
    print(f"A cidade de {cid[0]} começa com a palavra 'Santo'")
else:
    print(f"A cidade {cid[0]} não começa com palavra Santo")


cid = str(input("Digite o nome de uma cidade... ")).lower().strip().split()
ver = cid[0] == "santo"

# exercico 25

nome = str(input("Digite um nome: ")).lower()
cond = "silva" in nome
if cond == True:
    print(f'Sim no nome {nome.capitalize()} contém "Silva" no nome')
else:
    print(f'O nome {nome.capitalize()} não conté "Silva" no nome')

# exercico 25

nome = str(input("Digite um nome: ")).lower()

print(f"Seu nome tem silva? {'silva' in nome}")


# exercico 26

frase = str(input("Digite uma frase... ")).lower()
cont = frase.count("a")
pos = frase.find("a")
pos2 = frase.rfind("a")
print(f'Na frase {frase} contém {cont} vez(es) a vogal "a"')
print(f'A primeira vogal "a" está na posição {pos}')
print(f'A última vogal "a" se encontra na posição {pos2}')

# exercico 26

frase = str(input("Digite uma frase... ")).lower().strip()
print(f'Na frase {frase} contém {frase.count("a")} vez(es) a vogal "a"')
print(f'A primeira vogal "a" está na posição {frase.find("a")+1}')
print(f'A última vogal "a" se encontra na posição {frase.rfind("a")+1}')


# exercicio 27
nome = str(input("Digite um nome completo: "))
divi = nome.split()
print(f"O primeiro nome é {divi[0]}")
print(f"E o último nome é {divi[-1]}")
