from time import sleep
import random


print ("Suas opções:")
print ("[ 0 ] Pedra")
print ("[ 1 ] Papel")
print ("[ 2 ] Tesoura")
jogada = int ( input("Qual a sua jogada: "))
sleep(1)

print("Jan")
sleep(1)
print("Ken")
sleep(1)
print("Pôn")
sleep(1)

opcoes = ("Pedra" , "Papel" , "Tesoura")
computador = random.randint(0, 2)

print("==" * 10)

print(f"\nO jogador escolheu a opção: {opcoes[jogada]}")
print(f"\nO computador escolheu a opção: {opcoes[computador]}.")
print("-=" * 10)

if computador == 0:

    
    if jogada == 0:
        print ("A rodada deu: EMPATE")

    elif jogada == 1:
        print ("A jogada deu: DERROTA")

    elif jogada == 2:
        print ("A rodada deu: VITORIA")

    else:
        print("Rodada inválida.")

elif computador == 1:

    if jogada == 0:
        print("A rodada deu: DERROTA")

    elif jogada == 1:
        print("A rodada deu: EMPATE")

    elif jogada == 2:
        print("A jogada deu: VITORIA")
    
    else:
        print("Rodada inválida")

elif computador == 2:

    if jogada == 0:
        print("A rodada deu: VITORIA")

    elif jogada == 1:
        print("A rodada deu: DERROTA")

    elif jogada == 2:
        print("A rodada deu: EMPATE")

    else:
        print("Rodada inválida")
