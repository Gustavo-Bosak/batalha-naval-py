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
    
    
#função para alterar jogadores
def alternarJogador(jogadorAtual):      #Verifica se o jogador atual é 0 (Jogador 1), se sim retorna 1 (Jogador 2), se não retorna 0 (Jogador 1)
    if jogadorAtual == 0:
        return 1
    else: 0                     
    
#função para capturar jogada  
def capturarJogada(jogadorAtual):       #recebe o jogador atual (0 ou 1) como parâmetro
    if jogadorAtual == 0:               #verifica se o jogador atual é 0 (Jogador 1), se sim o inimigo é 1 (Jogador 2)
        inimigo = 1
    else: 0

    # Dicionário mapeando as letras das colunas para os índices
    colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    while True:
        entrada = input(f"🎯 Jogador {jogadorAtual + 1}, escolha uma posição para atacar (ex: B4): ").strip().upper()

        # Valida o formato da entrada (letra + número)
        if len(entrada) < 2 or len(entrada) > 3:
            print("❌ Formato inválido. Tente novamente.")
            continue

        letra = entrada[0]      #Pega a primeira letra da entrada
        numero = entrada[1:]    #Pega o número 

        # Verifica se a letra está contida no dicionário
        if letra not in colunas:
            print("❌ Letra inválida. Tente novamente.")
            continue

        # Verifica se a posição existe no tabuleiro
        if not numero.isdigit() or int(numero) < 1 or int(numero) > 8:
            print("❌ Número da linha inválido. Tente novamente.")
            continue

        linha = int(numero) - 1      # Subtrai 1 para ajustar o índice(0 a 7)
        coluna = colunas[letra]      # Usando o dicionário para pegar o índice da coluna

        # Verifica se a posição foi atacada antes (com base nos símbolos)
        simboloAtual = tabuleiros[inimigo][linha][coluna]

        if simboloAtual in ['🔥', '💣']:
            print("⛔ Você já jogou nessa posição. Escolha outra.")
            continue

        # Verifica se acertou o barco ou errou
        if simboloAtual == '🚢':
            tabuleiros[inimigo][linha][coluna] = '🔥'
            print("🔥 ACERTOU!")
            return True
        else:
            tabuleiros[inimigo][linha][coluna] = '💣'
            print("💣 ERROU!")
            return False


#função para exibir tabuleiro
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