def display_scores(players):
    for player in enumerate(players):
        print(f"Player {player[0] + 1} has {player[1]} points.")
    print()


def display_rules():
    print("Each player rolls a dice.")
    print("Number from 2 to 6 is the amount of points they get.")
    print("If a player rolls 1 - they lose all points acumulated during this turn. The turn ends.")
    print("At any point during their turn a player may choose to stop rolling, saving their points and passing the turn on to the next player.")
    print("The game goes on for the agreed beforehand amount of rounds.")
    print("The player who has the most points by the end of the game is the winner.")
    print()


def display_commands():
    print("help - see list of available commands")
    print("scores - see players' scores")
    print("rules - read rules of the game")
    print("roll - roll the dice")
    print("stop - end turn")
    print()


def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Unexpected input")
