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

# -------------------------- UTIL --------------------------
def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# -------------------------- ESTADO ------------------------ 
def criarEstado():
    """
    Dicionario para evitar variaveis globais
    """
    return {
        "tabuleiros": [],                
        "jogadas_certas": [],            
        "jogadas_erradas": [],           
        "barcos_por_jogador": [],        
        "quantBarcosTotais": [15, 15],   
        "barcos_restantes_template": {
            4: 1,  # 1 barco de 4
            3: 2,  # 2 barcos de 3
            2: 2,  # 2 barcos de 2
            1: 1   # 1 barco de 1
        }
    }

def criarNovosTabuleiros(estado):
    """
    Reseta toda a estrutura do jogo e gera 2 tabuleiros vazios com emojis - 🌊
    """
    estado["jogadas_certas"].clear()
    estado["jogadas_erradas"].clear()
    estado["tabuleiros"].clear()
    estado["barcos_por_jogador"].clear()
    estado["quantBarcosTotais"] = [15, 15]

    for _ in range(2):
        barco_por_jogador = estado["barcos_restantes_template"].copy()
        tabuleiro = [["🌊" for _ in range(8)] for _ in range(8)]
        estado["tabuleiros"].append(tabuleiro)
        estado["barcos_por_jogador"].append(barco_por_jogador)

# ---------------------- TELAS / REGRAS --------------------
def mostrarRegras(estado):
    """
    Função para exibir regras do jogo
    """
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
 

# ---------------------- FLUXO DE JOGO ---------------------
def definirNomeJogador(modoDeJogo):
    """
    Função para definir jogador 2
    """
    return 'Computador' if modoDeJogo == 2 else 'Jogador 2'

def sortearJogadores(modoDeJogo):
    """
    Função sortear jogador e exibir ao usuario.
    """
    limparTerminal()
    print('Sorteando os jogadores', end='')
    for _ in range(3):
        time.sleep(0.3)
        print('.', end='')
    print('\n---------------------------------------------\n')

    jogador2 = definirNomeJogador(modoDeJogo)
   
    primeiroAJogar = random.choice(['Jogador 1', jogador2])
    print(f'Quem joga primeiro é o {primeiroAJogar}!')
    input('\nAperte ⏎ Enter para começar.')

    return 0 if primeiroAJogar == 'Jogador 1' else 1

def exibirTabuleiro(estado, jogadorAtual, ocultar=True):
    """
    Função para exibir tabuleiro e ocultar barcos do adversario 
    """
    limparTerminal()
    print(' A   B    C    D    E    F    G    H')
    print('_______________________________________')
    tabuleiro = estado["tabuleiros"][jogadorAtual]
    for i in range(8):
        linha_formatada = ''
        for j in range(8):
            simbolo = tabuleiro[i][j]
            if simbolo == '🚢' and ocultar:
                linha_formatada += '🌊' + ' | '
            else:
                linha_formatada += simbolo + ' | '
        print(linha_formatada + f'{i+1}')
    print('_______________________________________\n')

def alternarJogador(jogadorAtual):
    """
    Função para alternar jogador
    """
    return 1 - jogadorAtual

def capturarEntrada(estado, jogadorAtual, modoDeJogo):
    """
    Função para capturar entrada. Maquina/Usuario(s)
    """
    if modoDeJogo == 2 and jogadorAtual == 1:
        # máquina decide a jogada
        return maquina(estado["jogadas_certas"], estado["jogadas_erradas"])
    else:
        entrada = input(f"🎯 Jogador {jogadorAtual + 1}, escolha uma posição (ex: B4): ").strip().upper()
        return entrada

def validarEntrada(entrada):
    """
    Função para validar entrada dos jogadores
    """
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
    return None

def processarJogada(estado, jogadorAtual, coordenadas, modoDeJogo):
    """
    Função para validar e adicionar emojis ao tabuleiro.
    Retorna se houver Acerto, Erro ou Vitoria 
    """
    inimigo = 1 - jogadorAtual
    linha, coluna = coordenadas
    simbolo = estado["tabuleiros"][inimigo][linha][coluna]

    if simbolo in ['🔥', '💣']:
        print("⛔ Já jogou aqui.")
        input("Aperte ⏎ Enter para continuar...")
        return 'repetida'

    if simbolo == '🚢':
        estado["tabuleiros"][inimigo][linha][coluna] = '🔥'
        estado["quantBarcosTotais"][inimigo] -= 1

        if modoDeJogo == 2 and jogadorAtual == 1:
            print("🤖 O computador jogou e ACERTOU!")
            estado["jogadas_certas"].append(coordenadas)
        else:
            print("🔥 ACERTOU!")
        input("\nAperte ⏎ Enter para continuar...")

        if estado["quantBarcosTotais"][inimigo] > 0:
            return 'acerto'
        else:
            return 'vitoria'
    else:
        estado["tabuleiros"][inimigo][linha][coluna] = '💣'
        if modoDeJogo == 2 and jogadorAtual == 1:
            print("🤖 O computador jogou e ERROU!")
            estado["jogadas_erradas"].append(coordenadas)
        else:
            print("💣 ERROU!")
        input("\nAperte ⏎ Enter para continuar...")
        return 'erro'

