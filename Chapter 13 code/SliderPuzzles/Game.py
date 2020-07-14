from Constants import *
from Square import *
import random



class Game():
    NSQUARES = 16
    OPEN_SQUARE_VALUE = 15  # value of the empty square in the game
    START_LEFT = 35
    START_TOP = 30
    PLAY_SOUND = True
    DONT_PLAY_SOUND = False

    def __init__(self, window):
        self.window = window

        # The following is a list of lists
        # Each sub list is the index of all legal moves from the current square
        # For example, for square 0, only squares 1 and 4 are legal.
        self.legalMovesList = [ \
            [1, 4], \
            [0, 2, 5], \
            [1, 3, 6], \
            [2, 7], \
            [0, 5, 8], \
            [1, 4, 6, 9], \
            [2, 5, 7, 10], \
            [3, 6, 11], \
            [4, 9, 12], \
            [5, 8, 10, 13], \
            [6, 9, 11, 14], \
            [7, 10, 15], \
            [8, 13], \
            [9, 12, 14], \
            [10, 13, 15], \
            [11, 14]]

        font = pygame.font.SysFont(None, 60)
        self.tileImageList = []
        for number in range(0, Game.NSQUARES):

            # Use drawing calls to create a surface for each tile
            # Draw a black square, draw a circle, and center a number in it
            surface = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
            if number < Game.OPEN_SQUARE_VALUE:
                surface.fill(PURPLE)
                pygame.draw.rect(surface, BLACK, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)),
                                 2)  # black border around everything
                centerX = SQUARE_WIDTH // 2
                centerY = SQUARE_HEIGHT // 2
                pygame.draw.circle(surface, YELLOW, (centerX, centerY), 35)
                numberAsImage = font.render(str(number + 1), True, BLACK)
                widthOfNumber = numberAsImage.get_width()
                leftPos = (SQUARE_WIDTH - widthOfNumber) // 2
                heightOfNumber = numberAsImage.get_height()
                topPos = (SQUARE_HEIGHT - heightOfNumber) // 2
                surface.blit(numberAsImage, (leftPos, topPos))

            else:
                surface.fill(GRAY)
                pygame.draw.rect(surface, BLACK, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)),
                                 2)  # black border around everything

            # Alternatively, could load image tiles from a folder:
            # thisTileImage = pygame.image.load('images/tile' + str(number) + '.png')

            self.tileImageList.append(surface)

        yPos = Game.START_TOP
        squareNum = 0
        self.squareList = []

        for row in range(0, 4):
            xPos = Game.START_LEFT

            for col in range(0, 4):
                oSquare = Square(self.window, xPos, yPos)
                self.squareList.append(oSquare)
                squareNum = squareNum + 1
                xPos = xPos + SQUARE_WIDTH


            yPos = yPos + SQUARE_HEIGHT

        self.soundTick = pygame.mixer.Sound('sounds/tick.wav')
        self.soundApplause = pygame.mixer.Sound('sounds/applause.wav')
        self.soundNope = pygame.mixer.Sound('sounds/nope.wav')

        self.startNewGame()

    def startNewGame(self):

        for number, oSquare in enumerate(self.squareList):
            oSquare.setValue(number)  # initialize value in each square
            thisImage = self.tileImageList[number]
            oSquare.setImage(thisImage)

        self.openSpaceIndex = Game.OPEN_SQUARE_VALUE  # index of the open space

        previousOpenSpaceIndex = -1

        for i in range(0, 200):  # make 200 arbitrary moves to randomize
            legalMovesForThisSpaceList = self.legalMovesList[self.openSpaceIndex]
            nMoves = len(legalMovesForThisSpaceList)
            randomIndex = random.randrange(nMoves)
            nextMoveIndex = legalMovesForThisSpaceList[randomIndex]

            # This code ensures that the next random move to try is not
            # the reverse of the previous random move
            if nextMoveIndex == previousOpenSpaceIndex:
                randomIndex = randomIndex + 1
            if randomIndex >= nMoves:
                randomIndex = 0

            nextMoveIndex = legalMovesForThisSpaceList[randomIndex]

            # switch values
            self.switch(nextMoveIndex, Game.DONT_PLAY_SOUND)

            previousOpenSpaceIndex = self.openSpaceIndex
            self.openSpaceIndex = nextMoveIndex

        self.playing = True
        # print 'Open space is at index:', self.openSpaceIndex

    def gotClick(self, clickLoc):
        if not self.playing:
            # print 'Game is over ... waiting to restart'
            return  # game is over, waiting for Restart button

        for number, square in enumerate(self.squareList):
            if square.clickInside(clickLoc):
                # print 'Got a mouseDown on box number:', boxNum

                legalMovesForOpenSpaceList = self.legalMovesList[self.openSpaceIndex]
                # print 'legalMovesForOpenSpaceList, boxNum: ', legalMovesForOpenSpaceList, boxNum
                legalMove = number in legalMovesForOpenSpaceList

                if legalMove:
                    self.switch(number, Game.PLAY_SOUND)
                else:
                    # illegal move (not next to the empty space)
                    self.soundNope.play()
                return

    def draw(self):
        for oSquare in self.squareList:
            oSquare.draw()

    # Switch the square with the empty piece
    def switch(self, squareNumToSwitch, playMoveSound):
        # print 'Must switch box number', squareNumToSwitch, ' and ', self.openSpaceIndex
        valueToMove1 = self.squareList[squareNumToSwitch].getValue()
        imageToMove1 = self.squareList[squareNumToSwitch].getImage()
        valueToMove2 = self.squareList[self.openSpaceIndex].getValue()
        imageToMove2 = self.squareList[self.openSpaceIndex].getImage()

        self.squareList[squareNumToSwitch].setValue(valueToMove2)
        self.squareList[squareNumToSwitch].setImage(imageToMove2)
        self.squareList[self.openSpaceIndex].setValue(valueToMove1)
        self.squareList[self.openSpaceIndex].setImage(imageToMove1)

        self.openSpaceIndex = squareNumToSwitch  # remember position of open space

        if playMoveSound == Game.PLAY_SOUND:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False

        for number in range(0, Game.NSQUARES):
            if self.squareList[number].getValue() != number:
                return False

        self.playing = False  # game is over
        self.soundApplause.play()
        return True

    def getGamePlaying(self):
        return self.playing

    def stopPlaying(self):
        self.playing = False