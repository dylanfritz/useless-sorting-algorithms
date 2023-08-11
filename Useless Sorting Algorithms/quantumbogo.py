import math
import random

def isSorted(l):
    assert len(l) > 0, "Input list must have at least 1 value"

    prev = l[0]
    for i in l:
        if i < prev:
            return False
        prev = i
    return True


def bogo(l):
    new = l
    random.shuffle(new)
    return new

def DESTROY_THE_EFFIN_UNIVERSE():
    return # Not quite sure how to implement this one yet...

inputlist = [1,4,3,6,2,62,68]

sortedlist = bogo(inputlist)

if not isSorted(sortedlist):
    print("Whoopsie")
    DESTROY_THE_EFFIN_UNIVERSE()
