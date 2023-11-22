import termo_raffle
import valid_check
import termo_gameplay
def solo(words_used, possible_words, termo_words):
    termo_attempts = 0
    loss_pass = False
    while termo_attempts < 6:
        while True:
            player_input = input(">> ").lower()
            check = valid_check.player_input_validation(player_input, words_used, possible_words)
            if check == False:
                pass
            else:
                break
        termo_gameplay.compare(player_input, termo_words[0])
        words_used.append(player_input)
        termo_attempts += 1
        if player_input in termo_words:
            played_file = open("palavras_já_sorteadas.txt", "a")
            played_file.write(termo_words[0] + "\n")
            played_file.close()
            loss_pass = True
            termo_gameplay.credits(True, termo_attempts, termo_words)
            termo_attempts = 10
    if loss_pass == True:
        pass
    else:
        termo_gameplay.credits(False, termo_attempts, termo_words)
def dueto(words_used, possible_words, termo_words):
    termo_attempts = 0
    loss_pass = False
    termo_success = 0
    while termo_attempts < 7:
        while True:
            player_input = input(">> ").lower()
            check = valid_check.player_input_validation(player_input, words_used, possible_words)
            if check == False:
                pass
            else:
                break
        for word in range(2):
            termo_gameplay.compare(player_input, termo_words[word])
        words_used.append(player_input)
        termo_attempts += 1
        if player_input in termo_words:
            termo_success += 1
        if termo_success == 2:
            played_file = open("palavras_já_sorteadas.txt", "a")
            for word in range(2):
                played_file.write(termo_words[word] + "\n")
            played_file.close()
            loss_pass = True
            termo_gameplay.credits(True, termo_attempts, termo_words)
            termo_attempts = 10
    if loss_pass == True:
        pass
    else:
        termo_gameplay.credits(False, termo_attempts, termo_words)
def quarteto(words_used, possible_words, termo_words):
    termo_attempts = 0
    loss_pass = False
    termo_success = 0
    while termo_attempts < 9:
        while True:
            player_input = input(">> ").lower()
            check = valid_check.player_input_validation(player_input, words_used, possible_words)
            if check == False:
                pass
            else:
                break
        for word in range(4):
            termo_gameplay.compare(player_input, termo_words[word])
        words_used.append(player_input)
        termo_attempts += 1
        if player_input in termo_words:
            termo_success += 1
        if termo_success == 4:
            played_file = open("palavras_já_sorteadas.txt", "a")
            for word in range(4):
                played_file.write(termo_words[word] + "\n")
            played_file.close()
            loss_pass = True
            termo_gameplay.credits(True, termo_attempts, termo_words)
            termo_attempts = 10
    if loss_pass == True:
        pass
    else:
        termo_gameplay.credits(False, termo_attempts, termo_words)
def termo_main(gamemode):
    words_used = []
    termo_words, possible_words = termo_raffle.word_of_the_run(gamemode)
    if gamemode == 1:
        solo(words_used, possible_words, termo_words)
    elif gamemode == 2:
        dueto(words_used, possible_words, termo_words)
    elif gamemode == 3:
        quarteto(words_used, possible_words, termo_words)
