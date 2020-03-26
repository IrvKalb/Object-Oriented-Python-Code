# Card Class

import pygame
import pygwidgets

class Card():

    BACK_OF_CARD_IMAGE = pygame.image.load('images/backOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value
        fileName = 'images/' + self.cardName + '.png'
        self.images = pygwidgets.ImageCollection(window, (0, 0), \
                        {'front': fileName, 'back': Card.BACK_OF_CARD_IMAGE}, 'back')
        self.x = 0  # some starting pos, use setLoc below to change
        self.y = 0

        self.conceal()

    def conceal(self):
        self.faceUp = False
        self.images.replace('back')

    def reveal(self):
        self.faceUp = True
        self.images.replace('front')

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def setLoc(self, loc): # use inherited
        self.images.setLoc(loc)

    def getLoc(self):  # return loc as a tuple
        return((self.x, self.y))

    def draw(self):
        self.images.draw()

