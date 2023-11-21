def compare(player_input, word):
    answer_list = ["miss","miss","miss","miss","miss"]
    termo_list = list(word)
    player_input_list = list(player_input) 
    for g in range(5):
        if termo_list[g] == player_input_list[g]:
            answer_list[g] = "green"
            termo_list[g] = ""
            player_input_list[g] = "0"
    for y in range(5):
        if answer_list[y] == "green":
            pass
        else:
            for w in range(5):
                if player_input_list[y] == termo_list[w]:
                    answer_list[y] = "yellow"
                    termo_list[w] = ""
                    player_input_list[y] = "0"
    correct_list = list(player_input)
    for answer in range(5):
        if answer_list[answer] == "green":
            print(f'\033[32m{correct_list[answer]} \033[0m', end='|')
        elif answer_list[answer] == "yellow":
            print(f'\033[33m{correct_list[answer]} \033[0m', end='|')
        else:
            print(f'\033[30m{correct_list[answer]} \033[0m', end='|')
    print()
def credits(game_win, termo_attempts):
    if game_win == True:
        party_popper = "\U0001F389"
        applause = "\U0001F44F"
        print(f"CONGRATULATIONS! {applause} {party_popper}")
        print(f"Attempts taken to win: {termo_attempts}")
        print("Group project by Andrey and Otavio.")
        input("Press enter to play again. ")
    else:
        print("You lose, try again next time.")
        print("Group project by Andrey and Otavio.")
        input("Press enter to play again. ")
