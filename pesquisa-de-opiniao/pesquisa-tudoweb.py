# Pesquisa de Opinião TudoWeb
# O programa realiza uma pesquisa com 50 entrevistados
# e conta as respostas EXCELENTE e RUIM.

# Variáveis para contar as respostas
excelente = 0
ruim = 0

# Repetição para realizar a pesquisa com 50 entrevistados
for i in range(50):

    # Solicita os dados do entrevistado
    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade do entrevistado: "))

    # Solicita a opinião sobre o atendimento
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção escolhida: "))

    # Verifica a opinião escolhida
    if opiniao == 1:
        excelente = excelente + 1
        print("Resposta registrada: EXCELENTE")

    elif opiniao == 2:
        print("Resposta registrada: BOM")

    elif opiniao == 3:
        ruim = ruim + 1
        print("Resposta registrada: RUIM")

    else:
        print("Opção inválida.")

    print("--------------------------------")

# Exibe o resultado final da pesquisa
print("RESULTADO DA PESQUISA")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
