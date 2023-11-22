# Sistema inspirado no jogo _Termo_. 

**Trabalho para faculdade, formação em Sistemas de Informação.**

**Por Andrey Ricardo Lucca Peil e Otávio Ferreira Dahlke.**

## Módulo: `Main`
> Módulo que inicia o programa e contém o menu de escolha de modo de jogo.

> Contém as funções `main`, `start_game`, `clear_screen` e `game_settings` e os imports do módulo `termo_game` do programa e `os` da biblioteca do Python.
### Função -> `Main`
> Inicia o programa chamando a função `start_game`.

> Chamadas: `Main` -> Linha 38. 
### Função -> `Start Game`
> Chama a função `game_settings`, que contém o menu de escolha de modo de jogo.

> Loop while que quebra caso o usuário digite um número diferente de 1, 2 ou 3 (correspondem aos modos de jogo) e sai do jogo.

> Chama a função `termo_main` do módulo `termo_game` mandando como parâmetro a variável `gamemode`.

>  Chamadas: `Main` -> `Main` -> Linha 37.
### Função -> `Game Settings`
> Chama a função `clear_screen` para limpar a tela do terminal.

> Imprime o menu no terminal com 5 opções.

> 1, 2 ou 3 escolhem um dos modos de jogo (Solo, Dueto e Quarteto, respectivamente) e continuam a execução padrão do código.

> Como dito no menu, caso o usuário digite um número ou símbolo e cause um ValueError ele é levado a tela de reset do arquivo `palavras_já_sorteadas.txt`, onde caso ele digite "Y" o arquivo é resetado e qualquer outro valor digitado mantém o arquivo como está.

> Qualquer outro número inteiro leva a saída do jogo quebrando o loop while presente em `start_game`.

> Chamadas: `Main` -> `Main` -> `Start Game` -> Linha 30.
### Função -> `Clear Screen`
> Limpa a tela do terminal caso chamada.

> Chamadas: `Main` -> `Main` -> `Start Game` -> `Game Settings` -> Linha 6.

## Módulo: `Termo Game`
> Módulo que chama todas as funções necessárias (no número de vezes necessárias) para o andamento do jogo.

> Contém as funções `termo_main`, `solo`, `dueto` e `quarteto` e os imports dos seguintes módulos do programa: `termo_raffle`, `valid_check` e `termo_gameplay`.

> Imports: `Main`.
### Função -> `Termo Main`
> Inicializa `words_used` que será usada no módulo `valid_check`.

> Chama a função `word_of_the_run` do módulo `termo_raffle` mandando `gamemode` (o modo de jogo escolhido) como parâmetro e recebendo `termo_words` (as palavras sorteadas) e `possible_words` (as palavras possíveis).

> Dependendo do valor de `gamemode` chama uma das funções que veremos abaixo para prosseguir com a execução do jogo.

> Chamadas: `Main` -> `Main` -> `Start Game` -> Linha 35.
### Função -> `Solo`, `Dueto` e `Quarteto`
> Todas essas funções recebem os mesmos parâmetros, `words_used` (lista vazia que será preenchida com as palavras escritas pelo jogador para uso no módulo `valid_check`), `possible_words` e `termo_words` (Lista com 1 string em `solo`, 2 em `dueto` e 4 em `quarteto`).

> As variáveis `termo_attempts` (contador de tentativas) e `loss_pass` são inicializadas. Em `dueto` e `quarteto` também é iniciada `termo_success` (contador de acertos).

> Loop while que utiliza o contador de tentativas `termo_attempts` (6 em `solo`, 7 em `dueto` e 9 em `quarteto`) que é incrementado após a palavra digitada passar a verificação, ser comparada a sorteada e ser adicionada a lista de palavras usadas.

> Input do player passa pela verificação, caso falhe, uma mensagem é imprimida no terminal e é pedido o input novamente, caso não dê problema, continua a execução padrão do código.

> Chama a função `compare` do módulo `termo_gameplay` (é chamada 2 e 4 vezes em `dueto` e `quarteto`, respectivamente) e adiciona a palavra a lista de palavras usadas `words_used`.

> Caso o jogador acerte uma das palavras em `dueto` e `quarteto`, a variável `termo_success` é incrementada.

