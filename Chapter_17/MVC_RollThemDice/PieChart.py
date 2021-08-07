#  BarChart - Irv Kalb

import pygame
import pygame.gfxdraw
import math
from pygwidgets import *
from Constants import *

CENTER_X = 300
CENTER_Y = 300
RADIUS = 200

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

GRAY_TUPLE = (GRAY2, GRAY3, GRAY4, GRAY5, GRAY6,
                     GRAY7, GRAY8, GRAY9, GRAY10, GRAY11, GRAY12)

class PieChart():
    def __init__(self, window):
        self.window = window
        self.legendFields = []
        y = 160
        for legendNumber in range(2, 13):
            gray = GRAY_TUPLE[legendNumber - 2]
            oLegendField = pygwidgets.DisplayText(window, (550, y),
                                        value=str(legendNumber), fontSize=32,
                                        textColor=gray)
            self.legendFields.append(oLegendField)
            y = y + 25 # vertical spacing

    def update(self, nRounds, resultsDict, percentsDict):
        self.nRounds = nRounds
        self.resultsDict = resultsDict
        self.percentsDict = percentsDict
        for rollTotal in range(2, 13):
            rollCount = resultsDict[rollTotal]
            percent = percentsDict[rollTotal]
            index = rollTotal - 2
            oLegendField = self.legendFields[index]

            # Build percent as a string with one decimal digit
            percent = '{:.1f}'.format(100 * percent) + '%'
            oLegendField.setValue(str(rollTotal) + ':   ' + percent)

    def degreesToRadians(self, nDegrees):
        nRadians = (math.pi / 180) * nDegrees
        return nRadians

    def drawFilledArc(self, centerX, centerY, radius, degrees1, degrees2, color):
        radians1 = self.degreesToRadians(degrees1)
        radians2 = self.degreesToRadians(degrees2)

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
        for rollTotal in range(2, 13):
            index = rollTotal - 2
            percent = self.percentsDict[rollTotal]
            endAngle = startAngle + round(percent * 360)
            rgbColor = GRAY_TUPLE[index]
            self.drawFilledArc(CENTER_X, CENTER_Y, RADIUS, startAngle, endAngle, rgbColor)
            self.legendFields[index].draw()

            startAngle = endAngle  # set up for next wedge

