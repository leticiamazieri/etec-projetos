def main():
    aparelho = input("Nome do aparelho: ")
    potencia = float(input("Potência do aparelho em watts (W): "))
    horasDia = float(input("Tempo médio de uso diário (horas): "))

    consumoMensal = (potencia * horasDia * 30) / 1000
    tarifaFixa = 0.75
    custoEstimado = consumoMensal * tarifaFixa

    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumoMensal} kWh/mês")
    print(f"Custo estimado (considerando tarifa de R$0,75/kWh): R$ {custoEstimado} por mês")


if __name__ == "__main__":
    main()