# Sistema inspirado no jogo _Termo_. 

**Trabalho para faculdade, formação em Sistemas de Informação.**

**Por Andrey Ricardo Lucca Peil e Otávio Ferreira Dahlke.**

## Módulo: `Main`
main.py
### Função -> `Main`
'main()'
### Função -> `Start Game`
'start_game()'
### Função -> `Game Settings`
'game_settings()'
### Função -> `Clear Screen`
'clear_screen()'

## Módulo: `Termo Game`
'termo_game.py'
### Função -> `Termo Main`
'termo_main(gamemode)'
### Função -> `Solo`, `Dueto` e `Quarteto`
'solo(words_used, possible_words, termo_words)' 

'dueto(words_used, possible_words, termo_words)' 

'quarteto(words_used, possible_words, termo_words)'

## Módulo: `Termo Raffle`
> Módulo que faz o sorteio da(s) palavra(s) para o jogo.

> Contém a função `word_of_the_run` e o import do módulo `random` da biblioteca do Python.

> Imports: `Termo Game`.
### Função -> `Word of the Run`
> Recebe `gamemode` como parâmetro e lê os dados dos arquivos .txt, atribuindo eles a variáveis em forma de duas listas de strings.

> Utilizando `gamemode` determina quantas palavras devem ser sorteadas, atribuindo um valor entre 1, 2 e 4 a variável `draw_times`.

> Loop while que é executado enquanto o tamanho da lista `termo_words` for menor que a variável `draw_times` garantindo que o número certo de palavras seja sorteado.

> É sorteado um número entre 0 e 9871 (tamanho da lista `possible_words`) que é utilizado como índice para atribuir um valor da lista `possible_words` a variável `chosen_word`.

> Verifica se `chosen_word` já está na lista de palavras sorteadas ou palavras já jogadas (`termo_words` e `played_words`, respectivamente), caso não, adiciona ela a `termo_words`, caso esteja em uma delas, não é adicionada.

 > Fecha a ligação com os arquivos .txt e retorna a lista de palavras sorteadas (`termo_words`) e a lista de palavras possíveis (`possible_words`).

> Chamadas: `Termo Game` -> `Termo Main` -> Linha 91.

## Módulo: `Valid Check`
> Módulo que faz a validação do input do jogador.

> Contém apenas a função `player_input_validation`.

> Imports: `Termo Game`. 
### Função -> `Player Input Validation`
> Recebe `player_input`, `words_used` e `possible_words` como parâmetros e retorna True, apenas caso não falhe nenhuma verificação, ou False, no caso contrário.

> Verifica o tamanho da palavra, apenas podendo ter 5 letras nela conforme as regras do jogo.

> Evita que seja usada a mesma palavra mais de uma vez, verificando se ela está na lista `words_used`, servindo como conveniência ao jogador e uma prevenção para que não posso ganhar o `Dueto` e o `Quarteto` apenas digitando a mesma palavra 2 ou 4 vezes, respectivamente.

> Utilizando a função isalpha() do Python, verifica se as letras estão no alfabeto, para garantir que não são números ou símbolos.

> Verifica se a palavra não está entre as palavras possíveis (`possible_words`), serve para o funcionamento normal do jogo e para garantir que o usuário não digite palavras que contêm acentuação.

> Chamadas: > `Termo Game` -> `Termo Main` -> `Solo` -> Linha 10.

> `Termo Game` -> `Termo Main` -> `Dueto` -> Linha 36.

> `Termo Game` -> `Termo Main` -> `Quarteto` -> Linha 66.

## Módulo: `Termo Gameplay`
'termo_gameplay.py'
### Função -> `Compare`
'compare(player_input, word)'
### Função -> `Credits`
'credits(game_win, termo_attempts, termo_words)'

## Arquivo de Texto: `Palavras Termo`
> Arquivo que contém as palavras a serem sorteadas no jogo.

> São 9871 palavras de 5 letras que não contêm acentuação.

> Manipulação do Arquivo: `Termo Raffle` -> `Word of the Run` -> Linha 4.

## Arquivo de Texto: `Palavras já Sorteadas`
> Arquivo que contém as palavras que já foram sorteadas, começa vazio e é preenchido de acordo com as vitórias do jogador.

> Pode ser resetado no menu de escolha de modo de jogo.

> Manipulação do Arquivo: `Main` -> `Main` -> `Start Game` -> `Game Settings` -> Linha 22.

> `Termo Game` -> `Termo Main` -> `Solo` -> Linha 19.

> `Termo Game` -> `Termo Main` -> `Dueto` -> Linha 48.

> `Termo Game` -> `Termo Main` -> `Quarteto` -> Linha 78.

> `Termo Raffle` -> `Word of the Run` -> Linha 5.
