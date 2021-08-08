#  TextChart - Roll The Dice

import pygwidgets

class TextChart():
    def __init__(self, window):
        self.window = window
        # Roll total text never changes - set it once, at the beginning
        totalText = 'Total\n\n'
        for rollTotal in range(2, 13):
            totalText = totalText + str(rollTotal) +'\n'
        self.oTotalDisplay = pygwidgets.DisplayText(self.window, (200, 135), totalText,
                                                      fontSize=36, width=100, justified='right')
        self.oCountDisplay = pygwidgets.DisplayText(self.window, (320, 135),
                                                      fontSize=36, width=100, justified='right')
        self.oPercentDisplay = pygwidgets.DisplayText(self.window, (440, 135),
                                                      fontSize=36, width=100, justified='right')

    def update(self, nRounds, resultsDict, percentsDict):
        countText = 'Count\n\n'
        percentText = 'Percent\n\n'
        for rollTotal in range(2, 13):
            count = resultsDict[rollTotal]
            percent = percentsDict[rollTotal]
            
            countText = countText + str(count) + '\n'
            # Build percent as a string with one decimal digit
            percent = '{:.1f}'.format(100 * percent) + '%'
            percentText = percentText + percent + '\n'

        self.oCountDisplay.setValue(countText)
        self.oPercentDisplay.setValue(percentText)

    def draw(self):
        self.oTotalDisplay.draw()
        self.oCountDisplay.draw()
        self.oPercentDisplay.draw()
