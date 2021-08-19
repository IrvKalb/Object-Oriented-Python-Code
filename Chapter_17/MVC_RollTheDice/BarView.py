#  BarView - Roll The Dice

from Bin import *
from Constants import *

class BarView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel

        self.oRollTotal = pygwidgets.DisplayText(self.window, (50, 406), 'Roll total:',
                                                 fontName='arial', fontSize=16, justified='right', width=80)
        self.oCount = pygwidgets.DisplayText(self.window, (50, 441), 'Count:',
                                                 fontName='arial', fontSize=16, justified='right', width=80)
        self.oPercent = pygwidgets.DisplayText(self.window, (50, 471), 'Percent:',
                                                 fontName='arial', fontSize=16, justified='right', width=80)

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
        self.oRollTotal.draw()
        self.oCount.draw()
        self.oPercent.draw()
        for oBin in self.oBinsDict.values():
            oBin.draw()
