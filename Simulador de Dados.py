# Simulador de dados
# Simular valor de dado aleatoriamente para 4 jogadores, valor de 1 até 6
# Verificar a ordem do maior para o menor do sorteio dos dados

from random import randint
jogo = { 'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}

print(jogo)