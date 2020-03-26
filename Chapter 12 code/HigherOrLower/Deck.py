# Deck Class

import random
from Card import *

class Deck():
    SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    STANDARD_VALUES_TUPLE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    def __init__(self, window, valuesTuple=STANDARD_VALUES_TUPLE):
        # If nothing is passed in for valuesTuple, it uses default values
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for index, rank in enumerate(Deck.RANK_TUPLE):
                oCard = Card(window, rank, suit, valuesTuple[index])
                self.startingDeckList.append(oCard)

        self.shuffle()

    def shuffle(self):
        # make a copy of the starting deck and save in the playing deck list
        self.playingDeckList = self.startingDeckList[:]
        for oCard in self.playingDeckList:
            oCard.conceal()
        random.shuffle(self.playingDeckList)

    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise Exception('No more cards')
        oCard = self.playingDeckList.pop()  # pop one off the deck and return it
        return oCard


if __name__ == "__main__":
    # MAIN CODE to test Deck

    import pygame
    from Card import *

    # CONSTANTS
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    oDeck = Deck(window)
    for i in range(1, 53):
        oCard = oDeck.getCard()
        print('Name: ', oCard.getName(), '  Value:', oCard.getValue())
