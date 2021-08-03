#  TextChart - Irv Kalb

import pygwidgets

class TextChart():
    def __init__(self, window):
        self.window = window
        self.oResultsDisplay = pygwidgets.DisplayText(self.window, (340, 180),
                                                      fontSize=36)

    def update(self, nRounds, resultsDict):
        self.resultsDict = resultsDict
        self.resultsText = ''
        for rollTotal in range(2, 13):
            count = self.resultsDict[rollTotal]
            percent = (count / nRounds) * 100
            percent = format(percent, '.1f') + '%'
            self.resultsText = self.resultsText + str(rollTotal) + ':   ' +\
                                        str(count) + '   ' + percent + '\n'

        self.oResultsDisplay.setValue(self.resultsText)

    def draw(self):
        self.oResultsDisplay.draw()
