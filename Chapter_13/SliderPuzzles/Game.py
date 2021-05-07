from Constants import *
from Tile import *
import random

class Game():
    START_LEFT = 35
    START_TOP = 30
    PLAY_SOUND = True
    DONT_PLAY_SOUND = False

    def __init__(self, window):
        self.window = window
        '''
        The game board is made up of 4 rows and 4 columns - 16 tiles.
        However, because Python lists and tuples start at zero, the tiles
        are internally numbered (indexed) 0 to 15, like this:
             0  1  2  3
             4  5  6  7
             8  9 10 11
            12 13 14 15
        '''

        yPos = Game.START_TOP
        self.tilesList = []

        # Create list of Tile objects
        for row in range(0, 4):
            xPos = Game.START_LEFT
            for col in range(0, 4):
                tileNumber = (row * 4) + col
                oTile = Tile(self.window, xPos, yPos, tileNumber)
                self.tilesList.append(oTile)
                xPos = xPos + TILE_WIDTH
            yPos = yPos + TILE_HEIGHT

        self.soundTick = pygame.mixer.Sound('sounds/tick.wav')
        self.soundApplause = pygame.mixer.Sound('sounds/applause.wav')
        self.soundNope = pygame.mixer.Sound('sounds/nope.wav')

        self.playing = False
        self.startNewGame()

    def startNewGame(self):
        # Reset all tiles to starting numbers and images
        for index, oTile in enumerate(self.tilesList):
            oTile.reset(index)

        self.openSpaceIndex = STARTING_OPEN_TILE_INDEX  # index of the open space

        for i in range(0, 200):  # make 200 arbitrary moves to randomize
            legalMovesForThisTile = self.tilesList[self.openSpaceIndex].getLegalMoves()
            nextMoveIndex = random.choice(legalMovesForThisTile)

            # switch tiles
            self.switch(nextMoveIndex, Game.DONT_PLAY_SOUND)
            self.openSpaceIndex = nextMoveIndex

        self.playing = True
        # print('Open space is at index:', self.openSpaceIndex)

    def gotClick(self, clickLoc):
        if not self.playing:
            return  # game is over, waiting for Restart button

        for tileNumber, oTile in enumerate(self.tilesList):
            if oTile.clickedInside(clickLoc):
                # print('Got a mouseDown on box number:', number)
                legalMovesForOpenSpaceTuple = self.tilesList[self.openSpaceIndex].getLegalMoves()
                legalMove = tileNumber in legalMovesForOpenSpaceTuple

                if legalMove:
                    self.switch(tileNumber, Game.PLAY_SOUND)
                else: # illegal move (not next to the open space)
                    self.soundNope.play()
                return

    # Switch a tile with the open space tile
    def switch(self, tileNumberToSwitch, playMoveSound):

        oTileToMove1 = self.tilesList[tileNumberToSwitch]
        oTileToMove2 = self.tilesList[self.openSpaceIndex]

        oTileToMove1.switch(oTileToMove2)

        self.openSpaceIndex = tileNumberToSwitch  # remember position of open space

        if playMoveSound == Game.PLAY_SOUND:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False

        for number in range(0, NTILES):
            if not self.tilesList[number].isInProperPlace(number):
                return False

        # All in proper place, game over
        self.playing = False
        self.soundApplause.play()
        return True

    def getGamePlaying(self):
        return self.playing

    def stopPlaying(self):
        self.playing = False

    def draw(self):
        for oTile in self.tilesList:
            oTile.draw()
