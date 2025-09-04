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

# Inicialização das listas
tabuleiros = []
jogadas_certas = []
jogadas_erradas = []
quantTotalBarcos = [7, 7] # 1 barco de 4x1, 2 barcos para cada tamanho 3x1, 2x1 e 1x1, totalizando 7

def criarNovosTabuleiros(tabuleiros, quantTotalBarcos, jogadas_certas, jogadas_erradas):
    # Redefinição da quantidade inicial de barcos
    quantTotalBarcos[0] = 1
    quantTotalBarcos[1] = 1
    jogadas_certas.clear()
    jogadas_erradas.clear()

    for _ in range(0,2):
        if len(tabuleiros) == 2:
            tabuleiros.clear()
        
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

# Função para definir o primeiro a jogar, retorna 0 ou 1
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

    if primeiroAJogar == 'Jogador 1':
        return 0
    else:
        return 1

#função para exibir tabuleiro
def exibirTabuleiro(jogadorAtual):    
    limparTerminal()
    print('---------------------------------------------')
    print(f'--------------TABULEIRO INIMIGO-------------')
    print('---------------------------------------------\n')

    print(' A   B    C    D    E    F    G    H')
    print('_______________________________________')

    for i in range(8):
            linha_formatada = ''
            for j in range(8):
                simbolo = tabuleiros[jogadorAtual][i][j]
                if simbolo in ['🔥', '💣']:
                    linha_formatada += simbolo + ' | '
                else:
                    linha_formatada += '🌊' + ' | '
            print(linha_formatada + f'{i+1}')
    print('_______________________________________\n')

#função para alterar jogadores
def alternarJogador(jogadorAtual):
    return 1 - jogadorAtual

def capturarEntrada(jogadorAtual, modoDeJogo):
    if modoDeJogo == 2 and jogadorAtual == 1:
        # Passa direto, resposta já capturada da máquina
        return maquina(jogadas_certas, jogadas_erradas)
    
    else:
        entrada = input(f"🎯 Jogador {jogadorAtual + 1}, escolha uma posição (ex: B4): ").strip().upper()
        return entrada

def validarEntrada(entrada):
    colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    
    if isinstance(entrada, tuple):
        return entrada
    
    if len(entrada) < 2 or len(entrada) > 3:
        return None
    
    letra, numero = entrada[0], entrada[1:]
    
    if letra not in colunas or not numero.isdigit():
        return None
    
    linha = int(numero) - 1
    coluna = colunas[letra]

    if 0 <= linha <= 7 and 0 <= coluna <= 7:
        return (linha, coluna)
    else:
        return None

def processarJogada(jogadorAtual, coordenadas, modoDeJogo):
    inimigo = 1 - jogadorAtual
    linha, coluna = coordenadas
    simbolo = tabuleiros[inimigo][linha][coluna]

    if simbolo in ['🔥', '💣']:
        print("⛔ Já jogou aqui.")
        input("Aperte ⏎ Enter  para continuar...")
        return 'repetida'

    if simbolo == '🚢':
        tabuleiros[inimigo][linha][coluna] = '🔥'
        quantTotalBarcos[inimigo] -= 1

        if modoDeJogo == 2 and jogadorAtual == 1:
            print("🤖 O computador jogou e ACERTOU!")
            jogadas_certas.append(coordenadas)
        else:
            print("🔥 ACERTOU!")
        return 'acerto' if quantTotalBarcos[inimigo] > 0 else 'vitoria'
    else:
        tabuleiros[inimigo][linha][coluna] = '💣'
        if modoDeJogo == 2 and jogadorAtual == 1:
            print("🤖 O computador jogou e ERROU!")
            jogadas_erradas.append(coordenadas)

        else:
            print("💣 ERROU!")
        input("\nAperte ⏎ Enter  para continuar...")
        return 'erro'

