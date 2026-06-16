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
                "\n1) Qual o maior país do Mundo em relação a território?\nA) Brasil\nB) Rússia\nC) Estados Unidos\nResposta: "
            ).upper()

            if resposta == "B":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (B).")

        elif i == 2:
            resposta = input(
                "\n2) Quanto é 60*3?\nA) 180\nB) 120\nC) 150\nResposta: "
            ).upper()

            if resposta == "A":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (A).")

        elif i == 3:
            resposta = input(
                "\n3) Quantos dias tem 1 ano?\nA) 360\nB) 367\nC) 365\nResposta: "
            ).upper()

            if resposta == "C":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (C).")

        elif i == 4:
            resposta = input(
                "\n4) Qual é o maior Planeta do Sistema Solar?\nA) Júpiter\nB) Marte\nC) Vênus\nResposta: "
            ).upper()

            if resposta == "A":
                print("\nParabéns!! Você acertou essa questão.")
                pontos = pontos + 1
            else:
                print("\nResposta incorreta! A alternativa correta era a (A).")

        elif i == 5:
            resposta = input(
                "\n5) Qual é o maior artilheiro da seleção portuguesa?\nA) Pauleta\nB)  Eusébio\nC) Cristiano Ronaldo\nResposta: "
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