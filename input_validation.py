def player_input_validation(player_input,words_used):
    if len(player_input) != 5:
        print("Word must have 5 letters.")
        return False
    elif player_input in words_used:
        print("Word prevented from being used twice.")
