# DisplayMoney class - displays a number as an amount of money
#
# Demo of inheritance

import pygwidgets

BLACK = (0, 0, 0)

#  DisplayMoney class inherits from DisplayText class
class DisplayMoney(pygwidgets.DisplayText):

    def __init__(self, window, loc, value=None,
                 fontName=None, fontSize=24, width=150, height=None, 
                 textColor=BLACK, backgroundColor=None,
                 justified='left', nickname=None, currencySymbol='$',
                 currencySymbolOnLeft=True, showCents=True):

        self.currencySymbol = currencySymbol
        self.currencySymbolOnLeft = currencySymbolOnLeft
        self.showCents = showCents
        if value is None:
            value = 0.00

        # Call the __init__ method of our base class
        super().__init__(window, loc, value, fontName, fontSize,
                            width, height, textColor, backgroundColor,
                            justified, nickname)

    def setValue(self, money):
        if money == '':
            money = 0.00

        money = float(money)

        if self.showCents:
            money = '{:,.2f}'.format(money)
        else:
            money = '{:,.0f}'.format(money)

        if self.currencySymbolOnLeft:
            theText = self.currencySymbol + money
        else:
            theText = money + self.currencySymbol

        # Call the setValue method of our base class
        super().setValue(theText)
