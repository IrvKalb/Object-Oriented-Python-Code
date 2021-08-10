#  PieCView - Roll The Dice

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

class PieView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel
        self.legendFields = []
        y = 110
        # Create the legends (first two are not needed and not drawn)
        for index in range(0, MAX_TOTAL_PLUS_1):
            gray = GRAY_TUPLE[index]
            oLegendField = pygwidgets.DisplayText(window, (550, y),
                                        value=str(index), fontSize=32,
                                        textColor=gray)
            self.legendFields.append(oLegendField)
            y = y + 25 # vertical spacing

    def update(self, ):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()

        self.nRounds = nRounds
        self.resultsDict = resultsDict
        self.percentsDict = percentsDict
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            # Could use the count if we want to display it later
            #rollCount = resultsDict[index]
            percent = percentsDict[index]
            oLegendField = self.legendFields[index]

            # Build percent as a string with one decimal digit
            percent = '{:.1%}'.format(percent)
            oLegendField.setValue(str(index) + ':   ' + percent)

    def drawFilledArc(self, centerX, centerY, radius, degrees1, degrees2, color):
        """This method generates a list of points that are used to create
        a filled polygon representing an arc in the circle.  We'll use the
        angles passed in and a little trig to figure out the points in the arc
        """
        centerTuple = (centerX, centerY)
        nPointsToDraw = int(degrees2 - degrees1)
        # Both degrees parameters need to be converted to radians for calculating points
        radians1 = math.radians(degrees1)
        radians2 = math.radians(degrees2)
        radiansDiff = (radians2 - radians1)  / nPointsToDraw

        # Start and end with the center point of the circle
        pointsList = [centerTuple]
        # Determine the points on the edge of the arc
        for pointNumber in range(nPointsToDraw + 1):
            offset = pointNumber * radiansDiff
            x = centerX + (radius * math.cos(radians1 + offset))
            y = centerY + (radius * math.sin(radians1 + offset))
            pointsList.append((x, y))
        pointsList.append(centerTuple)

        pygame.gfxdraw.filled_polygon(self.window, pointsList, color)
        # If you would like black lines around each arc, uncomment the next line
        #pygame.gfxdraw.polygon(self.window, pointsList, BLACK)

    # Draw the slice of the pie (arc) for every roll total
    def draw(self):
        startAngle = 0.0
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            percent = self.percentsDict[index]
            endAngle = startAngle + (percent * 360)
            rgbColor = GRAY_TUPLE[index]
            self.drawFilledArc(CENTER_X, CENTER_Y, RADIUS, startAngle, endAngle, rgbColor)
            self.legendFields[index].draw()

            startAngle = endAngle  # set up for next wedge

        pygame.draw.circle(self.window, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)