def turno(jogadorAtual, modoDeJogo):
    while True:
        if not (modoDeJogo == 2 and jogadorAtual == 1):
            exibirTabuleiro(1 - jogadorAtual)
        else:
            limparTerminal()

        entrada = capturarEntrada(jogadorAtual, modoDeJogo)
        coordenadas = validarEntrada(entrada)
        if coordenadas is None:
            print("❌ Entrada inválida.")
            input("\nAperte ⏎ Enter  para continuar...")
            continue

        resultado = processarJogada(jogadorAtual, coordenadas, modoDeJogo)
        if resultado == 'repetida':
            continue
        
        if resultado == 'vitoria':
            return 'vitoria'
        
        if resultado == 'erro':
            return 'erro'


''' comentado para testes
#função para capturar jogada
def capturarJogada(jogadorAtual):      #recebe o jogador atual (0 ou 1) como parâmetro
    inimigo = 1 - jogadorAtual
    exibirTabuleiro(inimigo)

    # bug: não ta saindo do laço quando acerta e quando a lista de barcos é esvaziada, não é erro mas precisa ajustar
    while True:
        entrada = input(f"🎯 Jogador {jogadorAtual + 1}, escolha uma posição para atacar (ex: B4): ").strip().upper()
        if validarJogada(entrada, inimigo) == False: # True or False
            return
    
def validarJogada(coordenadas, inimigo):
    # Dicionário mapeando as letras das colunas para os índices
    colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    if (type(coordenadas) == str):
        # Valida o formato da entrada (letra + número)
        if len(coordenadas) < 2 or len(coordenadas) > 3:
            print("❌ Formato inválido. Tente novamente.")
            return True

        letra = coordenadas[0]      #Pega a primeira letra da entrada
        numero = coordenadas[1:]    #Pega o número 

        # Verifica se a letra está contida no dicionário
        if letra not in colunas:
            print("❌ Letra inválida. Tente novamente.")
            return True

        # Verifica se a posição existe no tabuleiro
        if not numero.isdigit() or int(numero) < 1 or int(numero) > 8:
            print("❌ Número da linha inválido. Tente novamente.")
            return True

        linha = int(numero) - 1      # Subtrai 1 para ajustar o índice(0 a 7)
        coluna = colunas[letra]      # Usando o dicionário para pegar o índice da coluna

    # Verifica se a posição foi atacada antes (com base nos símbolos)
    simboloAtual = tabuleiros[inimigo][linha][coluna]    

    if simboloAtual in ['🔥', '💣']:
        print("⛔ Você já jogou nessa posição. Escolha outra.")
        return True

    # Verifica se acertou o barco ou errou
    if simboloAtual == '🚢':
        tabuleiros[inimigo][linha][coluna] = '🔥'
        if quantTotalBarcos[inimigo] < 1:
            return False
        
        quantTotalBarcos[inimigo] -= 1 # bug: não faço ideia kkkk
        print("🔥 ACERTOU!\n")
        return True
    
    else:
        tabuleiros[inimigo][linha][coluna] = '💣'
        print("💣 ERROU!")
        return False
'''

# Funções pra fazer
def posicionarBarcos(jogadorAtual):
    print('A')

def posicionarBarcosMaquina():
    print('A')

def validarPosicao():
    print('A')

'''
def exibirVitoria(jogadorAtual, resposta):
    # Roda o jogo até alguém ganhar
    while quantTotalBarcos[0] > 0 or quantTotalBarcos[1] > 0:
        capturarJogada(jogadorAtual)
        input('\nAperte ⏎ Enter para começar.')
        jogadorAtual = alternarJogador(jogadorAtual)

    if resposta == 1:
        jogador2 = 'Jogador 2'
    else:
        jogador2 = 'Computador'
        
    # Imprime a mensagem de vitória conforme adversário
    if quantTotalBarcos[1] == 0 :
        print(f'Jogador 1 ganhou! 🎉')
    else:
        print(f'{jogador2} ganhou! 🎉')
'''

def verificarVitoria(modoDeJogo):
    jogadorAtual = sortearJogadores(modoDeJogo)

    while True:
        status = turno(jogadorAtual, modoDeJogo)

        if status == 'vitoria':
            if modoDeJogo == 1:
                jogador2 = 'Jogador 2'
            else:
                jogador2 = 'Computador'
                
            # Imprime a mensagem de vitória conforme adversário
            if quantTotalBarcos[1] == 0 :
                print(f'Jogador 1 ganhou! 🎉')
            else:
                print(f'{jogador2} ganhou! 🎉')
            break
        jogadorAtual = alternarJogador(jogadorAtual)
    

