# Projeto Batalha Naval – Python (Console)

## 1. Identificação do Projeto
- **Nome do Projeto**: Batalha Naval – Python (Console)
- **Versão**: 1.0
- **Data**: 05.09.2025
- **Integrantes**: Felipe Ferrete, Gustavo Bosak, Nikolas Brisola

---

## 2. Descrição Geral
O projeto consiste em uma versão digital do tradicional jogo de tabuleiro **Batalha Naval**, implementado em Python e jogado diretamente no console.

O objetivo do jogo é permitir que os jogadores posicionem seus barcos em um tabuleiro 8x8 e tentem descobrir as posições do adversário por meio de jogadas sucessivas.

O jogo conta com um **menu inicial**, onde o usuário pode escolher entre:
- **Jogar contra outro jogador** (Humano x Humano)
- **Jogar contra a máquina** (Humano x Máquina)
- **Consultar as regras do jogo** antes de iniciar

A experiência foca na lógica do jogo, sem interface gráfica, mas com todas as funcionalidades básicas de posicionamento, sorteio inicial e jogabilidade interativa.

---

## 3. Regras do Jogo
1. O **jogador inicial** é definido por sorteio aleatório (**MatchRandom**).
2. Cada jogador possui um **tabuleiro de 8x8**, com linhas de A a H e colunas de 1 a 8.
3. O **posicionamento dos barcos** é manual, com escolha das coordenadas pelo jogador.
4. Os barcos **não podem se sobrepor** e devem ser posicionados apenas na horizontal ou vertical (não em diagonal).
5. **Tipos de barcos**:
   - 1 Grande → tamanho 4x1
   - 2 Médios → tamanho 3x1
   - 2 Pequenos → tamanho 2x1
   - 1 Minúsculo → tamanho 1x1
6. O jogador tem direito a **1 tentativa por rodada**. Caso acerte um barco inimigo, ganha o direito de jogar novamente.
7. O sistema realiza **validação das entradas**, garantindo que o jogador digite apenas coordenadas válidas.

---

## 4. Condições de Vitória / Derrota
- **Vitória**: Vence o jogador que conseguir destruir todos os barcos do adversário.
- **Derrota**: O jogo segue até que um dos lados seja derrotado.

---

## 5. Modos de Jogo
- **Humano x Humano**: Dois jogadores alternam suas jogadas no console.
- **Humano x Máquina**: A máquina realiza jogadas de forma totalmente aleatória. Mesmo quando acerta, sua próxima jogada também será randômica.

---

## 6. Extras e Limitações
- **Inteligência artificial**: A IA da máquina é básica, limitada a jogadas randômicas.
- **Interface**: O jogo funciona apenas no console, sem interface gráfica.

---

## 7. Considerações Finais
Este projeto tem como objetivo praticar a lógica de programação, uso de funções, controle de fluxo e manipulação de dados em Python.

Como possíveis melhorias futuras, seriam interessantes as seguintes implementações:
- **Interface gráfica**, utilizando bibliotecas como Tkinter ou Pygame.
- **Inteligência artificial mais avançada** para a máquina.
- **Multiplayer online**, para permitir que jogadores se enfrentem pela internet.

---

## 8. Como Executar

Para rodar o jogo, siga os passos abaixo:

### Pré-requisitos
Certifique-se de ter o Python 3.x instalado. Você pode verificar isso rodando o seguinte comando:

```bash
python --version

Passos para rodar o jogo:

Clone o repositório:

git clone https://github.com/seuusuario/batalha-naval.git


Navegue até o diretório do projeto:

cd batalha-naval


Execute o jogo:

python batalha_naval.py

9. Licença

Este projeto está licenciado sob a licença MIT – veja o arquivo LICENSE
 para mais detalhes.
