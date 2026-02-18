numero = int(input("digite um numero inteiro: "))
suss = numero + 1
ante = numero - 1
print(f"O numero digitado é {numero} seu sucessor é {suss} e seu antecessor é {ante}.")
print(
    f"O numero digitado é {numero} seu sucessor é {numero+1} e seu antecessor é {numero-1}."
)
print("\n", ">" * 50, "\n")

#########################

num = int(input("digite um numero inteiro: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1 / 2)
print(f"numero digitado {num} dobro {dobro} triplo {triplo} raiz {raiz:.2f}")
print(
    f"numero digitado {num} dobro {num*2} triplo {num*3} raiz {num**(1/2):.2f} ou {pow(num,1/2)}"
)

print("\n", ">" * 50, "\n")

#########################
n1 = float(input("digite a nota 1: "))
n2 = float(input("digite a nota 2: "))
som = (n1 + n2) / 2
print(f" nota 1 {n1} nota 2 {n2} média {som}")
print(f"1ª nota {n1} 2ª nota {n2} a média do aluno é {(n1+n2)/2:.1f}")

print("\n", ">" * 50, "\n")

#########################

metros = float(input("Digite quantos metros quer converter: "))
cm = metros * 100
mm = metros * 1000
print(f"{metros} metros é o mesmo que \n{cm} centímetros \n{mm} milímetros.")
print(
    f"{metros} metros é o mesmo que\n {metros*100:.0f} centimetros\n {metros/1000:.2f} kilometro(s)"
)
print("\n", ">" * 50, "\n")

########################

tabuada = int(input("Qual tabuada deseja: "))
print("-" * 12)
for resultado in range(1, 11):
    conta = resultado * tabuada
    print(f"{tabuada} x {resultado:2} = {conta:2}")
print("-" * 12)


print("\n", ">" * 50, "\n")

########################

carteira = float(input("Quanto dinheiro vc tem? R$"))
dolar = 3.27
print(f"Você tem R${carteira:.2f}  vc consegue comprar US${carteira/dolar:.2f}")

print("\n", ">" * 50, "\n")

########################

altura = float(input(" qual altura da parede? "))
largura = float(input(" qual largura da parede? "))
area = altura * largura
tinta = area / 2
print(
    f"Altura {altura} metros x Largura {largura} metros = área de {area:.2f} m2 precisamos de {tinta:.2f} litros de tinta para pintar essa área."
)

print("\n", ">" * 50, "\n")

########################

preco = float(input("Digite o valor da venda: R$"))
desconto = preco * 0.95
porcentagem = preco - desconto
print(
    f"Preço normal R${preco:.2f} e com 5%  equivalente a R${porcentagem:.2f} de desconto ficou R${desconto:.2f}"
)

print("\n", ">" * 50, "\n")

########################

salario = float(input("Digite seu salário: R$"))
aumento = float(input("digite o aumento "))
final = salario * (aumento / 100)

print(
    f"O salário de R${salario:.2f} teve um aumento de {aumento}% e o novo salário será R${salario + final:.2f}"
)

print("\n", ">" * 50, "\n")

########################
temperatura = float(input("Informe a temperatura em ºC: "))
f = temperatura * 1.8 + 32

print(f"a temperatura de {temperatura}ºC equivale a {f:.1f}ºF")

print("\n", ">" * 50, "\n")

########################
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM rodados? "))
valor_diaria = (dias * 60) + (0.15 * km)
print(f"O total a pagar é de R${valor_diaria:.2f}")
