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


inputlist = [1,4,3,6,2,62,68]
print(isSorted(inputlist))

while not isSorted(inputlist):
    newlist = bogo(inputlist)
    print(newlist)
    inputlist = newlist