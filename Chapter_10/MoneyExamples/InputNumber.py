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
LEGAL_KEYS_TUPLE = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME,
                    pygame.K_END, pygame.K_DELETE, pygame.K_BACKSPACE, 
                    pygame.K_RETURN, pygame.K_KP_ENTER)
# Legal keys to be typed
LEGAL_UNICODE_CHARS = ('0123456789.-')

#
#  InputNumber inherits from InputText
#
class InputNumber(pygwidgets.InputText):

    def __init__(self, window, loc, value='', fontName=None, fontSize=24, width=200, 
                 textColor=BLACK, backgroundColor=WHITE, focusColor=BLACK, 
                 initialFocus=False, nickName=None, callback=None, mask=None,
                 keepFocusOnSubmit=False, allowFloatingNumber=True, allowNegativeNumber=True):
        self.allowFloatingNumber = allowFloatingNumber
        self.allowNegativeNumber = allowNegativeNumber

        # Call the __init__ method of our base class
        super().__init__(window, loc, value, fontName, fontSize, width, 
                         textColor, backgroundColor, focusColor, initialFocus, nickName,
                         callback, mask, keepFocusOnSubmit)

    # Override handleEvent so we can filter for proper keys
    def handleEvent(self, event):
        if (event.type == pygame.KEYDOWN):  # unicode value is only present on key down
            # Only allow the key to pass if it's an editing key or a numeric key
            allowableKey = (event.key in LEGAL_KEYS_TUPLE) or (event.unicode in LEGAL_UNICODE_CHARS)
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

    def getValue(self):
        userString = super().getValue()
        try:
            if self.allowFloatingNumber:
                returnValue = float(userString)
            else:
                returnValue = int(userString)
        except ValueError:
            raise ValueError('Entry is not a number, needs to have at least one digit.')               
            
        return returnValue


##    def getValue(self):
##        OK = False
##        if char in self.text:
##            if char.isdigit():
##                OK = True
##                break
##
##        if not OK:
##            raise ValueError('Entry is not a number, needs to have at least one digit.')
##        userString = super().getValue()
##        if self.allowFloatingNumber:
##            return float(userString)
##        else:
##            return int(userString)
            
