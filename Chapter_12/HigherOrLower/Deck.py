# Deck class

import random
from Card import *

class Deck():
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    # This dict maps each card rank to a value for a standard deck
    STANDARD_DICT = {'Ace':1, '2':2, '3':3, '4':4, '5':5,
                                  '6':6, '7':7, '8': 8, '9':9, '10':10,
                                  'Jack':11, 'Queen':12, 'King':13}

    def __init__(self, window, rankValueDict=STANDARD_DICT):
        # rankValueDict defaults to STANDARD_DICT, but you can call 
        # with a different dict, e.g., a special dict for Blackjack
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                oCard = Card(window, rank, suit, value)
                self.startingDeckList.append(oCard)

        self.shuffle()

    def shuffle(self):
        # Copy the starting deck and save it in the playing deck list
        self.playingDeckList = self.startingDeckList.copy()
        for oCard in self.playingDeckList:
            oCard.conceal()
        random.shuffle(self.playingDeckList)

    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise IndexError('No more cards')
        # Pop one card off the deck and return it
        oCard = self.playingDeckList.pop()  
        return oCard

    def returnCardToDeck(self, oCard):
        # Put a card back into the deck
        self.playingDeckList.insert(0, oCard)


if __name__ == '__main__':
    # Main code to test the Deck class

    import pygame

    # Constants
    WINDOW_WIDTH = 100
    WINDOW_HEIGHT = 100

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    oDeck = Deck(window)
    for i in range(1, 53):
        oCard = oDeck.getCard()
        print('Name: ', oCard.getName(), '  Value:', oCard.getValue())

        
##    Optional code to show blackjack deck
##    print('BlackJack Deck:')
##    blackJackDict = {'Ace':1, '2':2, '3':3, '4':4, '5':5,
##                 '6':6, '7':7, '8': 8, '9':9, '10':10,
##                 'Jack':10, 'Queen':10, 'King':10}
##    oBlackjackDeck = Deck(window, rankValueDict=blackJackDict)
##
##    for i in range(1, 53):
##        oCard = oBlackjackDeck.getCard()
##        print('Name: ', oCard.getName(), '  Value:', oCard.getValue())

