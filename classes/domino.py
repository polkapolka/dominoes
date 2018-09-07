#!/usr/bin/env python
"""
A basic class domino.
"""

class Domino(object):
    """
    Domino has two integer values between 0 and 6 inclusive.
    Domino has an orientation of (L)eft, (R)ight, or (V)ertical.
    This determines how the Domino is printed.
    If the orientation is (L)eft, then the higher value is on the left.
    If the orientation is (R)ight, then the higher value is on the right.
    If vertical, then the values are displayed on top of each other.
    """
    def __init__(self, *args):
        no_args = len(args)
        if no_args == 2:
            self.values = sorted(list(args))
            
        else:
            raise TypeError, Domino.__doc__
        if self.values[0] == self.values[1]:
            self.orientation = 'V'
        else:
            self.orientation = 'R'
    
    def __str__(self):
        if self.orientation == 'R':
            return "-----\n|%s|%s|\n-----\n " % (self.values[0], self.values[1])
        elif self.orientation == 'L':
            return "-----\n|%s|%s|\n-----\n " % (self.values[1], self.values[0])
        elif self.orientation == 'V':
            return " |%s| \n |-| \n |%s| \n " % (self.values[0], self.values[1])
        else:
            raise ValueError, "Incorrect orientation."
        


def main():
    print Domino(0,0)
    print Domino(0,1)
    print Domino(1,0)
    d = Domino(0,1)
    d.orientation = 'L'
    print d


if __name__ == '__main__':
    main()


"""
 |0| 
 |-| 
 |0| 

-----
|0|1|
-----

-----
|0|1|
-----

-----
|1|0|
-----

"""
