#  Roll Them Dice

import pygame
import pygwidgets

MAX_BAR_HEIGHT = 300
BAR_BOTTOM = 420
BAR_WIDTH = 30
BAR_COLOR = (128, 128, 128)
COLUMN_LEFT_START = -20
COLUMN_OFFSET = 60

# Bin Class
class Bin():
    def __init__(self, window, binNumber):
        self.window = window
        self.pixelsPerCount = MAX_BAR_HEIGHT

        self.left = COLUMN_LEFT_START + (binNumber * COLUMN_OFFSET)
        self.oBinLabel = pygwidgets.DisplayText(window,
                                (self.left + 3, BAR_BOTTOM + 12), binNumber,
                                fontName='arial', fontSize=24, width=25, justified='center')
        self.oBinCount = pygwidgets.DisplayText(window,
                                (self.left - 5, BAR_BOTTOM + 40), '',
                                fontName='arial', fontSize=18, width=45, justified='center')
        self.oBinPercent = pygwidgets.DisplayText(window,
                                (self.left - 5, BAR_BOTTOM + 60), '',
                                 fontName='arial', fontSize=18, width=50, justified='center')

    def update(self, nRounds, count):
        self.count = count
        self.oBinCount.setValue(count)
        percent = int((count / nRounds) * 100)
        self.oBinPercent.setValue(format(percent, '.1f') + '%')

        # force float here, use int when drawing rects
        # Calculate the real height, multiply by two to make it look better
        # All bars will certainly be less than 50%
        self.nPixelsPerTrial = float(MAX_BAR_HEIGHT)  / nRounds
        barHeight = int(count * self.nPixelsPerTrial)  * 2
        self.rect = pygame.Rect(self.left, BAR_BOTTOM - barHeight, BAR_WIDTH, barHeight)

    def draw(self):
        pygame.draw.rect(self.window, BAR_COLOR, self.rect, 0)
        self.oBinLabel.draw()
        self.oBinCount.draw()
        self.oBinPercent.draw()