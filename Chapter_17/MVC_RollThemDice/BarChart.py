#  BarChart - Irv Kalb


from Bin import *

class BarChart():
    def __init__(self, window):

        self.window = window

        self.oBinsList = []
        # Possible rolls only go from 2 to 12
        for diceTotalForBin in range(0, 13):
            oBin = Bin(self.window, diceTotalForBin)
            self.oBinsList.append(oBin)

    def update(self, nRounds, resultsDict):
        self.resultsDict = resultsDict
        for number, oBin in enumerate(self.oBinsList):
            if number >= 2:
                thisResult = resultsDict[number]
                oBin.update(nRounds, thisResult)

    def draw(self):
        for number, oBin in enumerate(self.oBinsList):
            if number >= 2:
                oBin.draw()