def menu():
    limparTerminal()
    print('---------------------------------------------')
    print('----------------BATALHA NAVAL----------------')
    print('---------------------------------------------\n')
    print('Escolha uma das opções: \n1. Jogar contra amigos\n2. Jogar contra a máquina\n3. Regras')

    tabuleiros[0][0][0] = '🚢'
    tabuleiros[1][0][0] = '🚢'
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
            verificarVitoria(resposta)

        case 2:
            verificarVitoria(resposta)

        case _:
            limparTerminal()
            print('regras')

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

def main():
    while True:
        # Resetar tabuleiro
        criarNovosTabuleiros(tabuleiros, quantTotalBarcos, jogadas_certas, jogadas_erradas)

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

# tiroAleatorio
# validacao
#     trocaJogador
#     JogaDnv
#     VERIFICAR

# menu (
#     sortearJogadores
#     exibirVitoria(
#         while barcosRestantes > 0:
#             if acertou
#             capturarJogada
#             validarJogada
#             else:
#             alternarJogador
#             continue
            
#         'Ganhou'
#     )
# )

# posicaoMaquina = tiroAleatorio():
#             (ultima_jogada[0] - 1, ultima_jogada[1]), # Acima
#             (ultima_jogada[0] + 1, ultima_jogada[1]), # Abaixo
#             (ultima_jogada[0], ultima_jogada[1] - 1), # Esquerda
#             (ultima_jogada[0], ultima_jogada[1] + 1) 
# posicionarBarcosMaquina
# posicionarBarcosJogador
#     validar 
# posicionarBarcos(posicaoMaquina)
# posicionarBarcos(posicao)(
#     validarPosição
#     validarTamanho
#     tabuleiro = posicao 'O' = 'B'
#     quantBarcos =+ 1
# )

