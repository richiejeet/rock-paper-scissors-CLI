import random
from pprint import pprint

def rpsCLI():
    moves = ['R', 'P', "S"]
    full = ['Rock', 'Paper', 'Scissor']

    players = {'H': 0, 'C': 0}

    y = input("Is player 1 a human? Y/N ")
    
    num = input("Max number of points to win? ")
    max_points = int(num)

    while (max_points not in players.values()):
        p1 = None
        if y == 'Y':
            ch = input("Rock [R], Paper[P], Scissor [S]? ")
            p1 = moves.index(ch)
        else:
            p1 = random.randint(0,2)
        p2 = random.randint(0,2)

        if p1 == p2:
            pprint("This round is a draw.")
            continue
        elif p1 == 0 and p2 == 1:
            players['C'] += 1
            pprint("Player 1 chose {} and Player 2 chose {}".format(full[p1], full[p2]))
            pprint("Paper beats rock!")
            pprint(players)
        elif p1 == 0 and p2 == 2:
            players['H'] += 1
            pprint("Player 1 chose {} and Player 2 chose {}".format(full[p1], full[p2]))
            pprint("Rock beats scissor!")
            pprint(players)
        elif p1 == 1 and p2 == 0:
            players['H'] += 1
            pprint("Player 1 chose {} and Player 2 chose {}".format(full[p1], full[p2]))
            pprint("Paper beats rock!")
            pprint(players)
        elif p1 == 1 and p2 == 2:
            players['C'] += 1
            pprint("Player 1 chose {} and Player 2 chose {}".format(full[p1], full[p2]))
            pprint("Scissor beats paper!")
            pprint(players)
        elif p1 == 2 and p2 == 0:
            players['C'] += 1
            pprint("Player 1 chose {} and Player 2 chose {}".format(full[p1], full[p2]))
            pprint("Rock beats scissor!")
            pprint(players)
        elif p1 == 2 and p2 == 1:
            players['H'] += 1
            pprint("Player 1 chose {} and Player 2 chose {}".format(full[p1], full[p2]))
            pprint("Scissor beats paper!")
            pprint(players)

    player1 = 'human' if y == 'Y' else 'computer'

    if players['H'] == max_points:
        pprint("Player 1 i.e. {} won!!!!". format(player1))
    else:
        pprint("Player 2 i.e. computer won!!!!")


if __name__ == '__main__':
    rpsCLI()
