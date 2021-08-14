#  BarView - Roll The Dice

from Bin import *
from Constants import *

class BarView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel

        self.oBinsDict = {}
        # Possible rolls only go from 2 to 12
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            oBin = Bin(self.window, rollTotal)
            self.oBinsDict[rollTotal] = oBin

    def update(self):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            thisResult = resultsDict[rollTotal]
            thisPercent = percentsDict[rollTotal]
            oBin = self.oBinsDict[rollTotal]
            oBin.update(nRounds, thisResult, thisPercent)

    def draw(self):
        for oBin in self.oBinsDict.values():
            oBin.draw()
