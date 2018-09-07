#!/usr/bin/env python
"""
A basic class domino_set.
A DominoSet has a 28 dominoes.
The DominoSet can deal, generate a hand.
"""
import domino
import random

DOMINO_MAX = 6 #Size of Domino Set

class DominoSet:
    def __init__(self):
        self.Dominoes = []
        for x in range(DOMINO_MAX +1):
            for y in range(DOMINO_MAX +1):
                self.Dominoes += [domino.Domino(x,y)]
    
    def __str__(self):
        ds_string = ''
        display = [(d.orientation, d.values) for d in self.Dominoes]
        ds_string += ''.join(['|%s|%s|'% (v[0],v[1]) for o,v in display if o !='V'])
        ds_string += '\n\n'
        ds_string += ''.join([" |%s| " % (v[0]) for o,v in display if o =='V']) +'\n'
        ds_string += ''.join([" |%s| " % (v[1]) for o,v in display if o =='V'])
        return ds_string

    def Deal(self):
        random.shuffle(self.Dominoes)
        return self.Dominoes.pop()

    def DealHand(self, hand_no):
        random.shuffle(self.Dominoes)
        return [self.Dominoes.pop() for x in range(hand_no)]
        



def main():
    DominoSet()
    print DominoSet()
    f = DominoSet()
    f.Deal()
    f.Deal()
    print f
    f.DealHand(5)
    print f
    

    

if __name__ =='__main__':
    main()
        
"""
"""