def turno(estado, jogadorAtual, modoDeJogo):
    """
    Função para verificar erro e alternar turno.
    Oculta barcos do inimigo
    """
    while True:
        # mostra o tabuleiro do inimigo 
        if not (modoDeJogo == 2 and jogadorAtual == 1):
            exibirTabuleiro(estado, 1 - jogadorAtual, ocultar=True)
        else:
            limparTerminal()

        entrada = capturarEntrada(estado, jogadorAtual, modoDeJogo)
        coordenadas = validarEntrada(entrada)
        if coordenadas is None:
            print("❌ Entrada inválida.")
            input("\nAperte ⏎ Enter para continuar...")
            continue

        resultado = processarJogada(estado, jogadorAtual, coordenadas, modoDeJogo)
        if resultado == 'repetida':
            continue
        if resultado == 'vitoria':
            return 'vitoria'
        if resultado == 'erro':
            return 'erro'
        

def alternarTurno(estado, jogadorAtual, modoDeJogo):
    """
    Função que verifica vitoria senão alterna jogador.
    """
    while True:
        status = turno(estado, jogadorAtual, modoDeJogo)
        if status == 'vitoria':
            exibirVitoria(estado, jogadorAtual, modoDeJogo)
            break
        jogadorAtual = alternarJogador(jogadorAtual)

def exibirVitoria(estado, jogadorAtual, modoDeJogo):
    """
    Função para verificar jogador vencedor e exibir no terminal.
    """
    vencedor = "Jogador 1" if jogadorAtual == 0 else ("Computador" if modoDeJogo == 2 else "Jogador 2")
    print(f'{vencedor} ganhou! 🎉')

# ---------------------- POSICIONAMENTO ---------------------
def validarPosicao(tabuleiro, coord1, coord2, barcos_restantes):
    """
    Função de validação para poscionamento dos barcos.
    """
    linha1, col1 = coord1
    linha2, col2 = coord2

    # precisa ser em linha reta
    if linha1 != linha2 and col1 != col2:
        return False, "❌ O barco deve estar em linha reta (horizontal ou vertical).", None

    # tamanho
    tamanho = abs(linha2 - linha1 + col2 - col1) + 1

    if tamanho not in barcos_restantes or barcos_restantes[tamanho] == 0:
        return False, f"❌ Você não pode posicionar mais barcos de {tamanho} casas.", None

    # sobreposição
    if linha1 == linha2:  # horizontal
        for col in range(min(col1, col2), max(col1, col2)+1):
            if tabuleiro[linha1][col] != '🌊':
                return False, "🚫 Já existe um barco nessa posição.", None
    else:  # vertical
        for lin in range(min(linha1, linha2), max(linha1, linha2)+1):
            if tabuleiro[lin][col1] != '🌊':
                return False, "🚫 Já existe um barco nessa posição.", None

    return True, "✅ Posição válida.", tamanho

def posicionarBarcos(estado, jogador):
    """
    Função com um loop verificando se a barcos para receber entrada e posicionar barcos nos tabuleiros do usuario
    """
    while sum(estado["barcos_por_jogador"][jogador].values()) > 0:
        exibirTabuleiro(estado, jogador, ocultar=False)
        print(f'\n Jogador {jogador+1} coloque seus barcos no tabuleiro!')
        print("📦 Barcos restantes:")
        for tamanho, qtd in estado["barcos_por_jogador"][jogador].items():
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
        if not coord1 or not coord2:
            print("❌ Coordenadas inválidas.")
            input('\nAperte ⏎ Enter para continuar.')
            continue

        valido, msg, tamanho = validarPosicao(
            estado["tabuleiros"][jogador], coord1, coord2, estado["barcos_por_jogador"][jogador]
        )
        if not valido:
            print(msg)
            input('\nAperte ⏎ Enter para continuar.')
            continue

        # posiciona
        linha1, col1 = coord1
        linha2, col2 = coord2
        if linha1 == linha2:
            for col in range(min(col1, col2), max(col1, col2)+1):
                estado["tabuleiros"][jogador][linha1][col] = '🚢'
        else:
            for lin in range(min(linha1, linha2), max(linha1, linha2)+1):
                estado["tabuleiros"][jogador][lin][col1] = '🚢'

        estado["barcos_por_jogador"][jogador][tamanho] -= 1

    print(f"\n✅ Jogador {jogador + 1}, todos os barcos foram posicionados!\n")
    input("Aperte ⏎ para continuar.")
    limparTerminal()

