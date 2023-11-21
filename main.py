import termo_game
import os
def clear_screen():
    # Clear the terminal screen for various operating systems #
    os.system('cls' if os.name == 'nt' else 'clear')
def game_settings():
    clear_screen()
    # Termo, Dueto or Quarteto / Game choice or exit #
    print('TERMO\n')
    print('Choose the game you wish to play:')
    print('1 - Solo')
    print('2 - Dueto')
    print('3 - Quarteto')
    print('Type a letter or symbol to reset words played list.')
    print("Any other number to exit.")
    while True:
        try:
            gamemode = int(input("What game do you want to play? "))
            return gamemode
        except ValueError:
            print('This feature only has an impact after you played at least once.')
            reset = input("Do you wish to reset words so that they can appear again? [Press ""Y""] ").upper()
            if reset == "Y":
                reset_file = open("palavras_já_sorteadas.txt", "w")
                reset_file.write("")
                reset_file.close()
            else:
                pass
            input('Returning to option select. Press enter. ')
def start_game():
    while True:
        gamemode = game_settings()
        if gamemode != 1 and gamemode != 2 and gamemode != 3:
            print("Goodybye, friend, see you another time!")
            break
        else:
            termo_game.termo_main(gamemode)
def main():
    start_game()
main()
