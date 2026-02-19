# exercicio 39
import datetime

nasc = int(input("Digite o ano do seu nascimento:"))
anoAtual = datetime.date.today().year
validacao = anoAtual - nasc
if validacao < 18:
    print(f"Você ainda não precisa se alistar pois vc tem {validacao} anos")
elif validacao == 18:
    print(f"Você precisa se alistar pois vc tem {validacao} anos")
else:
    print(f"Você já passou da época de alistar pois vc tem {validacao} anos")
