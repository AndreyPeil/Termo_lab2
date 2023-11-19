import termo_raffle
import input_validation
def solo(words_used,termo_words):
    termo_attempts = 0
    while termo_attempts < 6:
        while True:
            player_input = input(">> ")
            check = input_validation.player_input_validation(player_input,words_used)
            if check == False:
                pass
            else:
                break
def dueto():
    pass
def quarteto():
    pass
def termo(gamemode):
    words_used = []
    termo_words = termo_raffle.word_of_the_run(gamemode)
    if gamemode == 1:
        solo(words_used,termo_words)
    elif gamemode == 2:
        dueto()
    elif gamemode == 3:
        quarteto()
    else:
        print("Goodybye, friend, see you another time!")
