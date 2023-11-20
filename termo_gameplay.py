def credits(game_win):
    if game_win == True:
        party_popper = "\U0001F389"
        applause = "\U0001F44F"
        print(f"CONGRATULATIONS! {applause} {party_popper}")
        play_again = input("Play again? [Press ""Y""]").upper()
        if play_again == "Y":
            import main
            main.main()
    else:
        print("You lose, try again next time.")
        play_again = input("Play again? [Press ""Y""]").upper()
        if play_again == "Y":
            import main
            main.main()