def posicionarBarcosMaquina(estado, jogador):
    """
    Função para maquina (Não exibe no terminal) com um loop verificando se a barcos para receber entrada e posicionar barcos nos tabuleiros do usuario
    """
    while sum(estado["barcos_por_jogador"][jogador].values()) > 0:
        tamanho_aleatorio = random.choice(
            [t for t, q in estado["barcos_por_jogador"][jogador].items() if q > 0]
        )
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

        valido, _, tamanho = validarPosicao(
            estado["tabuleiros"][jogador], coord1, coord2, estado["barcos_por_jogador"][jogador]
        )
        if not valido:
            continue

        # posiciona
        linha1, col1 = coord1
        linha2, col2 = coord2
        if linha1 == linha2:
            for col in range(col1, col2 + 1):
                estado["tabuleiros"][jogador][linha1][col] = '🚢'
        else:
            for lin in range(linha1, linha2 + 1):
                estado["tabuleiros"][jogador][lin][col1] = '🚢'

        estado["barcos_por_jogador"][jogador][tamanho] -= 1

# ---------------------- IA / MÁQUINA ----------------------
def tiroAleatorio():
    """
    Função gerando cordenas aleatorias para maquina
    """
    return (random.randint(0, 7), random.randint(0, 7))

def maquina(jogadas_certas, jogadas_erradas):
    """
    Função para deixar maquina "Inteligente", cria lista com jogadas proximas se houver acerto.
    Retorna um tiro aleatorio.
    """
    tiro = None
    if jogadas_certas:
        ultima = jogadas_certas[-1]
        opcoes = [
            (ultima[0] - 1, ultima[1]), #esquerda
            (ultima[0] + 1, ultima[1]), #direita
            (ultima[0], ultima[1] - 1), #cima
            (ultima[0], ultima[1] + 1)  #baixo
        ]
        tiros_validos = [
            op for op in opcoes
            if 0 <= op[0] <= 7 and 0 <= op[1] <= 7 and op not in jogadas_certas and op not in jogadas_erradas
        ]
        if tiros_validos:
            tiro = random.choice(tiros_validos)

    if not tiro:
        tiro = tiroAleatorio()
        while tiro in jogadas_certas or tiro in jogadas_erradas:
            tiro = tiroAleatorio()

    return tiro

# ---------------------- ORQUESTRAÇÃO ----------------------
def jogar(estado, modoDeJogo):
    """
    Função para roda o jogo, sorteia jogadores, posiciona barcos e alterna turno. 
    """
    jogadorAtual = sortearJogadores(modoDeJogo)

    if modoDeJogo == 2:
        for _ in range(2):
            if jogadorAtual == 1:
                posicionarBarcosMaquina(estado, jogadorAtual)
            else:
                posicionarBarcos(estado, jogadorAtual)
            jogadorAtual = alternarJogador(jogadorAtual)
    else:
        for _ in range(2):
            posicionarBarcos(estado, jogadorAtual)
            jogadorAtual = alternarJogador(jogadorAtual)

    alternarTurno(estado, jogadorAtual, modoDeJogo)

def menu(estado):
    """
    Exibe menu e recebe entrada com validação.
    """
    while True:
        limparTerminal()
        print('---------------------------------------------')
        print('----------------BATALHA NAVAL----------------')
        print('---------------------------------------------\n')
        print('Escolha uma das opções: ')
        print('1. Jogar contra amigos')
        print('2. Jogar contra a máquina')
        print('3. Regras')
        print('4. Sair do jogo')

        # entrada menu
        resposta = None
        while True:
            try:
                resposta = int(input('\nR: '))
                if resposta in (1, 2, 3, 4):
                    break
                else:
                    print('Digite apenas números entre 1 e 4.')
            except ValueError:
                print('Digite apenas números inteiros')

        if resposta in (1, 2):
            jogar(estado, resposta)
            return  # volta para main após término da partida
        elif resposta == 3:
            mostrarRegras(estado)
            # loop continua e redesenha o menu
        else:
            return  # sair

def main():
    while True:
        estado = criarEstado()
        criarNovosTabuleiros(estado)

        menu(estado)

        print('\n\n---------------------------------------------')
        print('-----------------FIM DE JOGO-----------------')
        print('---------------------------------------------\n')
        entrada = input('Quer jogar novamente? ("sim" / "não"): ').strip().lower()
        if entrada in ("sim", "s"):
            continue
        elif entrada in ("não", "nao", "n"):
            break
        else:
            print('Resposta não reconhecida, encerrando...')
            break

main()
