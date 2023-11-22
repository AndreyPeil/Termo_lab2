# Jogo "Termo". 
# Trabalho para faculdade, formação em Sistemas de Informação.
# Por Andrey Ricardo Lucca Peil e Otávio Ferreira Dahlke.

## Módulo: Main
'main.py'
### Função -> Main
'main()'
### Função -> Start Game
'start_game()'
### Função -> Game Settings
'game_settings()'
### Função -> Clear Screen
'clear_screen()'

## Módulo: Termo Game
'termo_game.py'
### Função -> Termo Main
'termo_main(gamemode)'
### Função -> Solo, Dueto e Quarteto
'solo(words_used, possible_words, termo_words)' 

'dueto(words_used, possible_words, termo_words)' 

'quarteto(words_used, possible_words, termo_words)'

## Módulo: Termo Raffle
'termo_raffle.py'
### Função -> Word of the Run
'word_of_the_run(gamemode)'

## Módulo: Valid Check
'valid_check.py'
### Função -> Player Input Validation
'player_input_validation(player_input, words_used, possible_words)'

## Módulo: Termo Gameplay
'termo_gameplay.py'
### Função -> Compare
'compare(player_input, word)'
### Função -> Credits
'credits(game_win, termo_attempts, termo_words)'

## Arquivo de Texto: Palavras Termo
> Arquivo que contém as palavras a serem sorteadas no jogo.

> São 9871 palavras de 5 letras que não contêm acentuação.

> Manipulação do Arquivo: Termo Raffle -> Word of the Run -> Linha 4.

## Arquivo de Texto: Palavras já Sorteadas
> Arquivo que contém as palavras que já foram sorteadas, começa vazio e é preenchido de acordo com as vitórias do jogador.

> Pode ser resetado no menu de escolha de modo de jogo.

> Manipulação do Arquivo: Main -> Main -> Start Game -> Game Settings -> Linha 22.

> Termo Game -> Termo Main -> Solo -> Linha 19.

> Termo Game -> Termo Main -> Dueto -> Linha 48.

> Termo Game -> Termo Main -> Quarteto -> Linha 78.

> Termo Raffle -> Word of the Run -> Linha 5.
