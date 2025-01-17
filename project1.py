#  a game of 'pig'

import utils
import random


def main():
    n_players = utils.int_input("How many players? ")
    n_rounds = utils.int_input("How many rounds? ")
    players = {}
    for i in range(n_players):
        players[i] = 0
    print()
    for round in range(n_rounds):
        for player_id in players.keys():
            points_this_round = 0
            print(f"Player {player_id + 1}, your turn.")
            while True:
                print("Type 'roll' to roll the dice. Type 'stop' to end the turn.")
                command = input()

                match command:
                    case "roll":
                        roll_score = random.randint(1,6)
                        if roll_score != 1:
                            points_this_round += roll_score
                            print(f"You rolled a {roll_score}. Right now you have {points_this_round} points.")
                        else:
                            print("You rolled a 1. You lose points gained this round and end the turn.")
                            print()
                            break
                    case "stop":
                        print(f"You collect {points_this_round} points and end the turn.\n")
                        players[player_id] += points_this_round
                        utils.display_scores(players.values())
                        break     
                    case "scores":
                        utils.display_scores(players.values())
                    case "rules":
                        utils.display_rules()
                    case "help":
                        utils.display_commands()
                    case _:
                        print(f"Unknown command {command}")

    print()
    print("Game over")
    utils.display_scores(players.values())


main()