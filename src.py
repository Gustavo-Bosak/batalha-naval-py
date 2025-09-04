'''
1. Função para exibir menu principal:
    - imprimir opções
    - capturar resposta do usuário
    - validar se a resposta está dentro do esperado
    - levar para a opção selecionada

2. Função para posicionar barcos:
    - exibir tabuleiro vazio
    - capturar posição e tamanho do barco com base em coordenadas (exemplo A2 e B2)
    - posicionar na lista os barcos, trocando o emoji de onda pelo emoji de barco
    - verificar se todos os barcos foram posicionados, e então passar a vez através da função alternar jogadores
    - validar se não há sobreposição
    - validar se a posição existe no tabuleiro
    - validar se não atingiu o limite de barcos (1 de 4 casas, 2 de cada 3, 2 e 1 casa)

3. Função para sortear jogador:
    - gerar número aleatório para cada jogador e calcular qual é o maior, para decidir quem joga primeiro

4. Função para alternar a vez entre os jogadores:
    - trocar lista (tabuleiro) exibida para ser manipulada

5. Função para capturar jogada:
    - verificar qual jogador está jogando
    - capturar posição da bomba
    - validar se a posição existe no tabuleiro
    - registrar jogada na lista, trocando o emoji de onda pelo emoji de bomba respectivo ao erro ou acerto
    - retornar se acertou ou não

6. Função para exibir o tabuleiro
    - imprimir o tabuleiro atualizado do respectivo jogador

7. Função para verificar vitória:
    - verificar se todos os barcos foram destruidos
    - imprimir condição de vitória

8. Função principal
    - rodar em loop com condição de querer continuar jogando ou não
    - resetar tabuleiros e  chamar função menu dentro do loop

9. Função para modo vs computador:
    - gerar um valor aleatório para ser usado no posicionamento de barcos
    - checar lista de acertos e erros para se basear na escolha do valor aleatório, priorizando valores próximos ao acerto

'''

import random
import time
import os

# Definição inicial e global dos tabuleiros
tabuleiros = []
for i in range(0,2):
    tabuleiro = []
    for _ in range(8):
        novaLinha = []
        for _ in range(8):
            novaLinha.append('🌊')
        tabuleiro.append(novaLinha)
    tabuleiros.append(tabuleiro)

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

    limparTerminal()
    exibirTabuleiro(0, primeiroAJogar)

def exibirTabuleiro(numeroTabuleiro, jogadorDaVez):
    limparTerminal()
    print('---------------------------------------------')
    print(f'------------------{jogadorDaVez.upper()}------------------')
    print('---------------------------------------------\n')

    print(' A   B    C    D    E    F    G    H')
    print('_______________________________________')
    for i in range(8):
            linha_formatada = ''
            for j in range(8):
                linha_formatada += tabuleiros[numeroTabuleiro][i][j] + ' | '
            print(linha_formatada + f'{i+1}')
    print('_______________________________________\n')

def posicionarBarcos(posicao):
    limparTerminal()

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


#FERRETE
def tiroAleatorio():
    """Gera coordenadas de um tiro aleatório no tabuleiro."""
    linha = random.randint(0, 7)
    coluna = random.randint(0, 7)
    return (linha, coluna)

def maquina(jogadas_certas, jogadas_erradas):
    """
    Decide onde a máquina deve atirar com base nas jogadas anteriores.
    
    Args:
        tabuleiro_adversario (list): O tabuleiro do jogador a ser atacado.
        jogadas_certas (list): Lista de coordenadas onde a máquina acertou.
        jogadas_erradas (list): Lista de coordenadas onde a máquina errou.
        
    Returns:
        tuple: As coordenadas (linha, coluna) do tiro.
    """
    tiro = None
    # Lógica de 'caçar' o barco: se houver acertos anteriores não afundados
    if jogadas_certas:
        # Pega a última jogada certa para tentar atirar ao redor
        ultima_jogada = jogadas_certas[-1]
        opcoes_de_tiro = [
            (ultima_jogada[0] - 1, ultima_jogada[1]), # Acima
            (ultima_jogada[0] + 1, ultima_jogada[1]), # Abaixo
            (ultima_jogada[0], ultima_jogada[1] - 1), # Esquerda
            (ultima_jogada[0], ultima_jogada[1] + 1)  # Direita
        ]
        
        # Filtra as opções para garantir que estão dentro do tabuleiro e ainda não foram tentadas
        tiros_validos = [
            op for op in opcoes_de_tiro 
            if 0 <= op[0] <= 7 and 0 <= op[1] <= 7 and op not in jogadas_certas and op not in jogadas_erradas
        ]

        '''
        for op in opcoes_de_tiro:
            if 0 <= op[0] <= 7 and 0 <= op[1] <= 7 and op not in jogadas_certas and op not in jogadas_erradas:
                tiros_validos.append(op)
        '''
        if tiros_validos:
            tiro = random.choice(tiros_validos)
    
    # Se não houver acertos ou se a lógica de 'caça' não encontrar um tiro válido
    if not tiro:
        tiro = tiroAleatorio()
        while tiro in jogadas_certas or tiro in jogadas_erradas:
            tiro = tiroAleatorio()
            
    return tiro

def alternarJogador():
    """Alterna o turno entre os jogadores."""
    # Sua lógica para alternar jogadores viria aqui

def validaJogada(coordenadas, tabuleiro):
    """
    Valida a jogada em um tabuleiro e retorna o resultado.
    
    Args:
        coordenadas (tuple): As coordenadas (linha, coluna) do tiro.
        tabuleiro (list): O tabuleiro a ser verificado.
        
    Returns:
        str: O resultado do tiro ("Acertou", "Errou" ou "Barco Destruído").
    """
    # Exemplo de lógica simples de validação
    linha, coluna = coordenadas
    if tabuleiro[linha][coluna] == '⛵': # Supondo que '⛵' representa um barco
        return "Acertou"
    elif tabuleiro[linha][coluna] == '🌊': # Supondo que '🌊' representa a água
        return "Errou"
    else:
        return "Errou" # Ou outra validação, se o espaço já foi atingido

def main():
    while True:
        # Resetar tabuleiro
        for i in range(0,2):
            tabuleiros[i] = []

            for _ in range(8):
                novaLinha = []
                for _ in range(8):
                    novaLinha.append('🌊')
                tabuleiros[i].append(novaLinha)
            
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