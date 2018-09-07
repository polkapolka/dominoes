#!/usr/bin/env python
"""
I don't actually know how to play dominoes. I am trying
to generate the rules I observe from playing the online
game at dominoes.playdrift.com

"""
import sys, os

if __name__ == '__main__':
    sys.path.insert(0, "..") 
else:                        
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import classes.domino_set as DS


def PrintScoreBoard(player_scores, board_score):
    """
    Display the score.
    """
    display = [[] for x in range(7)]
    for x in range(9):
        display[0] += '-----'
        display[1] += '     '
        display[5] += '     '
        display[6] += '-----'
    display[2] = ' ' * 14 + 'Dominoes Game' + ' ' * 14
    display[3] = ' ' * 5 
    for (i, x) in enumerate(player_scores):
        display[3] += 'Player%s Score: %s' % (i, x) + ' '*5
    display[4] = ' ' * 5 + 'Board Score: %s' % board_score
    print '\n'.join([''.join(d) for d in display])


def PrintDominoBoard(played_list):
    """
    This is honestly the hardest part of making this.
    """
    display = [[] for x in range(9)]
    temp = played_list[:] # independent copy of the list
    while temp: # continue until empty
        t = temp.pop(0)
        if t.orientation =='V':
            display[0] += '---'
            display[1] += '   '
            display[2] += '---'
            display[3] += '|%s|' % t.values[0]
            display[4] += '---'
            display[5] += '|%s|' % t.values[1]
            display[6] += '---'
            display[7] += '   '
            display[8] += '---'
        elif t.orientation =='R':
            display[0] += '-----'
            display[1] += '     '
            display[2] += '     '
            display[3] += '-----'
            display[4] += '|%s|%s|'% (t.values[0], t.values[1])
            display[5] += '-----'
            display[6] += '     '
            display[7] += '     '
            display[8] += '-----'
        elif t.orientation == 'L':
            display[0] += '-----'
            display[1] += '     '
            display[2] += '     '
            display[3] += '-----'
            display[4] += '|%s|%s|' % (t.values[1], t.values[0])
            display[5] += '-----'
            display[6] += '     '
            display[7] += '     '
            display[8] += '-----'
    for x in range(9-len(played_list)):
        display[0] += '-----'
        display[1] += '     '
        display[2] += '     '
        display[3] += '     '
        display[4] += '     '
        display[5] += '     '
        display[6] += '     '
        display[7] += '     '
        display[8] += '-----'
    print '\n'.join([''.join(d[::-1]) for d in display])
        


def PrintPlayerHand(hand):
    """
    Arbitrarily setting the size of the hand display to 14.
    """
    display = []
    display += ['\n']
    display += ['   %s   ' * 7 % tuple(range(1,8))]
    display += [''.join([' |%s|%s| ' % tuple(x.values) for x in hand[:8]])]
    display += display[0]
    display += ['   %s   ' * 7 % tuple([hex(x)[2].upper() for x in range(8,15)])]
    display += [''.join([' |%s|%s| ' % tuple(x.values) for x in hand[8:15]])]
    display += display[0]
    print '\n'.join(display)



def PlayDominoes():
    new_set = DS.DominoSet()
    board_score = 0
    player1 = new_set.DealHand(7)
    player2 = new_set.DealHand(7)
    player_scores = [0,0]
    played_dominoes = []
    while True:
        PrintScoreBoard(player_scores,board_score)
        PrintDominoBoard(played_dominoes)
        PrintPlayerHand(player2)
        try:
            play = int(raw_input("What letter will you play?\nEnter Number 1-7::::"))
        except:
            break
        played_dominoes += [player2[play-1]]
        player2 = player2[:play-1]+player2[play:]


def main():
    while True:
        print
        print "Playing a game of Dominoes!!"
        print
        print "Want to play?"
        print
        answer = raw_input("(Q)uit? \n    :")
        if answer.upper() == 'Q':
            break
        else:
            PlayDominoes()

if __name__ == '__main__':
    main()


"""
"""
