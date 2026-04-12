import func
import tratamento

j = float(input("Digite um número: "))
print(f"A raiz quadrada de {j} é {func.raizQuadrada(j)}")
print(
    f"A raiz quadrada de {tratamento.trata(j)} é {tratamento.trata(func.raizQuadrada(j))}"
)
