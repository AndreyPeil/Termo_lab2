import termo_game
import os
def clear_screen():
    # Clear the terminal screen for various operating systems #
    os.system('cls' if os.name == 'nt' else 'clear')
def game_settings():
    clear_screen()
    # Termo, Dueto or Quarteto / Game choice #
    print('TERMO\n')
    print('Choose the game you wish to play:')
    print('1 - Solo')
    print('2 - Dueto')
    print('3 - Quarteto')
    print("Any other number to exit.")
    while True:
        try:
            gamemode = input("What game do you want to play? ")
            return gamemode
        except ValueError:
            print('Please, type a valid option!')
def main():
    gamemode = game_settings()
    termo_game.termo(gamemode)
main()
