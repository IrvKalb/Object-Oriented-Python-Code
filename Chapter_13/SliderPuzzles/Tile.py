import pygame
from Constants import *

class Tile():
    '''
    A tile is a square of the game board, in the application window.
    Each tile has a location, rectangle, a tuple of legal moves, and
    the number and image showing on the tile.  As the game plays,
    for each move, we exchange the number and the image with the
    blank (empty) space.

    The following is a dict of tileNumber:tuple.  Each tuple contains all
    legal moves (vertical and horizontal neighbors) for each tile in the grid.
    For example, for Tile 0, only Tiles 1 and 4 are legal moves.
    '''

    LEGAL_MOVES_DICT = {
        0:(1, 4),
        1:(0, 2, 5),
        2:(1, 3, 6),
        3:(2, 7),
        4:(0, 5, 8),
        5:(1, 4, 6, 9),
        6:(2, 5, 7, 10),
        7:(3, 6, 11),
        8:(4, 9, 12),
        9:(5, 8, 10, 13),
        10:(6, 9, 11, 14),
        11:(7, 10, 15),
        12:(8, 13),
        13:(9, 12, 14),
        14:(10, 13, 15),
        15:(11, 14)}

    def __init__(self, window, left, top, tileNumber):
        self.window = window
        self.loc = (left, top)
        self.tileNumber = tileNumber
        self.legalMovesTuple = Tile.LEGAL_MOVES_DICT[self.tileNumber]
        self.rect = pygame.Rect(left, top, TILE_WIDTH, TILE_HEIGHT)

        font = pygame.font.SysFont(None, 60)

        # Use drawing calls to create a surface for each tile
        # For the empty tile, just a filled tile
        # For all others a black tile, draw a circle, and center a number in it
        surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        if tileNumber == STARTING_OPEN_TILE_INDEX: # draw empty image
            surface.fill(GRAY)
            pygame.draw.rect(surface, BLACK,
                             pygame.Rect((0, 0, TILE_WIDTH, TILE_HEIGHT)),
                             2)  # black border around everything
        else:  # numbered image
            surface.fill(PURPLE)
            pygame.draw.rect(surface, BLACK,
                             pygame.Rect((0, 0, TILE_WIDTH, TILE_HEIGHT)),
                             2)  # black border around everything
            centerX = TILE_WIDTH // 2
            centerY = TILE_HEIGHT // 2
            pygame.draw.circle(surface, YELLOW, (centerX, centerY), 35)
            numberAsImage = font.render(str(self.tileNumber + 1), True, BLACK)
            widthOfNumber = numberAsImage.get_width()
            leftPos = (TILE_WIDTH - widthOfNumber) // 2
            heightOfNumber = numberAsImage.get_height()
            topPos = (TILE_HEIGHT - heightOfNumber) // 2
            surface.blit(numberAsImage, (leftPos, topPos))

            # Alternatively, could load image tiles from a folder:
            # thisTileImage = pygame.image.load('images/tile' + str(number) + '.png')

        self.image = surface

    def isInProperPlace(self, number):
        return (number == self.tileNumber)

    def getLegalMoves(self):
        return self.legalMovesTuple

    def clickedInside(self, mouseLoc):
        hit = self.rect.collidepoint(mouseLoc)
        return hit

    def switch(self, oOtherTile):
        # switch the tileNumber and image of two Tile objects
        self.tileNumber, oOtherTile.tileNumber = oOtherTile.tileNumber, self.tileNumber
        self.image, oOtherTile.image = oOtherTile.image, self.image

    def draw(self):
        self.window.blit(self.image, self.loc)

