'''
1. Função para exibir menu principal:
    - imprimir opções
    - capturar resposta do usuário
    - validar se a resposta está dentro do esperado
    - levar para a opção selecionada dentro de um match case
2. Função para criar e resetar listas:
    - criar e recriar as principais listas: tabuleiros, jogadas_certas, jogadas_erradas, barcos_restantes_template, barcos_por_jogador e quantBarcosTotais
    
2. Função para posicionar barcos:
    - exibir tabuleiro vazio
    - capturar posição e tamanho do barco com base em coordenadas (exemplo A2 e B2)
    - posicionar na lista os barcos, trocando o emoji de onda pelo emoji de barco
    - verificar se todos os barcos foram posicionados, e então passar a vez através da função alternar jogadores
    - validar se não há sobreposição
    - validar se a posição existe no tabuleiro
    - validar se não atingiu o limite de barcos (1 de 4 casas, 2 de cada 3, 2 e 1 casa)

3. Função para sortear jogador:
    - retorna 0 ou 1 aleatoriamente para ser usado como indice do jogador

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
barcos_restantes_template = {    
    4: 1,  # 1 barco de 4 posições   
    3: 2,  # 2 barcos de 3 posições
    2: 2,  # 2 barcos de 2 posições
    1: 1   # 1 barco de 1 
}
barcos_por_jogador = []
quantBarcosTotais = [15, 15]

def mostrarRegras():
    limparTerminal()
    print('------------------ REGRAS ------------------\n')

    print('🎮 OBJETIVO DO JOGO:')
    print('- Destruir todos os barcos do oponente antes que ele destrua os seus.\n')

    print('🚢 POSICIONAMENTO DE BARCOS:')
    print('- Cada jogador tem os seguintes barcos:')
    print('   • 1 barco de 4 casas')
    print('   • 2 barcos de 3 casas')
    print('   • 2 barcos de 2 casas')
    print('   • 1 barco de 1 casa')
    print('- Os barcos devem ser colocados em linha reta (horizontal ou vertical).')
    print('- Não é permitido sobrepor barcos.')
    print('- Para posicionar, digite a posição inicial e final (ex: A1 A4).\n')

    print('🗺️ JOGANDO:')
    print('- Em cada rodada, o jogador escolhe uma posição para atacar (ex: B3).')
    print('- Se atingir um barco, será marcado com 🔥.')
    print('- Se errar, será marcado com 💣.')
    print('- Se já tiver atacado a posição, perderá a vez.\n')

    print('👾 MODO CONTRA A MÁQUINA:')
    print('- O computador posiciona seus barcos aleatoriamente.')
    print('- Ele tenta jogar perto de acertos anteriores.\n')

    print('🏁 VITÓRIA:')
    print('- Ganha quem destruir todos os barcos do oponente primeiro.\n')

    input('Aperte ⏎ para voltar ao menu.')
    menu()

def criarNovosTabuleiros(tabuleiros, jogadas_certas, jogadas_erradas, barcos_por_jogador):
    # Redefinição da quantidade inicial de barcos
    jogadas_certas.clear()
    jogadas_erradas.clear()

    for _ in range(2):
        if len(tabuleiros) == 2:
            tabuleiros.clear()
            barcos_por_jogador.clear()
        
        barco_por_jogador = barcos_restantes_template.copy()
        tabuleiro = []

        for _ in range(8):
            novaLinha = []
            for _ in range(8):
                novaLinha.append('🌊')
            tabuleiro.append(novaLinha)
        tabuleiros.append(tabuleiro)
        barcos_por_jogador.append(barco_por_jogador)

# Função para limpar o terminal (variação para Windows e macOS)
def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else :
        os.system('clear')

def definirNomeJogador(modoDeJogo):
    if modoDeJogo == 1:
        return 'Jogador 2'
    elif modoDeJogo == 2:
        return 'Computador'

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
    
    jogador2 = definirNomeJogador(modoDeJogo)

    primeiroAJogar = random.choice(['Jogador 1', jogador2])
    print(f'Quem joga primeiro é o {primeiroAJogar}!')
    
    input('\nAperte ⏎ Enter para começar.')

    if primeiroAJogar == 'Jogador 1':
        return 0
    else:
        return 1

#função para exibir tabuleiro
def exibirTabuleiro(jogadorAtual, ocultar = True):    
    limparTerminal()

    print(' A   B    C    D    E    F    G    H')
    print('_______________________________________')

    for i in range(8):
            linha_formatada = ''
            for j in range(8):
                simbolo = tabuleiros[jogadorAtual][i][j]
                if simbolo == '🚢' and ocultar == True:
                    linha_formatada += '🌊' + ' | '
                else:
                    linha_formatada += simbolo + ' | '
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
        quantBarcosTotais[inimigo] -= 1

        if modoDeJogo == 2 and jogadorAtual == 1:
            print("🤖 O computador jogou e ACERTOU!")
            jogadas_certas.append(coordenadas)
            
        else:
            print("🔥 ACERTOU!")
        input("\nAperte ⏎ Enter  para continuar...")        
        
        if quantBarcosTotais[inimigo] > 0:
            return 'acerto'
        else:
            return 'vitoria'
    
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

def alternarTurno(jogadorAtual, modoDeJogo):
    while True:
        status = turno(jogadorAtual, modoDeJogo)
        exibirVitoria(status, jogadorAtual, modoDeJogo)
        jogadorAtual = alternarJogador(jogadorAtual)

def exibirVitoria(status, jogadorAtual, modoDeJogo):
    if status == 'vitoria':
        jogador2 = definirNomeJogador(modoDeJogo)
            
        # Imprime a mensagem de vitória conforme adversário
        if quantBarcosTotais[1 - jogadorAtual] == 0:
            print(f'Jogador 1 ganhou! 🎉')
        else:
            print(f'{jogador2} ganhou! 🎉')
        
    return


def validarPosicao(tabuleiro, coord1, coord2, barcos_restantes):
    linha1, col1 = coord1
    linha2, col2 = coord2

    if linha1 != linha2 and col1 != col2:
        return False, "❌ O barco deve estar em linha reta (horizontal ou vertical).", None
    
    tamanho = abs(linha2 - linha1 + col2 - col1) + 1                    # tamanho do barco (considerando linha ou coluna) e +1 para incluir a casa inicial abs para garantir valor positivo

    if tamanho not in barcos_restantes or barcos_restantes[tamanho] == 0:       # checa se o tamanho é válido e se ainda há barcos desse tamanho disponíveis
        return False, f"❌ Você não pode posicionar mais barcos de {tamanho} casas.", None

    # Verifica sobreposição
    if linha1 == linha2:  # horizontal
        for col in range(min(col1, col2), max(col1, col2)+1):   # percorre as colunas entre col1 e col2 e verifica se já há um barco
            if tabuleiro[linha1][col] != '🌊':                  # Se o emoji for diferente de mar, retorna falso
                return False, "🚫 Já existe um barco nessa posição.", None
    else:  # Horizontal
        for lin in range(min(linha1, linha2), max(linha1, linha2)+1):       
            if tabuleiro[lin][col1] != '🌊':
                return False, "🚫 Já existe um barco nessa posição.", None

    return True, "✅ Posição válida.", tamanho

def posicionarBarcos(jogador, barcos_por_jogador):                                                    # jogador = 0 ou 1
    while sum(barcos_por_jogador[jogador].values()) > 0:                          # enquanto a soma dos valores do dicionário for maior que 0, ou seja, enquanto houver barcos para posicionar
        exibirTabuleiro(jogador, False)                        # exibe o tabuleiro do jogador atual
        print(f'\n Jogador {jogador+1} coloque seus barcos no tabuleiro!')
        print("📦 Barcos restantes:")                                             # exibe os barcos restantes
        for tamanho, qtd in barcos_por_jogador[jogador].items():                  # percorre o dicionário de barcos restantes
            if qtd > 0:
                print(f" - {qtd} barco(s) de {tamanho} casas")                    # exibe a quantidade de barcos de cada tamanho

        entrada = input("Digite a posição inicial e final do barco (ex: A1 A4): ").strip().upper()         # captura a entrada do jogador e formata
        try:
            inicio, fim = entrada.split()                                       # tenta separar a entrada em duas partes
        except ValueError:                                                      # se não conseguir, exibe mensagem de erro e continua o loop
            print("❌ Entrada inválida. Use o formato: A1 A4.")                 
            input('\nAperte ⏎ Enter para continuar.')
            continue 

        coord1 = validarEntrada(inicio)                         # converte as coordenadas para índices
        coord2 = validarEntrada(fim)                       

        if not coord1 or not coord2:                                     # se alguma das coordenadas for inválida, exibe mensagem de erro e continua o loop
            print("❌ Coordenadas inválidas.")
            input('\nAperte ⏎ Enter para continuar.')
            continue

        valido, msg, tamanho = validarPosicao(tabuleiros[jogador], coord1, coord2, barcos_por_jogador[jogador])     # valida a posição
        if not valido:
            print(msg)
            input('\nAperte ⏎ Enter para continuar.')
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

def posicionarBarcosMaquina(jogador, barcos_por_jogador):
    while sum(barcos_por_jogador[jogador].values()) > 0:
        tamanho_aleatorio = random.choice([t for t, q in barcos_por_jogador[jogador].items() if q > 0])

        orientacao = random.choice(['H', 'V'])
        linha, coluna = tiroAleatorio()
        
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

def tiroAleatorio():
    """Gera coordenadas de um tiro aleatório no tabuleiro."""
    linha = random.randint(0, 7)
    coluna = random.randint(0, 7)
    return (linha, coluna)

def maquina(jogadas_certas, jogadas_erradas):
    """
    Decide onde a máquina deve atirar com base nas jogadas anteriores.
    
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

        if tiros_validos:
            tiro = random.choice(tiros_validos)
    
    # Se não houver acertos ou se a lógica de 'caça' não encontrar um tiro válido
    if not tiro:
        tiro = tiroAleatorio()
        while tiro in jogadas_certas or tiro in jogadas_erradas:
            tiro = tiroAleatorio()
                
    return tiro

def jogar(modoDeJogo):
    jogadorAtual = sortearJogadores(modoDeJogo)

    if modoDeJogo == 2:
        for _ in range(2):
            if jogadorAtual == 1:
                posicionarBarcosMaquina(jogadorAtual, barcos_por_jogador)
            else:
                posicionarBarcos(jogadorAtual, barcos_por_jogador)

            jogadorAtual = alternarJogador(jogadorAtual)
    
    else:
        for _ in range(2):
            posicionarBarcos(jogadorAtual, barcos_por_jogador)
            jogadorAtual = alternarJogador(jogadorAtual)

    alternarTurno(jogadorAtual, modoDeJogo)

def menu():
    limparTerminal()
    print('---------------------------------------------')
    print('----------------BATALHA NAVAL----------------')
    print('---------------------------------------------\n')
    print('Escolha uma das opções: \n1. Jogar contra amigos\n2. Jogar contra a máquina\n3. Regras\n4. Sair do jogo')
    
    # Validação de entrada para menu
    while True:
        try:
            resposta = int(input('\nR: '))

            if resposta >= 1 and resposta <= 4:
                break
            else:
                print('Digite apenas números entre 1 e 4.')
                
        except ValueError:
            print('Digite apenas números inteiros')
    
    match resposta:
        case 1:
            jogar(resposta)

        case 2:
            jogar(resposta)

        case 3:
            mostrarRegras()
        case _:
            return

def main():
    while True:
        # Resetar tabuleiro
        criarNovosTabuleiros(tabuleiros, jogadas_certas, jogadas_erradas, barcos_por_jogador)

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