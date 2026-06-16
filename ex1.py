total_de_partidas = 0
total_de_pontos = 0
melhor_pontuacao = 0

jogar = "SIM"

while jogar.upper() == "SIM":
    pontos = 0
    total_de_partidas = total_de_partidas + 1

    print("\nNova Partida:")

    for i in range(1, 6):

        if i == 1:
            resposta = input(
                "\n1) Qual a capital do Brasil?\nA) Rio de Janeiro\nB) Brasília\nC) São Paulo\nResposta: "
            ).upper()

            if resposta == "B":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (B).")

        elif i == 2:
            resposta = input(
                "\n2) Quanto é 5 x 4?\nA) 20\nB) 25\nC) 15\nResposta: "
            ).upper()

            if resposta == "A":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (A).")

        elif i == 3:
            resposta = input(
                "\n3) Qual linguagem estamos estudando?\nA) Java\nB) C++\nC) Python\nResposta: "
            ).upper()

            if resposta == "C":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (C).")

        elif i == 4:
            resposta = input(
                "\n4) Qual planeta é conhecido como planeta vermelho?\nA) Marte\nB) Terra\nC) Júpiter\nResposta: "
            ).upper()

            if resposta == "A":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (A).")

        elif i == 5:
            resposta = input(
                "\n5) Quantos dias tem uma semana?\nA) 5\nB) 6\nC) 7\nResposta: "
            ).upper()

            if resposta == "C":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (C).")

    print("\nVocê fez", pontos, "ponto(s) de 5.")

    total_de_pontos = total_de_pontos + pontos

    if pontos > melhor_pontuacao:
        melhor_pontuacao = pontos

    jogar = input("\nDeseja jogar novamente? (sim/não): ")

media = total_de_pontos / total_de_partidas

print("\nResumo da Parida")
print("Partidas jogadas:", total_de_partidas)
print("Total de pontos:", total_de_pontos)
print("Melhor pontuação:", melhor_pontuacao)
print("Média de pontos:", media)