'''
barcos_restantes_template = {    
    4: 1,  # 1 barco de 4 posições   
    3: 2,  # 2 barcos de 3 posições
    2: 2,  # 2 barcos de 2 posições
    1: 1   # 1 barco de 1 
}

def coordenada_para_indices(coordenada):
    letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}  # Mapeamento das letras para índices
    letra = coordenada[0].upper()
    numero = coordenada[1:]
    if letra in letras and numero.isdigit():
        linha = int(numero) - 1
        coluna = letras[letra]
        if 0 <= linha <= 7 and 0 <= coluna <= 7:
            return linha, coluna
    return None



def validarPosicao(tabuleiro, coord1, coord2, barcos_restantes):
    linha1, col1 = coord1
    linha2, col2 = coord2

    if linha1 == linha2: 
        tamanho = abs(col2 - col1) + 1                                  # checa se é horizontal fazendo a diferença entre as colunas
    else:
        tamanho = abs(linha2 - linha1) + 1                              # checa se é vertical fazendo a diferença entre as linhas
        return False, "❌ O barco deve estar em linha reta (horizontal ou vertical).", None

    tamanho = abs(linha2 - linha1 + col2 - col1) + 1                    # tamanho do barco (considerando linha ou coluna) e +1 para incluir a casa inicial abs para garantir valor positivo

    if tamanho not in barcos_restantes or barcos_restantes[tamanho] == 0:       # checa se o tamanho é válido e se ainda há barcos desse tamanho disponíveis
        return False, f"❌ Você não pode posicionar mais barcos de {tamanho} casas.", None

    # Verifica sobreposição
    if linha1 == linha2:  # horizontal
        for col in range(min(col1, col2), max(col1, col2)+1):   # percorre as colunas entre col1 e col2 e verifica se já há um barco
            if tabuleiro[linha1][col] != '🌊':                  # Se o emoji for diferente de mar, retorna falso
                return False, "🚫 Já existe um barco nessa posição.", None
    else:  # vertical
        for lin in range(min(linha1, linha2), max(linha1, linha2)+1):       
            if tabuleiro[lin][col1] != '🌊':
                return False, "🚫 Já existe um barco nessa posição.", None

    return True, "✅ Posição válida.", tamanho


def posicionarBarcos(jogador):                                                    # jogador = 0 ou 1
    while sum(barcos_por_jogador[jogador].values()) > 0:                          # enquanto a soma dos valores do dicionário for maior que 0, ou seja, enquanto houver barcos para posicionar
        exibirTabuleiro(jogador, f"Jogador {jogador + 1}")                        # exibe o tabuleiro do jogador atual
        print("📦 Barcos restantes:")                                             # exibe os barcos restantes
        for tamanho, qtd in barcos_por_jogador[jogador].items():                  # percorre o dicionário de barcos restantes
            if qtd > 0:
                print(f" - {qtd} barco(s) de {tamanho} casas")                    # exibe a quantidade de barcos de cada tamanho

        entrada = input("Digite a posição inicial e final do barco (ex: A1 A4): ").strip().upper()         # captura a entrada do jogador e formata
        try:
            inicio, fim = entrada.split()                                       # tenta separar a entrada em duas partes
        except ValueError:                                                      # se não conseguir, exibe mensagem de erro e continua o loop
            print("❌ Entrada inválida. Use o formato: A1 A4.")                 
            continue

        coord1 = coordenada_para_indices(inicio)                         # converte as coordenadas para índices
        coord2 = coordenada_para_indices(fim)                       

        if not coord1 or not coord2:                                     # se alguma das coordenadas for inválida, exibe mensagem de erro e continua o loop
            print("❌ Coordenadas inválidas.") 
            continue

        valido, msg, tamanho = validarPosicao(tabuleiros[jogador], coord1, coord2, barcos_por_jogador[jogador])     # valida a posição
        if not valido:      
            print(msg)
            continue

        # ✅ Posiciona o barco
        linha1, col1 = coord1               # desempacota as coordenadas
        linha2, col2 = coord2               # desempacota as coordenadas

        if linha1 == linha2: 
            for col in range(min(col1, col2), max(col1, col2)+1):   # percorre as colunas entre col1 e col2 e posiciona o barco
                tabuleiros[jogador][linha1][col] = '🚢'             # posiciona o barco no tabuleiro
        else:
            for lin in range(min(linha1, linha2), max(linha1, linha2)+1):
                tabuleiros[jogador][lin][col1] = '🚢'

        barcos_por_jogador[jogador][tamanho] -= 1                   # decrementa a quantidade de barcos restantes do tamanho usado

    print(f"\n✅ Jogador {jogador + 1}, todos os barcos foram posicionados!\n")
    input("Aperte ⏎ para continuar.")
    limparTerminal()


#nao tenho ideia do que é isso
def posicionarBarcosMaquina(jogador):
    while sum(barcos_por_jogador[jogador].values()) > 0:
        tamanho_aleatorio = random.choice([t for t, q in barcos_por_jogador[jogador].items() if q > 0])

        orientacao = random.choice(['H', 'V'])
        linha = random.randint(0, 7)
        coluna = random.randint(0, 7)

        if orientacao == 'H':
            if coluna + tamanho_aleatorio > 8:
                continue
            coord1 = (linha, coluna)
            coord2 = (linha, coluna + tamanho_aleatorio - 1)
        else:
            if linha + tamanho_aleatorio > 8:
                continue
            coord1 = (linha, coluna)
            coord2 = (linha + tamanho_aleatorio - 1, coluna)

        valido, msg, tamanho = validarPosicao(tabuleiros[jogador], coord1, coord2, barcos_por_jogador[jogador])
        if not valido:
            continue

        # Posiciona
        linha1, col1 = coord1
        linha2, col2 = coord2

        if linha1 == linha2:
            for col in range(col1, col2 + 1):
                tabuleiros[jogador][linha1][col] = '🚢'
        else:
            for lin in range(linha1, linha2 + 1):
                tabuleiros[jogador][lin][col1] = '🚢'

        barcos_por_jogador[jogador][tamanho] -= 1
        
        
        global barcos_por_jogador
barcos_por_jogador = [barcos_restantes_template.copy(), barcos_restantes_template.copy()]
'''

