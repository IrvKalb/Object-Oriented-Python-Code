#  BarChart - Roll The Dice

from Bin import *

class BarChart():
    def __init__(self, window):

        self.window = window

        self.oBinsList = []
        # Possible rolls only go from 2 to 12
        for diceTotalForBin in range(0, 13):
            oBin = Bin(self.window, diceTotalForBin)
            self.oBinsList.append(oBin)

    def update(self, nRounds, resultsDict, percentsDict):
        self.resultsDict = resultsDict
        self.percentsDict = percentsDict
        for rollTotal, oBin in enumerate(self.oBinsList):
            if rollTotal >= 2:
                thisResult = self.resultsDict[rollTotal]
                thisPercent = self.percentsDict[rollTotal]
                oBin.update(nRounds, thisResult, thisPercent)

    def draw(self):
        for number, oBin in enumerate(self.oBinsList):
            if number >= 2:
                oBin.draw()
