#  View - Roll The Dice

from BarChart import *
from PieChart import *
from TextChart import *

# ViewDice Class
class ViewDice():
    def __init__(self, window, nRounds):
        self.window = window
        self.nRounds = nRounds

        # Instantiate different View objects
        self.oBarChart = BarChart(self.window)
        self.oPieChart = PieChart(self.window)
        self.oTextChart = TextChart(self.window)
        self.oView = self.oBarChart  # default to bar chart at start

        self.oBarButton = pygwidgets.TextRadioButton(window, (80, 540),
                                                     'View', 'Bar Chart', value=True, fontSize=36)
        self.oPieButton = pygwidgets.TextRadioButton(window, (340, 540),
                                                     'View', 'Pie Chart', fontSize=36)
        self.oTextButton = pygwidgets.TextRadioButton(window, (600, 540),
                                                      'View', 'Text Chart', fontSize=36)

    # Called when there is new data
    def update(self, nRounds, rollsDict):
        self.rollsDict = rollsDict
        self.percentsDict = {}
        # Calculate percentages
        for rollTotal, count in rollsDict.items():
            thisPercent = count / nRounds
            self.percentsDict[rollTotal] = thisPercent
            # Tell the current view to update itself
        self.oView.update(nRounds, self.rollsDict, self.percentsDict)

    # Check for button presses to change views
    def handleEvent(self, event):
        if self.oBarButton.handleEvent(event):
            self.oView = self.oBarChart
            self.oView.update(self.nRounds, self.rollsDict, self.percentsDict)
        elif self.oPieButton.handleEvent(event):
            self.oView = self.oPieChart
            self.oView.update(self.nRounds, self.rollsDict, self.percentsDict)
        elif self.oTextButton.handleEvent(event):
            self.oView = self.oTextChart
            self.oView.update(self.nRounds, self.rollsDict, self.percentsDict)

    def setNumberOfRounds(self, nRounds):
        self.nRounds = nRounds

    def draw(self):
        self.oBarButton.draw()
        self.oPieButton.draw()
        self.oTextButton.draw()
        # Pass the draw call on to the currently selected view.
        self.oView.draw()
