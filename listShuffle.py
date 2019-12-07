# listShuffle.py
# Shuffling a list randomly.
# Kristal Dow 12/7/2019

from random import randrange

def shuffle (myList):
    shuffledList = []
    
    for i in range(len(myList)):
        itemToMove = randrange(0, len(myList))
        shuffledList.append(myList[itemToMove])
        myList.pop(itemToMove)
        
    return shuffledList


def main():
    firstList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    print (shuffle(firstList))

main()
