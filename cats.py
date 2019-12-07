# cats.py
# A class that accrues cats in boxes and releases hounds to get rid of them.
# Kristal Dow 12/2/2019

from random import randrange

class Cats:

    def __init__(self, boxes):
        self.boxes = boxes
        self.value = 1

    def accrueCats(self):
        self.value = self.boxes+randrange(1, self.boxes+100)

    def releaseHounds(self, hounds):
        calcHounds = self.value / hounds
        self.value = int(round(calcHounds, 0))

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value  
