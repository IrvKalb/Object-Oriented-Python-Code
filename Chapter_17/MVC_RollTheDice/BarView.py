#  BarView - Roll The Dice

from Bin import *
from Constants import *

class BarView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel

        self.oBinsList = []
        # Possible rolls only go from 2 to 12
        for diceTotalForBin in range(0, MAX_TOTAL_PLUS_1):
            oBin = Bin(self.window, diceTotalForBin)
            self.oBinsList.append(oBin)

    def update(self):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()

        for rollTotal, oBin in enumerate(self.oBinsList):
            if rollTotal >= MIN_TOTAL:
                thisResult = resultsDict[rollTotal]
                thisPercent = percentsDict[rollTotal]
                oBin.update(nRounds, thisResult, thisPercent)

    def draw(self):
        for number, oBin in enumerate(self.oBinsList):
            if number >= MIN_TOTAL:
                oBin.draw()
