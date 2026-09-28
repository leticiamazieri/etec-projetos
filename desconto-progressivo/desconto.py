# Este programa calcula o desconto de acordo com o
# valor total da compra.

# Solicita ao usuário o valor total da compra
valor = float(input("Digite o valor total da compra: R$ "))

# Verifica qual desconto deve ser aplicado
if valor < 200:
    desconto = valor * 0.05
    print("Desconto de 5% aplicado.")

elif valor < 300:
    desconto = valor * 0.10
    print("Desconto de 10% aplicado.")

else:
    desconto = valor * 0.15
    print("Desconto de 15% aplicado.")

# Calcula o valor que será pago após o desconto
total = valor - desconto

# Exibe os resultados
print("--------------------------------")
print("Valor da compra: R$", valor)
print("Valor do desconto: R$", desconto)
print("Valor total a pagar: R$", total)
print("--------------------------------")
