''' Testes no ajuste de variáveis globais
import random
import time
import os

# Variáveis globais de configuração (agora não são alteradas durante o jogo)
barcos_restantes_template = {    
    4: 1,  # 1 barco de 4 posições  
    3: 2,  # 2 barcos de 3 posições
    2: 2,  # 2 barcos de 2 posições
    1: 1   # 1 barco de 1 
}

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

def criarNovosTabuleiros():
    tabuleiros = []
    barcos_por_jogador = []
    for _ in range(2):
        tabuleiro = [['🌊' for _ in range(8)] for _ in range(8)]
        tabuleiros.append(tabuleiro)
        barcos_por_jogador.append(barcos_restantes_template.copy())
    return tabuleiros, barcos_por_jogador

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def sortearJogadores(modoDeJogo):
    limparTerminal()
    print(f'Sorteando os jogadores', end='')
    for _ in range(3):
        time.sleep(0.3)
        print('.', end='')
    time.sleep(0.3)
    print('\n---------------------------------------------\n')
    
    jogador2 = 'Jogador 2' if modoDeJogo == 1 else 'Computador'
    primeiroAJogar = random.choice(['Jogador 1', jogador2])
    print(f'Quem joga primeiro é o {primeiroAJogar}!')
    
    input('\nAperte ⏎ Enter para começar.')

    return 0 if primeiroAJogar == 'Jogador 1' else 1

def exibirTabuleiro(tabuleiros, jogadorAtual, ocultar=True):    
    limparTerminal()
    print(' A    B    C    D    E    F    G    H')
    print('_______________________________________')
    for i in range(8):
        linha_formatada = ''
        for j in range(8):
            simbolo = tabuleiros[jogadorAtual][i][j]
            if simbolo == '🚢' and ocultar:
                linha_formatada += '🌊' + ' | '
            else:
                linha_formatada += simbolo + ' | '
        print(linha_formatada + f'{i+1}')
    print('_______________________________________\n')

def alternarJogador(jogadorAtual):
    return 1 - jogadorAtual

def capturarEntrada(jogadorAtual, modoDeJogo, jogadas_certas, jogadas_erradas):
    if modoDeJogo == 2 and jogadorAtual == 1:
        return maquina(jogadas_certas, jogadas_erradas)
    else:
        entrada = input(f"🎯 Jogador {jogadorAtual + 1}, escolha uma posição (ex: B4): ").strip().upper()
        return entrada

def validarEntrada(entrada):
    colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    if isinstance(entrada, tuple):
        return entrada
    if len(entrada) < 2 or len(entrada) > 3 or entrada[0].upper() not in colunas or not entrada[1:].isdigit():
        return None
    
    letra, numero = entrada[0], entrada[1:]
    linha = int(numero) - 1
    coluna = colunas[letra]

    if 0 <= linha <= 7 and 0 <= coluna <= 7:
        return (linha, coluna)
    else:
        return None

def processarJogada(jogadorAtual, coordenadas, modoDeJogo, tabuleiros, quantBarcosTotais, jogadas_certas, jogadas_erradas):
    inimigo = 1 - jogadorAtual
    linha, coluna = coordenadas
    simbolo = tabuleiros[inimigo][linha][coluna]

    if simbolo in ['🔥', '💣']:
        if not (modoDeJogo == 2 and jogadorAtual == 1):
            print("⛔ Já jogou aqui.")
            input("Aperte ⏎ Enter para continuar...")
        return 'repetida'

    if simbolo == '🚢':
        tabuleiros[inimigo][linha][coluna] = '🔥'
        quantBarcosTotais[inimigo] -= 1
        if modoDeJogo == 2 and jogadorAtual == 1:
            print("🤖 O computador jogou e ACERTOU!")
            jogadas_certas.append(coordenadas)
        else:
            print("🔥 ACERTOU!")
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
        return 'erro'

def loopDoJogo(jogadorAtual, modoDeJogo, tabuleiros, quantBarcosTotais):
    jogadas_certas = []
    jogadas_erradas = []
    while quantBarcosTotais[0] > 0 and quantBarcosTotais[1] > 0:
        if modoDeJogo == 2 and jogadorAtual == 1:
            print("Vez do Computador...")
            time.sleep(1)
        
        exibirTabuleiro(tabuleiros, 1 - jogadorAtual)
        
        entrada = capturarEntrada(jogadorAtual, modoDeJogo, jogadas_certas, jogadas_erradas)
        coordenadas = validarEntrada(entrada)
        
        if coordenadas is None:
            if not (modoDeJogo == 2 and jogadorAtual == 1):
                print("❌ Entrada inválida.")
                input("\nAperte ⏎ Enter para continuar...")
            continue
        
        resultado = processarJogada(jogadorAtual, coordenadas, modoDeJogo, tabuleiros, quantBarcosTotais, jogadas_certas, jogadas_erradas)
        
        if resultado == 'vitoria':
            return jogadorAtual
        elif resultado == 'erro' or resultado == 'repetida':
            jogadorAtual = alternarJogador(jogadorAtual)
    return 1 - jogadorAtual

def exibirVitoria(vencedor, modoDeJogo):
    limparTerminal()
    print('---------------------------------------------')
    print('-----------------FIM DE JOGO-----------------')
    print('---------------------------------------------\n')
    
    if modoDeJogo == 1:
        vencedor_nome = 'Jogador 1' if vencedor == 0 else 'Jogador 2'
    else:
        vencedor_nome = 'Jogador 1' if vencedor == 0 else 'Computador'

    print(f'🎉 O vencedor é o {vencedor_nome}! 🎉\n')

def iniciarNovoJogo(modoDeJogo):
    tabuleiros, barcos_por_jogador = criarNovosTabuleiros()
    quantBarcosTotais = [15, 15]

    jogadorAtual = sortearJogadores(modoDeJogo)

    if modoDeJogo == 2:
        if jogadorAtual == 0:
            posicionarBarcos(0, tabuleiros, barcos_por_jogador)
            posicionarBarcosMaquina(1, tabuleiros, barcos_por_jogador)
        else:
            posicionarBarcosMaquina(1, tabuleiros, barcos_por_jogador)
            posicionarBarcos(0, tabuleiros, barcos_por_jogador)
    else:
        posicionarBarcos(0, tabuleiros, barcos_por_jogador)
        posicionarBarcos(1, tabuleiros, barcos_por_jogador)
        
    vencedor = loopDoJogo(jogadorAtual, modoDeJogo, tabuleiros, quantBarcosTotais)
    exibirVitoria(vencedor, modoDeJogo)

def menu():
    limparTerminal()
    print('---------------------------------------------')
    print('----------------BATALHA NAVAL----------------')
    print('---------------------------------------------\n')
    print('Escolha uma das opções: \n1. Jogar contra amigos\n2. Jogar contra a máquina\n3. Regras\n4. Sair do jogo')
    
    while True:
        try:
            resposta = int(input('\nR: '))
            if 1 <= resposta <= 4:
                return resposta
            else:
                print('Digite apenas números entre 1 e 4.')
        except ValueError:
            print('Digite apenas números inteiros')

def validarPosicao(tabuleiro, coord1, coord2, barcos_restantes):
    if not coord1 or not coord2:
        return False, "❌ Coordenadas inválidas.", None

    linha1, col1 = coord1
    linha2, col2 = coord2

    if linha1 != linha2 and col1 != col2:
        return False, "❌ O barco deve estar em linha reta (horizontal ou vertical).", None

    if linha1 == linha2:
        tamanho = abs(col2 - col1) + 1
    else:
        tamanho = abs(linha2 - linha1) + 1

    if tamanho not in barcos_restantes or barcos_restantes[tamanho] == 0:
        return False, f"❌ Você não pode posicionar mais barcos de {tamanho} casas.", None

    if linha1 == linha2:
        for col in range(min(col1, col2), max(col1, col2) + 1):
            if tabuleiro[linha1][col] != '🌊':
                return False, "🚫 Já existe um barco nessa posição.", None
    else:
        for lin in range(min(linha1, linha2), max(linha1, linha2) + 1):
            if tabuleiro[lin][col1] != '🌊':
                return False, "🚫 Já existe um barco nessa posição.", None
    
    return True, "✅ Posição válida.", tamanho

def posicionarBarcos(jogador, tabuleiros, barcos_por_jogador):
    while sum(barcos_por_jogador[jogador].values()) > 0:
        exibirTabuleiro(tabuleiros, jogador, ocultar=False)
        print(f'\n Jogador {jogador + 1} coloque seus barcos no tabuleiro!')
        print("📦 Barcos restantes:")
        for tamanho, qtd in barcos_por_jogador[jogador].items():
            if qtd > 0:
                print(f" - {qtd} barco(s) de {tamanho} casas")

        entrada = input("Digite a posição inicial e final do barco (ex: A1 A4): ").strip().upper()
        try:
            inicio, fim = entrada.split()
        except ValueError:
            print("❌ Entrada inválida. Use o formato: A1 A4.")
            input('\nAperte ⏎ Enter para continuar.')
            continue

        coord1 = validarEntrada(inicio)
        coord2 = validarEntrada(fim)

        valido, msg, tamanho = validarPosicao(tabuleiros[jogador], coord1, coord2, barcos_por_jogador[jogador])
        if not valido:
            print(msg)
            input('\nAperte ⏎ Enter para continuar.')
            continue

        linha1, col1 = coord1
        linha2, col2 = coord2

        if linha1 == linha2:
            for col in range(min(col1, col2), max(col1, col2) + 1):
                tabuleiros[jogador][linha1][col] = '🚢'
        else:
            for lin in range(min(linha1, linha2), max(linha1, linha2) + 1):
                tabuleiros[jogador][lin][col1] = '🚢'

        barcos_por_jogador[jogador][tamanho] -= 1

    print(f"\n✅ Jogador {jogador + 1}, todos os barcos foram posicionados!\n")
    input("Aperte ⏎ para continuar.")
    limparTerminal()

def posicionarBarcosMaquina(jogador, tabuleiros, barcos_por_jogador):
    print("A máquina está posicionando seus barcos...")
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

        valido, _, tamanho = validarPosicao(tabuleiros[jogador], coord1, coord2, barcos_por_jogador[jogador])
        
        if not valido:
            continue

        linha1, col1 = coord1
        linha2, col2 = coord2
        if linha1 == linha2:
            for col in range(min(col1, col2), max(col1, col2) + 1):
                tabuleiros[jogador][linha1][col] = '🚢'
        else:
            for lin in range(min(linha1, linha2), max(linha1, linha2) + 1):
                tabuleiros[jogador][lin][col1] = '🚢'

        barcos_por_jogador[jogador][tamanho] -= 1
    
    print("✅ Máquina, todos os barcos foram posicionados!\n")
    input('Aperte ⏎ para continuar.')

def tiroAleatorio():
    linha = random.randint(0, 7)
    coluna = random.randint(0, 7)
    return (linha, coluna)

def maquina(jogadas_certas, jogadas_erradas):
    tiro = None
    if jogadas_certas:
        ultima_jogada = jogadas_certas[-1]
        opcoes_de_tiro = [
            (ultima_jogada[0] - 1, ultima_jogada[1]), 
            (ultima_jogada[0] + 1, ultima_jogada[1]),
            (ultima_jogada[0], ultima_jogada[1] - 1), 
            (ultima_jogada[0], ultima_jogada[1] + 1)
        ]
        
        tiros_validos = [
            op for op in opcoes_de_tiro 
            if 0 <= op[0] <= 7 and 0 <= op[1] <= 7 and op not in jogadas_certas and op not in jogadas_erradas
        ]
        
        if tiros_validos:
            tiro = random.choice(tiros_validos)
    
    if not tiro:
        tiro = tiroAleatorio()
        while tiro in jogadas_certas or tiro in jogadas_erradas:
            tiro = tiroAleatorio()
            
    return tiro

def main():
    while True:
        resposta = menu()
        
        if resposta == 1:
            iniciarNovoJogo(resposta)
        elif resposta == 2:
            iniciarNovoJogo(resposta)
        elif resposta == 3:
            mostrarRegras()
        elif resposta == 4:
            break
        
        print('\n\n---------------------------------------------')
        print('-----------------FIM DE JOGO-----------------')
        print('---------------------------------------------\n')
        print('Quer jogar novamente? Responda apenas "sim" ou "não"')
        confirmacao = input('R: ').lower().strip()
        if confirmacao in ['nao', 'não']:
            break

if __name__ == '__main__':
    main()
'''