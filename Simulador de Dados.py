# Simulador de dados
# Simular valor de dado aleatoriamente para 4 jogadores, valor de 1 até 6
# Verificar a ordem do maior para o menor do sorteio dos dados

from random import randint
from time import  sleep
from operator import itemgetter
jogo = { 'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('¨¨' * 30)
print('-- Ranking dos jogadores --')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirando {v[1]} no dado.')
    sleep(1)