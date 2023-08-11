import random

inputlist = [3,2,5,7,34,25,128,8]

def isSorted(l):
    assert len(l) > 0, "Input list must have at least 1 value"

    prev = l[0]
    for i in l:
        if i < prev:
            return False
        prev = i
    return True

def bozoOp(l):
    firstNum = random.randint(0, len(inputlist)-1)
    secondNum = firstNum
    while secondNum == firstNum:
        secondNum = random.randint(0, len(inputlist)-1)
    
    print(f"{firstNum}, {secondNum}")

    newlist = l
    temp = newlist[firstNum]
    newlist[firstNum] = newlist[secondNum]
    newlist[secondNum] = temp

    return newlist

def bozo(l):
    templist = l
    i = 0
    while not isSorted(templist):
        i += 1
        print(templist)
        templist = bozoOp(templist)
    print(templist)
    print(f"Iterations Required: {i}")

bozo(inputlist)
