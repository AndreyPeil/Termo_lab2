import random
def word_of_the_run(gamemode):
    termo_words = []
    termo_file = open("palavras_termo.txt", "r")
    possible_words = termo_file.read().splitlines()
    if gamemode == 3:
        draw_times = 4
    elif gamemode == 1 or gamemode == 2:
        draw_times = gamemode
    else:
        return False, False
    for i in range(draw_times):
        number_draw = random.randint(0,507)
        chosen_word = possible_words[number_draw]
        if chosen_word in termo_words:
            pass
        else:
            termo_words.append(chosen_word)
    termo_file.close()
    return termo_words, possible_words
