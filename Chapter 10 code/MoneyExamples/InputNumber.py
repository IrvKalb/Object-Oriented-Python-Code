#  InputNumber class, allows the user to only enter numbers
#
#  Demo of inheritance
#

import pygame
from pygame.locals import *
import pygwidgets

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Tuple of legal editing keys
LEGAL_KEYS_TUPLE = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME, pygame.K_END, \
                    pygame.K_DELETE, pygame.K_BACKSPACE, \
                    pygame.K_RETURN, pygame.K_KP_ENTER, \
                    )
# Tuple of unicode of legal keys to be typed
LEGAL_UNICODE_TUPLE = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-')

#
#  InputNumber inherits from InputText
#
class InputNumber(pygwidgets.InputText):

    def __init__(self, window, loc, startingAmount='', allowFloatingNumber=True, \
                 allowNegativeNumber=True, fontName=None, fontSize=24, width=200, \
                 textColor=BLACK, backgroundColor=WHITE, focusColor=BLACK, \
                 initialFocus=False, nickName=None):
        self.allowFloatingNumber = allowFloatingNumber
        self.allowNegativeNumber = allowNegativeNumber

        # Call the __init__ method of our base class
        super().__init__(window, loc, startingAmount, fontName, fontSize, width, \
                         textColor, backgroundColor, focusColor, initialFocus, nickName)

    # Override handleEvent so we can filter for proper keys
    def handleEvent(self, event):
        if (event.type == pygame.KEYDOWN):  # unicode value is only present on key down
            # Only allow the key to pass if it's an editing key or a numeric key
            allowableKey = (event.key in LEGAL_KEYS_TUPLE) or (event.unicode in LEGAL_UNICODE_TUPLE)
            if not allowableKey:
                return False

            if event.unicode == '-':  # user typed a minus sign
                if not self.allowNegativeNumber:
                    return False  # if negatives are now allowed, don't pass minus through
                if self.cursorPosition > 0:
                    return False  # can't put minus sign after first char
                if '-' in self.text:
                    return False  # can't enter a second minus sign

            if event.unicode == '.':
                if not self.allowFloatingNumber:
                    return False  # if floats are not allowed, don't pass the period through
                if '.' in self.text:
                    return False  # can't enter a second period

        result = super().handleEvent(event)  # allow the key or event to go through to the base class
        return result

