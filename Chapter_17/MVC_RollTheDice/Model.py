#  Model - Roll The Dice

import random
from Constants import *

SIDES_PER_DIE = 6
SIDES_PER_DIE_PLUS_ONE = SIDES_PER_DIE + 1

# Model Class
class Model():
    def __init__(self):
        self.nRounds = 0
        self.rollsDict = {}
        self.percentsDict = {}

    def generateRolls(self, nRounds):
        self.nRounds = nRounds
        self.rollsDict = {}
        for total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):  # Initialize all to zero
            self.rollsDict[total] = 0

        # Roll two dice, add them up, increment the count in the dict
        for roundNumber in range(0, self.nRounds):
            die1 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            die2 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            theSum = die1 + die2
            self.rollsDict[theSum] = self.rollsDict[theSum] + 1

        # Calculate  and save percentages in a dict
        self.percentsDict = {}
        for rollTotal, count in self.rollsDict.items():
            thisPercent = count / self.nRounds
            self.percentsDict[rollTotal] = thisPercent

    # All current views call this method to get all the data.
    def getRoundsRollsPercents(self):
        return self.nRounds, self.rollsDict, self.percentsDict

    # The methods below aren't used right now, but are available for new views
    def getNumberOfRounds(self):
        return self.nRounds

    def getRolls(self):
        return self.rollsDict

    def getPercents(self):
        return self.percentsDict
