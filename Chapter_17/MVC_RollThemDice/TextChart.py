#  TextChart - Irv Kalb

import pygwidgets

class TextChart():
    def __init__(self, window):
        self.window = window
        self.oResultsDisplay = pygwidgets.DisplayText(self.window, (300, 180),
                                                      fontSize=36)

    def update(self, nRounds, resultsDict, percentsDict):
        self.resultsDict = resultsDict
        self.resultsText = ''
        for rollTotal in range(2, 13):
            count = self.resultsDict[rollTotal]
            percent = percentsDict[rollTotal]

            # Build percent as a string with one decimal digit
            percent = '{:.1f}'.format(100 * percent) + '%'
            self.resultsText = self.resultsText + str(rollTotal) + ':   ' +\
                                        'count is ' + str(count) + '   ' + \
                                        percent + '\n'

        self.oResultsDisplay.setValue(self.resultsText)

    def draw(self):
        self.oResultsDisplay.draw()
