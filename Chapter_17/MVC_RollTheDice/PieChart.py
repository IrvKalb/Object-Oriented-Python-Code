#  PieChart - Roll The Dice

import pygame
import pygame.gfxdraw
import math
from pygwidgets import *
from Constants import *

CENTER_X = 300
CENTER_Y = 300
RADIUS = 200

GRAY0 = (0, 0, 0)  # not used
GRAY1 = (0, 0, 0)  # not used
GRAY2 = (40, 40, 40)
GRAY3 = (60, 60, 60)
GRAY4 = (80, 80, 80)
GRAY5 = (100, 100, 100)
GRAY6 = (120, 120, 120)
GRAY7 = (140, 140, 140)
GRAY8 = (160, 160, 160)
GRAY9 = (180, 180, 180)
GRAY10 = (200, 200, 200)
GRAY11 = (220, 220, 220)
GRAY12= (240, 240, 240)
BLACK = (0, 0, 0)

GRAY_TUPLE = (GRAY0, GRAY1,GRAY2, GRAY3, GRAY4, GRAY5, GRAY6,
                        GRAY7, GRAY8, GRAY9, GRAY10, GRAY11, GRAY12)

class PieChart():
    def __init__(self, window):
        self.window = window
        self.legendFields = []
        y = 110
        # Create 12 legends (first two are not needed and not drawn)
        for index in range(0, 13):
            gray = GRAY_TUPLE[index]
            oLegendField = pygwidgets.DisplayText(window, (550, y),
                                        value=str(index), fontSize=32,
                                        textColor=gray)
            self.legendFields.append(oLegendField)
            y = y + 25 # vertical spacing

    def update(self, nRounds, resultsDict, percentsDict):
        self.nRounds = nRounds
        self.resultsDict = resultsDict
        self.percentsDict = percentsDict
        for index in range(0, 13):
            if index >= 2:
                # Could use the count if we want to display it later
                #rollCount = resultsDict[index]
                percent = percentsDict[index]
                oLegendField = self.legendFields[index]

                # Build percent as a string with one decimal digit
                percent = '{:.1f}'.format(100 * percent) + '%'
                oLegendField.setValue(str(index) + ':   ' + percent)

    def drawFilledArc(self, centerX, centerY, radius, degrees1, degrees2, color):
        # Both degrees parameters need to be converted to radians for drawing
        radians1 = math.radians(degrees1)
        radians2 = math.radians(degrees2)

        nLines = 1000
        radiansDiff = (radians2 - radians1) / nLines
        centerTuple = (centerX, centerY)

        # Fill in the wedge
        for lineNum in range(nLines):
            x = centerX + (radius * math.cos(radians1 + (lineNum * radiansDiff)))
            y = centerY + (radius * math.sin(radians1 + (lineNum * radiansDiff)))
            pygame.draw.line(self.window, color, centerTuple, (x, y), 2)

        pygame.gfxdraw.pie(self.window, centerX, centerY, radius, degrees1, degrees2, BLACK)

    # Draw everything
    def draw(self):
        startAngle = 0
        for index in range(2, 13):
            if index >=2:
                percent = self.percentsDict[index]
                endAngle = startAngle + round(percent * 360)
                if index == 12:  # a little fudging to handle rounding errors
                    endAngle = 360
                rgbColor = GRAY_TUPLE[index]
                self.drawFilledArc(CENTER_X, CENTER_Y, RADIUS, startAngle, endAngle, rgbColor)
                self.legendFields[index].draw()

                startAngle = endAngle  # set up for next wedge