> Quando o jogador ganha o jogo (em `solo`, acerta a palavra, em `dueto` e `quarteto` a variável `termo_success` chega a 2 e 4), a(s) palavra(s) é/são escrita(s) (append) no arquivo `palavras_já_sorteadas.txt` para não serem sorteadas de novo, True é atribuído a variável `loss_pass` (para que quando seja quebrado o while não seja chamada a função `credits` de novo), é chamada a função `credits` do módulo `termo_gameplay` mandando True, `termo_attempts` e `termo_words` e, por fim, é quebrado o while atribuindo 10 a `termo_attempts`.

> Quando o jogador esgota as tentativas sem acertar a(s) palavra(s), ela(s) não é/são adicionada(s) a `palavras_já_sorteadas.txt` e `loss_pass` ainda é False e ele é mandado para `credits` com False como parâmetro ao invés de True.
  
> Chamadas: `Solo`: `Termo Game` -> `Termo Main` -> Linha 93.

> `Dueto`: `Termo Game` -> `Termo Main` -> Linha 95.

> `Quarteto`: `Termo Game` -> `Termo Main` -> Linha 97.

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

> Evita que seja usada a mesma palavra mais de uma vez, verificando se ela está na lista `words_used`, servindo como conveniência ao jogador e uma prevenção para que não possa ganhar o `Dueto` e o `Quarteto` apenas digitando a mesma palavra 2 ou 4 vezes, respectivamente.

> Utilizando a função isalpha() do Python, verifica se as letras estão no alfabeto, para garantir que não são números ou símbolos.

> Verifica se a palavra não está entre as palavras possíveis (`possible_words`), serve para o funcionamento normal do jogo e para garantir que o usuário não digite palavras que contêm acentuação.

> Chamadas: `Termo Game` -> `Termo Main` -> `Solo` -> Linha 10.

> `Termo Game` -> `Termo Main` -> `Dueto` -> Linha 36.

> `Termo Game` -> `Termo Main` -> `Quarteto` -> Linha 66.

## Módulo: `Termo Gameplay`
> Módulo que contém e executa o principal elemento de uma jogatina de Termo, comparar a palavra sorteada com a palavra que o jogador digita e vê o quão próximo ele está de acertá-lá junto dos "créditos" que representam uma tela de fim de jogo.

> Imports: `Termo Game`.
### Função -> `Compare`
> Recebe o input do player `player_input` e a palavra a ser comparada `word` e torna elas em listas de 5 letras.

> Inicializa uma lista chamada `answer_list` com 5 strings `miss`.

> Compara cada letra do input com a respectiva letra na palavra sorteada (1 com 1, 2 com 2...), caso sejam iguais, o `miss` do `answer_list` no mesmo index dessas letras se torna um `green` e elas são substituídas com um "0" e "" em `player_input_list` e `termo_list` respectivamente para retirá-las das próximas comparações e não dar erros (qualquer valor que não é uma letra do alfabeto serve contanto que eles sejam diferentes em cada lista -> "0" != "").

>

Chamadas: `Termo Game` -> `Termo Main` -> `Solo` -> Linha 15.

`Termo Game` -> `Termo Main` -> `Dueto` -> Linha 42.

`Termo Game` -> `Termo Main` -> `Quarteto` -> Linha 72.
### Função -> `Credits`
> Em vitórias, `game_win` será True, e por isso será imprimida uma mensagem de vitória, parabenizando o jogador, mostrando quantas tentativas ele levou para acertar por meio de `termo_attempts` e quais eram as palavras. Enter retorna o usuário ao menu de escolha de jogo `game_settings`.

> Em derrotas, `game_win` será False, e por isso será imprimida uma mensagem de derrota e apenas serão mostrada as palavras do jogo. Enter retorna o usuário ao menu de escolha de jogo `game_settings`.

> Chamadas: `Termo Game` -> `Termo Main` -> `Solo` -> Linha 23.

> `Termo Game` -> `Termo Main` -> `Solo` -> Linha 28.

> `Termo Game` -> `Termo Main` -> `Dueto` -> Linha 53.

> `Termo Game` -> `Termo Main` -> `Dueto` -> Linha 58.

> `Termo Game` -> `Termo Main` -> `Quarteto` -> Linha 83.

> `Termo Game` -> `Termo Main` -> `Quarteto` -> Linha 88.

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
