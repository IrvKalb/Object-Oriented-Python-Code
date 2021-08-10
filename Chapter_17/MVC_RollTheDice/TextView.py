#  TextChart - Roll The Dice

import pygwidgets
from Constants import *

class TextView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel
        # Roll total text never changes - set it once, at the beginning
        #totalText = 'Total\n\n'
        #for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            #totalText = totalText + str(rollTotal) +'\n'

        totalText = ['Total', '']
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            totalText.append(str(rollTotal))
        self.oTotalDisplay = pygwidgets.DisplayText(self.window, (200, 135), totalText,
                                                      fontSize=36, width=100, justified='right')
        self.oCountDisplay = pygwidgets.DisplayText(self.window, (320, 135),
                                                      fontSize=36, width=100, justified='right')
        self.oPercentDisplay = pygwidgets.DisplayText(self.window, (440, 135),
                                                      fontSize=36, width=100, justified='right')

    def update(self):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()

        # countText = 'Count\n\n'
        # percentText = 'Percent\n\n'
        # for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
        #     count = resultsDict[rollTotal]
        #     percent = percentsDict[rollTotal]
        #
        #     countText = countText + str(count) + '\n'
        #     # Build percent as a string with one decimal digit
        #     percent = '{:.1%}'.format(percent)
        #     percentText = percentText + percent + '\n'

        countList = ['Count', ''] # extra empty string for a blank line
        percentList = ['Percent', '']
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            count = resultsDict[rollTotal]
            percent = percentsDict[rollTotal]

            countList.append(str(count))
            # Build percent as a string with one decimal digit
            percent = '{:.1%}'.format(percent)
            percentList.append(percent)

        self.oCountDisplay.setValue(countList)
        self.oPercentDisplay.setValue(percentList)

    def draw(self):
        self.oTotalDisplay.draw()
        self.oCountDisplay.draw()
        self.oPercentDisplay.draw()
