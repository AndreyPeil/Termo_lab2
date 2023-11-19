import termo_raffle
import valid_check
def solo(words_used, possible_words, termo_words):
    termo_attempts = 0
    while termo_attempts < 6:
        while True:
            player_input = input(">> ").lower()
            check = valid_check.player_input_validation(player_input, words_used, possible_words)
            if check == False:
                pass
            else:
                break
        words_used.append(player_input)
        termo_attempts += 1
def dueto(words_used, possible_words, termo_words):
    termo_attempts = 0
    while termo_attempts < 7:
        while True:
            player_input = input(">> ").lower()
            check = valid_check.player_input_validation(player_input, words_used, possible_words)
            if check == False:
                pass
            else:
                break
        words_used.append(player_input)
        termo_attempts += 1
def quarteto(words_used, possible_words, termo_words):
    termo_attempts = 0
    while termo_attempts < 9:
        while True:
            player_input = input(">> ").lower()
            check = valid_check.player_input_validation(player_input, words_used, possible_words)
            if check == False:
                pass
            else:
                break
        words_used.append(player_input)
        termo_attempts += 1
def credits():
    party_popper = "\U0001F389"
    applause = "\U0001F44F"
    print(f"CONGRATULATIONS! {applause} {party_popper}")
def termo(gamemode):
    words_used = []
    termo_words, possible_words = termo_raffle.word_of_the_run(gamemode)
    if gamemode == 1:
        solo(words_used, possible_words, termo_words)
    elif gamemode == 2:
        dueto(words_used, possible_words, termo_words)
    elif gamemode == 3:
        quarteto(words_used, possible_words, termo_words)
    else:
        print("Goodybye, friend, see you another time!")
