#  TextChart - Roll The Dice

import pygwidgets
from Constants import *

class TextView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel

        totalText = ['Roll total', '']
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            totalText.append(rollTotal)
        self.oTotalDisplay = pygwidgets.DisplayText(self.window, (200, 135), totalText,
                                                      fontSize=36, width=120, justified='right')
        self.oCountDisplay = pygwidgets.DisplayText(self.window, (320, 135),
                                                      fontSize=36, width=120, justified='right')
        self.oPercentDisplay = pygwidgets.DisplayText(self.window, (440, 135),
                                                      fontSize=36, width=120, justified='right')

    def update(self):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()

        countList = ['Count', ''] # extra empty string for a blank line
        percentList = ['Percent', '']
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            count = resultsDict[rollTotal]
            percent = percentsDict[rollTotal]

            countList.append(count)
            # Build percent as a string with one decimal digit
            percent = '{:.1%}'.format(percent)
            percentList.append(percent)

        self.oCountDisplay.setValue(countList)
        self.oPercentDisplay.setValue(percentList)

    def draw(self):
        self.oTotalDisplay.draw()
        self.oCountDisplay.draw()
        self.oPercentDisplay.draw()
