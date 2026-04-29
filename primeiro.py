import random
import os

input("\033[93mPressione Enter para começar o jogo...\033[0m")

pontuacao = 0
maquina = 0
primeiro = True
while True:
    print("\033[92mjogo de adivinhação\033[0m 🎮")
    if primeiro:
        print("\033[96m♦ Pontuação:\033[0m")
        print("\033[96m♦ 1 tentativa = 3 pontos\033[0m")
        print("\033[96m♦ 2 tentativas = 2 pontos\033[0m")
        print("\033[96m♦ 3 tentativas = 1 ponto\033[0m")
        print("\033[96m♦ derrota = 0 pontos\033[0m")
        print("\033[96m♦ se você perder, a máquina ganha 3 pontos\033[0m")
        print("\033[96m♦ primeiro a 10 pontos reseta o placar\033[0m")
        primeiro = False
    numero_secreto = random.randint(1, 10)
    print("\033[94m tente adivinhar o número secreto entre 1 e 10\033[0m 🕵️")
    for tentativa_num in range(1, 4):
        print(f"\033[93mtentativa:{tentativa_num}/3 \033[0m", end="")
        tentativa = int(input())
        if tentativa == numero_secreto:
            print("\033[93mparabéns você acertou\033[0m 🏆")
            pontos = 4 - tentativa_num
            pontuacao += pontos
            print(f"\033[95mVocê ganhou {pontos} pontos! Pontuação total: {pontuacao}\033[0m")
            print(f"\033[91mPontuação da máquina: {maquina}\033[0m")
            if pontuacao >= 10:
                print("\033[92mvitória!!! 🏆\033[0m")
                pontuacao = 0
                maquina = 0
            elif maquina >= 10:
                print("\033[91mvocê perdeu 💀\033[0m")
                pontuacao = 0
                maquina = 0
            break
        elif tentativa < numero_secreto:
            print("\033[96mo número é maior! ⬆️\033[0m")
        else:
            print("\033[96mo número é menor! ⬇️\033[0m")
    else:
        print("\033[91mGAME OVER\033[0m 💀 \033[94mo número secreto era " + str(numero_secreto) + "\033[0m")
        print(f"\033[95mVocê ganhou 0 pontos. Pontuação total: {pontuacao}\033[0m")
        maquina += 3
        print(f"\033[91mPontuação da máquina: {maquina}\033[0m")
        if maquina >= 10:
            print("\033[91mvocê perdeu 💀\033[0m")
            pontuacao = 0
            maquina = 0
    print("\033[93mdeseja jogar novamente? (s/n) \033[0m", end="")
    reapostar = input().strip().lower()
    if reapostar == 's':
        pass
    else:
        print("\033[92mobrigado por jogar!\033[0m 👋")
        break


