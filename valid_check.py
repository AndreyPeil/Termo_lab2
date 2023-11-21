def player_input_validation(player_input, words_used, possible_words):
    alphabet_check = player_input.isalpha()
    if len(player_input) != 5:
        print("Word must have 5 letters.")
        return False
    elif player_input in words_used:
        print("Word prevented from being used twice.")
        return False
    elif alphabet_check == False:
        print("Word can only contain letters from the BR Alphabet.")
        return alphabet_check
    elif player_input not in possible_words:
        print("Word not found in game data, make sure to not use accentuation marks.")
        return False
    else:
        return True
