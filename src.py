'''
1. Função para exibir menu principal:
    - imprimir opções
    - capturar resposta do usuário
    - validar se a resposta está dentro do esperado
    - levar para a opção selecionada

2. Função para posicionar barcos:
    - exibir tabuleiro vazio
    - capturar posição e tamanho do barco com base em coordenadas (exemplo A2 e B2)
    - posicionar na lista os barcos
    - verificar se todos os barcos foram posicionados, e então passar a vez
    - validar se não há sobreposição
    - validar se a posição existe no tabuleiro

3. Função para sortear jogador:
    - gerar número aleatório para cada jogador e calcular qual é o maior, para decidir quem joga primeiro

4. Função para alternar a vez entre os jogadores:
    - trocar lista (tabuleiro) exibida para ser manipulada

5. Função para capturar jogada:
    - verificar qual jogador está jogando
    - capturar posição da bomba
    - retornar se acertou ou não
    - validar se a posição existe no tabuleiro

6. Função para atualizar o tabuleiro
    - imprimir o tabuleiro atualizado do respectivo jogador
    - chamar a função capturar jogada

7. Função para verificar vitória:
    - verificar se todos os barcos foram destruidos
    - imprimir condição de vitória

8. Função principal

9. Função para modo vs computador:
    - chamar posicionar barcos
    - 

'''

import random
import time
import os

# Função para limpar o terminal (variação para Windows e macOS)
def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else :
        os.system('clear')

def sortearJogadores(modoDeJogo):
    limparTerminal()
    print(f'Sorteando os jogadores', end='')
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    print('.')
    time.sleep(0.3)
    
    print('---------------------------------------------\n')
    
    if modoDeJogo == 1:
        jogador2 = 'Jogador 2'
    elif modoDeJogo == 2:
        jogador2 = 'Computador'

    primeiroAJogar = random.choice(['Jogador 1', jogador2])
    print(f'Quem joga primeiro é o {primeiroAJogar}!')
    
    input('\nAperte ⏎ Enter para começar.')

def menu():
    limparTerminal()
    print('---------------------------------------------')
    print('----------------BATALHA NAVAL----------------')
    print('---------------------------------------------\n')
    print('Escolha uma das opções: \n1. Jogar contra amigos\n2. Jogar contra a máquina\n3. Regras')

    # Validação de entrada para menu
    while True:
        try:
            resposta = int(input('\nR: '))

            if resposta >= 1 and resposta <= 3:
                break
            else:
                print('Digite apenas números entre 1 e 3.')
                
        except ValueError:
            print('Digite apenas números inteiros')
    
    match resposta:
        case 1:
            sortearJogadores(resposta)
        case 2:
            sortearJogadores(resposta)
        case _:
            limparTerminal()
            print('regras')

def main():
    while True:
        menu()
        print('\n\n---------------------------------------------')
        print('-----------------FIM DE JOGO-----------------')
        print('---------------------------------------------\n')
        print('Quer jogar novamente? Responda apenas "sim" ou "não"')
        entrada = input('R: ')
        confirmacao = entrada.lower().strip()

        if confirmacao == 'sim':
            continue
        elif confirmacao == 'não' or confirmacao == 'nao':
            break
        
        else:
            print('\nResposta não esperada.')
            entrada = input('R: ')

main()

tabuleiros = [
    [
        ['A1', 'B1', 'C1', 'D1', 'E1', 'F1',],
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2',],
        ['A3', 'B3', 'C3', 'D3', 'E3', 'F3',],
        ['A4', 'B4', 'C4', 'D4', 'E4', 'F4',],
        ['A5', 'B5', 'C5', 'D5', 'E5', 'F5',],
        ['A6', 'B6', 'C6', 'D6', 'E6', 'F6'] 
    ],
    [
        ['A1', 'B1', 'C1', 'D1', 'E1', 'F1',],
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2',],
        ['A3', 'B3', 'C3', 'D3', 'E3', 'F3',],
        ['A4', 'B4', 'C4', 'D4', 'E4', 'F4',],
        ['A5', 'B5', 'C5', 'D5', 'E5', 'F5',],
        ['A6', 'B6', 'C6', 'D6', 'E6', 'F6'] 
    ],
]


# limparTerminal()
print('---------------------------------------------')
print('------------------TABULEIRO------------------')
print('---------------------------------------------\n')
print(
    '\n  A   B     C    D    E    F    G    H\n'
    '_______________________________________\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 1\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 2\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 3\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 4\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 5\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 6\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 7\n'
    '🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 🌊 | 8\n'
    '_______________________________________\n'
)


'''
matriz = [
    [0, 0 , 0],
    [0, 0 , 0],
    [1, 0 , 2],
    [3, 0 , 4],
]

linhasNulas = 0
colunasNulas = 0

for i in range(4):
    itemNuloLinha = 0
    itemNuloColuna = 0

    for j in range(3):
        if matriz[i][j] == 0:
            itemNuloLinha += 1

    if itemNuloLinha == 3:
        linhasNulas+= 1

for i in range(3):
    itemNuloLinha = 0
    itemNuloColuna = 0
    for j in range(4):
        
        if matriz[j][i] == 0:
            itemNuloColuna += 1
    
    if itemNuloColuna == 4:
        colunasNulas+= 1

print(f'Número de linhas nulas: {linhasNulas} | Número de colunas nulas: {colunasNulas}')
'''