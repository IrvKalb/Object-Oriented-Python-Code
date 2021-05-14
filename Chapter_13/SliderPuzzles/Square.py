# Square class

import pygame
from Constants import *
from Tile import *

class Square():
    '''
    A Square is a square area of the game board, in the application window.
    Each square has a location, rectangle, a tuple of legal moves, and a
    Tile that is drawn on the Square.  For each user move, the game tells
    the clicked on Square to exchange its Tile with the blank (empty space) Square.
    '''

    def __init__(self, window, left, top, squareNumber, legalMovesTuple):
        self.window = window
        self.rect = pygame.Rect(left, top, SQUARE_WIDTH, SQUARE_HEIGHT)
        self.squareNumber = squareNumber
        self.legalMovesTuple = legalMovesTuple
        self.loc = (left, top)
        self.reset()

    def reset(self):
        # Create starting Tile associated with this Square
        self.oTile = Tile(self.window, self.squareNumber)

    def isTileInProperPlace(self):
        tileNumber = self.oTile.getTileNumber()
        return (self.squareNumber == tileNumber)

    def getLegalMoves(self):
        return self.legalMovesTuple

    def clickedInside(self, mouseLoc):
        hit = self.rect.collidepoint(mouseLoc)
        return hit

    def getSquareNumber(self):
        return self.squareNumber

    def switch(self, oOtherSquare):
        # Switch the Tiles associated with two Square objects
        self.oTile, oOtherSquare.oTile = oOtherSquare.oTile, self.oTile

    def draw(self):
        # Tell the Tile to draw at the Square's location
        self.oTile.draw(self.loc)
