#Pedra -> tesoura
#Papel -> Pedra
#Tesoura -> Papel
#os.system('cls')


import os

while True:
    print("======= Pedra, Papel ou Tesoura =======")
    print("Para escolheres escreve:\n- Papel \n- Tesoura \n- Pedra \n- 4 - para sair")

    jogador1 = input("jogador 1 - Escolha entre Pedra, papel ou tesoura: ").lower()
    if jogador1 == "4":
        print("Jogador 1 saiu")
        break

    os.system('cls')

    jogador2 = input("jogador 2 - Escolha entre Pedra, papel ou tesoura: ").lower()
    if jogador2 == "4":
        print("Jogador 2 saiu")
        break
    os.system('cls')


    match (jogador1, jogador2):
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            print("O jogador 1 ganhou")
        case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
            print("O jogador 2 ganhou")
        case ("pedra", "pedra") | ("tesoura", "tesoura") | ("papel", "papel"):
            print("Empate")
        case _:
            print("Resposta errada")

    resposta = input("Quer jogar novamente? (s/n): ").lower()
    if resposta != 's':
        print("Jogo terminado")
        break

            
