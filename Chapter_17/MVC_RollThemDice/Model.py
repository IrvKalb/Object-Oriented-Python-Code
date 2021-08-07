#  ModelDice - Roll Them Dice

import random

SIDES_PER_DIE = 6
SIDES_PER_DIE_PLUS_ONE = SIDES_PER_DIE + 1

# ModelDice Class
class ModelDice():
    def __init__(self, nRounds):
        self.nRounds = nRounds

    def generateRolls(self):
        self.rollsDict = {}
        for total in range(2, 13):  # Initialize all to zero
            self.rollsDict[total] = 0
        for roundNumber in range(0, self.nRounds):
            die1 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            die2 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            theSum = die1 + die2
            self.rollsDict[theSum] = self.rollsDict[theSum] + 1

        return self.nRounds, self.rollsDict

    def setNumberOfRounds(self, nRounds):
        self.nRounds = nRounds

# These are not used right now, but are available for the future
    def getNumberOfRounds(self):
        return self.nRounds

    def getRolls(self):
        return self.rollsDict
