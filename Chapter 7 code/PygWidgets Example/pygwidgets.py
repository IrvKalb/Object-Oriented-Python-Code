"""
pygwidgets is a collection of user interface widgets (e.g., buttons) written in Python for use with Pygame.

pygwidgets is pronounced as: "pig wijits".

Developed by Irv Kalb  -    Irv at furrypants.com

Full documentation at:   https://pygwidgets.readthedocs.io/en/latest/



Design notes:

    The way that you use objects instantiated from all these classes is very similar:
    
        1. Instantiate before the big loop starts.
         
        2. Call the object's "handleEvent" method every time through the loop.
           It  will return False most of the time,
           but returns True when something exciting happens (for example, user clicks on a button).
         
        3. Call the "draw" method (with no arguments) to draw each widget.
         
    I have tried to make consistent keyword parameter names across classes.

    I have also tried to make consistent names for methods across classes
    For example "getValue" and "setValue" are available in most classes.

    When instantiating objects from these classes, you typically only need to specify a few parameters.
    The rest will use reasonable default values, but you can change them using keyword arguments.


Each of the button widgets comes in two varieties:

    Text widget that is drawn using the Python's drawing tools.

    Custom widget where the programmer supplies their own graphics for the widget.

For example, "TextButton" below builds a button from a user-supplied text string,
whereas "CustomButton" is built to work with user-supplied custom images.



pygwidgets contains the following classes:

- TextButton - a button built on the fly from a user-supplied text.
- CustomButton - a button where you use your own images

- TextCheckBox - a checkbox built on the fly from a user-supplied text.
- CustomCheckBox - a checkbox where you use your images

- TextRadioButton - a radio button built on the fly from a user-supplied text.
- CustomRadioButton - a radio button where you use your images

- DisplayText - a text field used just for output (display)

- InputText - a text field intended for user input

- Dragger - gives the ability to drag any screen object with the mouse

- Image - simple display of an image at a location

- ImageCollection - A collection of Images, any of which can be shown at one time

- Animation - display a set number of images, each at its own rate
- SpriteSheetAnimation - display an animation directly from a sprite sheet
  (one file made up of many images)


Many widgets allow the use of a callback (a function or method to be called when an action happens)
    Any widget that uses a callback should be set up like this:
          def <callbackMethodName>(self, nickName)
    When the appropriate action happens, the callback method will be called and the nickName will be passed
    If you don't need the nickname, you can just ignore that parameter
 
************************************************************************************************

Simplified BSD License:

Copyright 2017 Irv Kalb. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY Irv Kalb ''AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Irv Kalb OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Irv Kalb.

******************************************************************************************


History:

5/19  Added ability in ImageCollection to specify a loaded image (alternative for giving path to image)
    Fixed conflict with "replace" in Image and ImageCollection classes.

4/19  Added the ability for Image and ImageCollection objects to use the empty string
    to indicate that the object should show no image.
    Added Image and ImageCollection to recognize clicks by adding handleEvents method

7/18   Added ability for all appropriate widgets to allow an optional callBack
    Changed "textButton" in Button, CheckBox, and RadioButton to "text"
    Change "label" to "nickname" in all widgets.


6/18   Added Animation and SpriteSheetAnimation

6/18   Added getRect (removed copy from Dragger and Image)
    In TextButton, changed param 'label' to 'text' to avoid confusion with superclass

5/18   Added Image object.  Allows you to set a loc and window at the instantiation.
    That way, all you need to do to show the image is to call its draw method.

1/18   Changed Button->TexButton, CheckBox->TextCheckBox, RadioButton->TextRadioButton
    Changed SetVisible->show, setInVisible->hide
    Created PygWidget base class, and have all classes inherit from it
    initializes and contains: nickname, visible, isEnabled

11/17  Added Dragger, changed main "surface" to "window"  Irv Kalb
    Changed 'caption' in the Button class to 'nickname', made it a positional parameter
    (instead of optional keyword param)
    Added 'nickname' and getNickname method to most classes
    Modified Button to grow to fit very long nicknames - defaults to minimum of 100 pixels.
    Added setPos to DisplayText 

4/17  Version 1.1 by Irv Kalb
    Renamed a few classes and methods, simplified the return of handleEvent in all classes
        to be just True or False.

3/17  Version 1.0 by Irv Kalb
    Combined Buttons, CheckBoxes, RadioButtons, and Text into a single file

1/17  Major rewrite by Irv Kalb
    Split the code into Button class and CustomButton class (with a common superclass: PygWidgetsButton).
    Added appropriate parameters with reasonable defaults so each is easier to instantiate.
    Added soundOnClick

12/16  Modified by Irv Kalb
     Add a default surface, so it is passed in once at creation.
     That way, calls to draw do not need to pass it in again.

8/14   Modified by Irv Kalb
     Added a disabled state to all buttons
     
The code of the TextButton and CustomButton classes are based on the original "pygbutton"
code developed by Al Sweigart.  I kept the good stuff (and there was plenty of that!),
added features (most importantly a disabled state), and removed some features that
I didn't feel were needed for the students in my classes.

*****************************************************************************************


"""

"""
ORIGINAL COMMENTS FROM AL SWEIGART ABOUT PYGBUTTON:

PygButton v0.1.0

PygButton (pronounced "pig button") is a module that implements UI buttons for Pygame.
PygButton requires Pygame to be installed. Pygame can be downloaded from http://pygame.org
PygButton was developed by Al Sweigart (al@inventwithpython.com)
https://github.com/asweigart/pygbutton


Simplified BSD License:

Copyright 2012 Al Sweigart. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY Al Sweigart ''AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Al Sweigart OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Al Sweigart.
"""

import pygame
import time
from pygame.locals import *

PYGWIDGETS_BLACK = (0, 0, 0)
PYGWIDGETS_WHITE = (255, 255, 255)
PYGWIDGETS_DARK_GRAY = (64, 64, 64)
PYGWIDGETS_GRAY = (128, 128, 128)
PYGWIDGETS_DOWN_GRAY = (140, 140, 140)
PYGWIDGETS_NORMAL_GRAY = (170, 170, 170)
PYGWIDGETS_OVER_GRAY = (210, 210, 210)
PYGWIDGETS_DISABLED_GRAY = (220, 220, 220)

pygame.font.init()

class PygWidget():
    """This is the base class (superclass) of ALL pygwidgets - this is an abstract class.

    It provides common functionality:
        - ability to show or hide any widget
        - ability to enable or disable any widget
        - save and retrieve a nickname associated with the widget
        - ability to get and set the loc, and get the rect of any widget

    """
    def __init__(self, nickname):
        """Initializes PygWidget.  Just sets a few key instance variables.

        Parameter:
            nickname - any name you want to associate with this widget
            
        """
        if type(self) is PygWidget:
            raise Exception('You should never instantiate PygWidget - it is an abstract class.')

        self.visible = True
        self.isEnabled = True
        self.nickname = nickname  # any nickname you want to associate with this widget
        self.dependentsList = [] # list of objects are depend on this object (for enabled/disabled)
        self.enableDependents = False
        self.rect = pygame.Rect(0, 0, 0, 0)

    def __del__(self):
        self.dependentsList = []  # remove all dependent objects - for future expansion

    def show(self):
        """Make this widget visible."""
        self.visible = True

    def hide(self):
        """Make this widget invisible."""
        self.visible = False

    def getVisible(self):
        """Returns the visible state."""
        return self.visible

    def enable(self):
        """Set this widget enabled."""
        self.isEnabled = True

    def disable(self):
        """Disables the current widget."""
        self.isEnabled = False

    def getEnabled(self):
        """Returns the enabled state."""
        return self.isEnabled

    def getNickname(self):
        """Returns the nickname associated with this widget."""
        return self.nickname

    def setLoc(self, loc):   # loc must be a tuple or list of x,y coordinates
        """Sets a new location (and changes the rect loc) for this widget."""
        self.loc = loc
        self.rect[0] = self.loc[0]
        self.rect[1] = self.loc[1]

    def getLoc(self):
        """Returns the location of this widget."""
        return self.loc

    def getRect(self):
        """Returns the rect of this widget."""
        return self.rect

    def overlaps(self, otherRect):
        collided = otherRect.colliderect(self.rect)
        return collided

    def getX(self):
        return self.rect.left

    def getY(self):
        return self.rect.top

    # def addDependent(self, oDependent):
    #     if not (isinstance(oDependent, list)):  # if it is a single object, make it a list
    #         oDependent = [oDependent]  # so we can iterate
    #     for thisDependent in oDependent:
    #         if oDependent not in self.dependentsList:
    #             self.dependentsList.append(thisDependent)
    #
    # def removeDependent(self, oDependent):
    #     if not (isinstance(oDependent, list)):  # if it is a single object, make it a list
    #         oDependent = [oDependent]  # so we can iterate
    #     for thisDependent in oDependent:
    #         if thisDependent in self.dependentsList:
    #             self.dependentsList.remove(thisDependent)
    #
    # def getDependents(self):
    #     """ Returns the list of dependent objects """
    #     return self.dependentsList


#
#
# BUTTON
# 
#
class PygWidgetsButton(PygWidget):
    """Base class of TextButton and CustomButton (below) - this is an abstract class.

    You should never instantiate from this class.
    Instead, instantiate a TextButton or CustomButton, then use the rest of the methods provided.
    TextButtons are built using the drawing methods in Pygame.
    CustomButtons are built using your supplied graphics.
    Details are in comments for those classes below.
    This code handles showing all the appropriate states of the button (up, down, over, disabled),
    based on user actions and method calls.



    """
        
    def __init__(self, window, loc, surfaceUp, surfaceOver, surfaceDown, surfaceDisabled, \
                 theRect, soundOnClick, nickname, enterToActivate, callBack):

        if type(self) is PygWidgetsButton:
            raise Exception('You need to instantiate a TextButton or CustomButton (not PygWidgetsButton directly)')

        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.surfaceUp = surfaceUp
        self.surfaceOver = surfaceOver
        self.surfaceDown = surfaceDown
        self.surfaceDisabled = surfaceDisabled
        self.rect = theRect
        self.soundOnClick = soundOnClick
        self.enterToActivate = enterToActivate
        self.callBack = callBack

        # used to track the state of the button
        self.buttonDown = False # is the button currently pushed down?
        self.mouseOverButton = False # is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # was the last mouse down event over the mouse button? (Tracks clicks.)
        if self.soundOnClick is not None:
            self.playSoundOnClick = True
            if type(self.soundOnClick) is str:  # user specified sound path, load it here
                pygame.mixer.init()
                self.soundOnClick = pygame.mixer.Sound(self.soundOnClick)  # save in same instance variable
        else:
            self.playSoundOnClick = False

        self.mouseIsDown = False


    def handleEvent(self, eventObj):
        """This method should be called every time through the main loop.

        It handles showing the up, over, and down states of the button.

        Parameters:
            | eventObj - the event object obtained by calling pygame.event.get()

        Returns:
            | False most of the time
            | True when the user clicks down and later up on the button.

        """

        if self.enterToActivate:
            if eventObj.type == pygame.KEYDOWN:

                # Return or Enter key
                if eventObj.key == pygame.K_RETURN:
                    return True

        if (eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN)) or (not self.visible):
            # The button only cares bout mouse-related events (or no events, if it is invisible)
            return False

        if not self.isEnabled:
            return False

        clicked = False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)
        if (not self.mouseOverButton) and eventPointInButtonRect:
            # if mouse has entered the button:
            self.mouseOverButton = True

        elif self.mouseOverButton and (not eventPointInButtonRect):
            # if mouse has exited the button:
            self.mouseOverButton = False

        if eventPointInButtonRect:

            if eventObj.type == MOUSEBUTTONDOWN:
                self.buttonDown = True
                self.lastMouseDownOverButton = True

        else:
            if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                # if an up/down happens off the button, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False

        if eventObj.type == MOUSEBUTTONDOWN:
            self.mouseIsDown = True
            
        # mouse up is handled whether or not it was over the button
        doMouseClick = False
        if eventObj.type == MOUSEBUTTONUP:
            self.mouseIsDown = False
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False

            if self.buttonDown:
                self.buttonDown = False

            if doMouseClick:
                self.buttonDown = False
                clicked = True
                self.mouseOverButton = False  # forces redraw of up state after click
                
                if self.playSoundOnClick:
                    self.soundOnClick.play()

        if clicked:
            if self.callBack is not None:
                self.callBack(self.nickname)

        return clicked

    def draw(self):
        """Draws the button in its current state.

        Should be called every time through the main loop

        """
        if not self.visible:
            return

        # Blit the button's current appearance to the surface.
        if self.isEnabled:
            if self.mouseIsDown:
                if self.mouseOverButton and self.lastMouseDownOverButton:
                    self.window.blit(self.surfaceDown, self.loc)
                else:
                    self.window.blit(self.surfaceUp, self.loc)
            else:  # mouse is up
                if self.mouseOverButton:
                    self.window.blit(self.surfaceOver, self.loc)
                else:
                    self.window.blit(self.surfaceUp, self.loc)

        else:
            self.window.blit(self.surfaceDisabled, self.loc)


    def _debug(self):
        """This is just for debugging, so we can see what buttons would be drawn.

        Not intended to be used in production."""
        self.window.blit(self.surfaceUp, (self.loc[0], 10))
        self.window.blit(self.surfaceOver, (self.loc[0], 60))
        self.window.blit(self.surfaceDown, (self.loc[0], 110))
        self.window.blit(self.surfaceDisabled, (self.loc[0], 160))


class TextButton(PygWidgetsButton):
    """TextButton creates a text-based button on the fly using a given string.

    Each TextButton has four states:  up, over, down, and disabled

    Typical use:

    1) Create TextButton (giving a loc (left, top) and text). e.g.:

        myButton = pygwidgets.TextButton(window, (500, 430), 'Some Text to show on the button')

        There are many optional parameters, including width and height that have good defaults.

    2) In your big loop, check for the button being clicked by calling its handleEvent method:

        if myButton.handleEvent(event):  # When the button is clicked, this returns True
            #  the button was clicked, do whatever you want here

    3) At the bottom of your big loop, draw the button:

        myButton.draw()

    Parameters:
        | window - the window to draw the button in
        | loc - the location (left and top) of the button as a tuple e.g. (10, 200).
        | text - the text to show on the button
    Optional keyword parameters:
        | width - the width of the button (default is 100)
        | height - the height of the button (default is 40)
        | textColor - the rgb color of the text. (default is black).
        | upColor - the background rgb color of the up button (default is a medium gray)
        | overColor - the background rgb color of the over button (default is a lighter gray)
        | downColor - the background rgb color of down button (default is a darker gray)
        | fontName - the name of the font to use for the text (default is freesansbold)
        | fontsize - the size fo the font to use (default is 14)
        | soundOnClick - a path to a sound effect file. Plays when the button is clicked (defaults to None)
        | enterToActivate - if user presses Enter (or Return), button will activate (default is False)
        | nickname - any name you want to use to identify this button (default is None)
        | callBack - a function or object.method to call when the button is clicked (default is None)


    """

    DEFAULT_FONT_NAME = None  # use Pygame default font
    DEFAULT_FONT_SIZE = 20
    PYGWIDGETS_FONT = pygame.font.Font(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)
    MINIMUM_WIDTH = 100

    def __init__(self, window, loc, text, width=None, height=40, textColor=PYGWIDGETS_BLACK, \
                 upColor=PYGWIDGETS_NORMAL_GRAY, overColor=PYGWIDGETS_OVER_GRAY, downColor=PYGWIDGETS_DOWN_GRAY, \
                 fontName=DEFAULT_FONT_NAME, fontSize=DEFAULT_FONT_SIZE, soundOnClick=None, \
                 enterToActivate=False, callBack=None, nickname=''):

        # Create the button's Surface objects.
        if nickname == '':
            nickname = text  # use the text as the internal name
        text = ' ' + text + ' '  # add padding for drawn text
        self.textColor = textColor
        self.upColor = upColor
        self.overColor = overColor
        self.downColor = downColor

        if (fontName == TextButton.DEFAULT_FONT_NAME) and (fontSize == TextButton.DEFAULT_FONT_SIZE):
            self.font = TextButton.PYGWIDGETS_FONT
        else:
            self.font = pygame.font.SysFont(fontName, fontSize)

        # create the text surface for up state of button (to get the size)
        textSurfaceUp = self.font.render(text, True, self.textColor, self.upColor)
        textRect = textSurfaceUp.get_rect()
        if width is None:
            # See if the text will fit inside the minimum width
            if textRect.width < TextButton.MINIMUM_WIDTH:
                width = TextButton.MINIMUM_WIDTH
            else:  # Make the width wide enough to handle all the text
                width = textRect.width

        buttonRect = pygame.Rect(loc[0], loc[1], width, height)
        w = buttonRect.width  # syntactic sugar
        h = buttonRect.height  # syntactic sugar
        size = buttonRect.size

        textRect.center = (int(w / 2), int(h / 2))

        # draw the up button
        surfaceUp = pygame.Surface(size)
        surfaceUp.fill(self.upColor)
        surfaceUp.blit(textSurfaceUp, textRect)
        if enterToActivate:
            pygame.draw.rect(surfaceUp, PYGWIDGETS_BLACK, pygame.Rect((0, 0, w - 1, h - 1)), 2)  # thicker black border
            pygame.draw.line(surfaceUp, PYGWIDGETS_WHITE, (2, 2), (w - 3, 2))
            pygame.draw.line(surfaceUp, PYGWIDGETS_WHITE, (2, 2), (2, h - 3))
            pygame.draw.line(surfaceUp, PYGWIDGETS_GRAY, (3, h - 3), (w - 3, h - 3))
            pygame.draw.line(surfaceUp, PYGWIDGETS_GRAY, (w - 3, 3), (w - 3, h - 3))
        else:
            pygame.draw.rect(surfaceUp, PYGWIDGETS_BLACK, pygame.Rect((0, 0, w, h)), 1)  # black border
            pygame.draw.line(surfaceUp, PYGWIDGETS_WHITE, (1, 1), (w - 2, 1))
            pygame.draw.line(surfaceUp, PYGWIDGETS_WHITE, (1, 1), (1, h - 2))
            pygame.draw.line(surfaceUp, PYGWIDGETS_DARK_GRAY, (1, h - 1), (w - 1, h - 1))
            pygame.draw.line(surfaceUp, PYGWIDGETS_DARK_GRAY, (w - 1, 1), (w - 1, h - 1))
            pygame.draw.line(surfaceUp, PYGWIDGETS_GRAY, (2, h - 2), (w - 2, h - 2))
            pygame.draw.line(surfaceUp, PYGWIDGETS_GRAY, (w - 2, 2), (w - 2, h - 2))

        # draw the down button
        surfaceDown = pygame.Surface(size)
        surfaceDown.fill(self.downColor)
        textSurfaceDown = self.font.render(text, True, self.textColor, self.downColor)
        textOffsetByOneRect = pygame.Rect(textRect.left + 1, textRect.top + 1, textRect.width,
                                                textRect.height)
        surfaceDown.blit(textSurfaceDown, textOffsetByOneRect)
        pygame.draw.rect(surfaceDown, PYGWIDGETS_BLACK, pygame.Rect((0, 0, w, h)), 1)  # black border around everything
        pygame.draw.line(surfaceDown, PYGWIDGETS_WHITE, (1, 1), (w - 2, 1))
        pygame.draw.line(surfaceDown, PYGWIDGETS_WHITE, (1, 1), (1, h - 2))
        pygame.draw.line(surfaceDown, PYGWIDGETS_DARK_GRAY, (1, h - 2), (1, 1))
        pygame.draw.line(surfaceDown, PYGWIDGETS_DARK_GRAY, (1, 1), (w - 2, 1))
        pygame.draw.line(surfaceDown, PYGWIDGETS_GRAY, (2, h - 3), (2, 2))
        pygame.draw.line(surfaceDown, PYGWIDGETS_GRAY, (2, 2), (w - 3, 2))

        # draw the over button
        surfaceOver = pygame.Surface(size)
        surfaceOver.fill(self.overColor)
        textSurfaceOver = self.font.render(text, True, self.textColor, self.overColor)
        surfaceOver.blit(textSurfaceOver, textRect)
        pygame.draw.rect(surfaceOver, PYGWIDGETS_BLACK, pygame.Rect((0, 0, w, h)), 1)  # black border around everything
        pygame.draw.line(surfaceOver, PYGWIDGETS_WHITE, (1, 1), (w - 2, 1))
        pygame.draw.line(surfaceOver, PYGWIDGETS_WHITE, (1, 1), (1, h - 2))
        pygame.draw.line(surfaceOver, PYGWIDGETS_DARK_GRAY, (1, h - 1), (w - 1, h - 1))
        pygame.draw.line(surfaceOver, PYGWIDGETS_DARK_GRAY, (w - 1, 1), (w - 1, h - 1))
        pygame.draw.line(surfaceOver, PYGWIDGETS_GRAY, (2, h - 2), (w - 2, h - 2))
        pygame.draw.line(surfaceOver, PYGWIDGETS_GRAY, (w - 2, 2), (w - 2, h - 2))

        # draw the disabled button
        surfaceDisabled = pygame.Surface(size)
        surfaceDisabled.fill(PYGWIDGETS_DISABLED_GRAY)
        textSurfaceDisabled = self.font.render(text, True, PYGWIDGETS_GRAY, PYGWIDGETS_DISABLED_GRAY)
        surfaceDisabled.blit(textSurfaceDisabled, textRect)
        pygame.draw.line(surfaceDisabled, PYGWIDGETS_GRAY, (1, h - 1), (w - 1, h - 1))
        pygame.draw.line(surfaceDisabled, PYGWIDGETS_GRAY, (w - 1, 1), (w - 1, h - 1))
        pygame.draw.line(surfaceDisabled, PYGWIDGETS_GRAY, (2, h - 2), (w - 2, h - 2))
        pygame.draw.line(surfaceDisabled, PYGWIDGETS_GRAY, (w - 2, 2), (w - 2, h - 2))

        # call the PygWidgetsButton superclass to finish initialization

        super().__init__(window, loc, surfaceUp, surfaceOver, surfaceDown, surfaceDisabled, \
                         buttonRect, soundOnClick, nickname, enterToActivate, callBack)


## Older way to do the same thing:
##     super(TextButton, self).__init__(window, loc, surfaceUp, surfaceOver, surfaceDown, surfaceDisabled, \
##                   buttonRect, soundOnClick, nickname, enterToActivate)


class CustomButton(PygWidgetsButton):
    """CustomButton creates a button using custom images.

    Each CustomButton has four states:  up, over, down, and disabled.

    Typical use:

    1) Create a CustomButton - giving a location tuple - as (left, top) and up to four images, e.g.:

         |   myButton = pygwidgets.CustomButton(window, (500, 430), 
         |                                    up='images/ButtonUp.png',
         |                                    down='images/ButtonDown.png',
         |                                    over='images/ButtonOver.png',
         |                                    disabled='images/ButtonDisabled.png')

    2) In your big loop, check for the button being clicked by calling its handleEvent method:

        if myButton.handleEvent(event):  # When the button is clicked, this returns True
            #  the button was clicked, do whatever you want here

    3) At the bottom of your big loop, draw the button:

        myButton.draw()


    The up, down, over, and disabled images must all be the same size.
    Only the up image needs to be specified. If any of the others are left out, 
    they will default to be a copy of the up surface.

    Parameters:
        | window - the window to draw the button in
        | loc - a tuple specifying the position (upper left corner) for the button to be drawn.
        | up - a path to a file with the button's up appearance.
    Optional keyword parameters:
        | down - a path to a file with the button's pushed down appearance.
        | over - a path to a file with the button's appearance when the mouse is over it.
        | disabled - a path to a file with the button's disabled appearance.
        | soundOnClick - a path to a sound effect file. Plays when the button is clicked (defaults to None)
        | nickname - any name you want to use to identify this button (default is None)
        | callBack - a function or object.method to call when the button is clicked (default is None)




    """

    def __init__(self, window, loc, up, down=None, over=None, disabled=None, soundOnClick=None, \
                 nickname=None, enterToActivate=False, callBack=None):

        # Create the button's Surface objects.
        surfaceUp = pygame.image.load(up)

        if down is None:
            surfaceDown = surfaceUp
        else:
            surfaceDown = pygame.image.load(down)

        if over is None:
            surfaceOver = surfaceUp
        else:
            surfaceOver = pygame.image.load(over)

        if disabled is None:
            surfaceDisabled = surfaceUp
        else:
            surfaceDisabled = pygame.image.load(disabled)

        width, height = surfaceUp.get_size()
        buttonRect = pygame.Rect(loc[0], loc[1], width, height)

        if (width, height) == surfaceDown.get_size() \
                == surfaceOver.get_size() == surfaceDisabled.get_size():
            pass  # typical case, sizes all match
        else:
            raise Exception('Custom button files (starting with: ' + up + ') are not all the same size')

        # call the PygWidgetsButton superclass to finish initialization
        super().__init__(window, loc, surfaceUp, surfaceOver, surfaceDown, surfaceDisabled,
                                    buttonRect, soundOnClick, nickname, enterToActivate, callBack)
# Older way to do the same thing:
#    super(CustomButton, self).__init__(window, loc, surfaceUp, surfaceOver, surfaceDown, surfaceDisabled,
#                                       buttonRect, soundOnClick, nickname, enterToActivate)


#
#
#  CHECKBOX
#
#
class PygWidgetsCheckBox(PygWidget):
    """Superclass of TextCheckBox and CustomCheckBox (see code below) - this is an abstract class.

    You should never instantiate from this class.
    Instead, instantiate a TextCheckBox or CustomCheckBox, then use the rest of the methods provided.


    """

    def __init__(self, window, loc, theRect, \
                 surfaceOn, surfaceOff, surfaceOnDown, surfaceOffDown,\
                 surfaceOnDisabled, surfaceOffDisabled, soundOnClick, value, nickname, callBack):
        """Initializer for the PygWidgetsCheckBox base class."""

        if type(self) is PygWidgetsCheckBox:
            raise Exception('You need to instantiate a CheckBox or CustomCheckBox (not PygWidgetsCheckBox directly)')

        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.rect = theRect
        self.surfaceOn = surfaceOn
        self.surfaceOff = surfaceOff
        self.surfaceOnDown = surfaceOnDown
        self.surfaceOffDown = surfaceOffDown
        self.surfaceOnDisabled = surfaceOnDisabled
        self.surfaceOffDisabled = surfaceOffDisabled
        self.soundOnClick = soundOnClick
        # self.value is the most important attribute - contains True or False
        self.value = value
        self.nickname = nickname
        self.callBack = callBack

        # used to track the state of the checkBox
        self.buttonDown = False  # is the checkBox currently pushed down?
        self.mouseOverButton = False  # is the mouse currently hovering over the checkBox?
        self.lastMouseDownOverButton = False # was the last mouse down event over the mouse button? (Track clicks.)
        if self.soundOnClick is not None:
            self.playSoundOnClick = True
            if type(self.soundOnClick) is str:  # user specified sound path, load it here
                pygame.mixer.init()
                self.soundOnClick = pygame.mixer.Sound(self.soundOnClick)  # save in same instance variable
        else:
            self.playSoundOnClick = False

        self.mouseIsDown = False



    def handleEvent(self, eventObj):
        """This method should be called every time through the main loop.

        It handles showing the up, over, and down states of the button.

        Parameters:
            | eventObj - the event object obtained by calling pygame.event.get()

        Returns:
            | False most of the time
            | True when the has toggled the checkbox.

        """

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self.visible:
            # The checkBox only cares bout mouse-related events (or no events, if it is invisible)
            return False

        if not self.isEnabled:
            return False

        clicked = False

        if (not self.mouseOverButton) and self.rect.collidepoint(eventObj.pos):
            # if mouse has entered the checkBox:
            self.mouseOverButton = True


        elif self.mouseOverButton and (not self.rect.collidepoint(eventObj.pos)):
            # if mouse has exited the checkBox:
            self.mouseOverButton = False

        if self.rect.collidepoint(eventObj.pos):

            if eventObj.type == MOUSEBUTTONDOWN:
                self.buttonDown = True
                self.lastMouseDownOverButton = True

        else:
            if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                # if an up/down happens off the checkBox, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False

        if eventObj.type == MOUSEBUTTONDOWN:
            self.mouseIsDown = True
            
        # mouse up is handled whether or not it was over the checkBox
        doMouseClick = False
        if eventObj.type == MOUSEBUTTONUP:
            self.mouseIsDown = False
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False

            if self.buttonDown:
                self.buttonDown = False

            if doMouseClick:
                self.buttonDown = False
                clicked = True
                
                if self.playSoundOnClick:
                    self.soundOnClick.play()

                # switch state:
                self.value = not self.value

        return clicked

    def draw(self):
        """Draws the checkbox."""
        if not self.visible:
            return

        # Blit the current checkbox's image.

        if self.isEnabled:
            if self.mouseIsDown and self.lastMouseDownOverButton and self.mouseOverButton:
                if self.value:
                    self.window.blit(self.surfaceOnDown, self.loc)
                else:
                    self.window.blit(self.surfaceOffDown, self.loc)
            else:
                if self.value:
                    self.window.blit(self.surfaceOn, self.loc)
                else:
                    self.window.blit(self.surfaceOff, self.loc)


        else:
            if self.value:
                self.window.blit(self.surfaceOnDisabled, self.loc)
            else:
                self.window.blit(self.surfaceOffDisabled, self.loc)


    def getValue(self):    # This is the key method for getting the current value of the checkbox
        """Returns the value of the checkbox  (True/False)."""
        return self.value

    def setValue(self, trueOrFalse):
        """Sets a new value for the checkBox to the value passed in."""
        self.value = trueOrFalse


class TextCheckBox(PygWidgetsCheckBox):
    """Builds a checkbox with a default text appearance.

    Each TextCheckBox has six states:  on, off, onDown, offDown, onDisabled, and offDisabled

    Typical use:

    1) Create a TextCheckBox (giving a window and a loc (left, top)):

        myCheckBox = pygwidgets.TextCheckBox(window, (500, 430), True, 'Text Nickname')

        There are many optional parameters, that have good defaults.

    2) In your big loop, check for the button being clicked by calling its handleEvent method:

        if myCheckBox.handleEvent(event):  # When clicked on to toggle, this returns True
            #  CheckBox was clicked, do whatever you want here

    3) At the bottom of your big loop, draw the checkBox:

        myCheckBox.draw()

    Parameters:
        | window - the window to draw the checkbox in
        | loc - a tuple specifying the upper left corner to draw the checkbox on the surface
    Optional keyword parameters:
        | value - True for on, False for off (default is True)
        | size - used for both the width and the height (assuming a square box) - (default is 20 pixels)
        | edgeColor - the rgb color of the edges of the checkBox. (default is black)
        | insideColor = the rgb color of the inside of the checkBox.  (default is white)
        | insideDownColor - the background rgb color of down button (default is a light gray)
        | textColor - the rgb color of the text word next to the checkbox (default is black)
        | soundOnClick - a path to a sound effect file. Plays when the checkbox is clicked (defaults to None)
        | nickname - any name you want to use to identify this button (default is None)
        | callBack - a function or object.method to call when the button is clicked (default is None)


    """
    DEFAULT_FONT_NAME = None # use pygame default font
    DEFAULT_FONT_SIZE = 20
    PYGWIDGETS_FONT = pygame.font.Font(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)


    def __init__(self, window, loc, text='', value=True, size=16, edgeColor=PYGWIDGETS_BLACK, insideColor=PYGWIDGETS_WHITE,\
                 insideDownColor=PYGWIDGETS_OVER_GRAY, textColor=PYGWIDGETS_BLACK, soundOnClick=None, nickname=None, callBack=None):

        self.edgeColor = edgeColor
        self.insideColor = insideColor
        self.insideDownColor = insideDownColor
        self.textColor = textColor
        if nickname is None:
            nickname = text  # use the text on the button as the internal name

        # Create the button's surfaces.

        self.font = TextCheckBox.PYGWIDGETS_FONT
        self.fontHeight = self.font.size('Anything')[1]  # returns a tuple of (width, height)

        if text == '':
            actualWidth = size
            actualHeight = size
            textSurface = None
            textSurfaceGray = None
            textOffset = 0
        else:
            textSurface = self.font.render(text, True, self.textColor)
            textSurfaceGray = self.font.render(text, True, PYGWIDGETS_DISABLED_GRAY)
            thisRect = textSurface.get_rect()
            textOffset = size + 4  # to offset from checkbox, where to start the text
            actualWidth = thisRect.width + textOffset

            if size > self.fontHeight:
                actualHeight = size
            else:
                actualHeight = self.fontHeight

        checkBoxRect = pygame.Rect(loc[0], loc[1], actualWidth, actualHeight)

        w = size  # syntactic sugar
        h = size  # syntactic sugar
        boxSize = (actualWidth, actualHeight)

        # draw the On checkBox, with an X across it to show On state
        surfaceOn = pygame.Surface(boxSize, pygame.SRCALPHA, 32)
        pygame.draw.rect(surfaceOn, self.insideColor, pygame.Rect(0, 0, w, h), 0)  # fill the box with inside color
        pygame.draw.rect(surfaceOn, PYGWIDGETS_BLACK, pygame.Rect(0, 0, w, h), 1)  # black border around everything
        pygame.draw.line(surfaceOn, PYGWIDGETS_BLACK, (0, 0), (w - 2, h - 1), 2)
        pygame.draw.line(surfaceOn, PYGWIDGETS_BLACK, (0, h), (w - 2, 0), 2)
        if text != '':
            surfaceOn.blit(textSurface, (textOffset, 0))
            surfaceOn = pygame.Surface.convert_alpha(surfaceOn)  # optimizes blitting

        # draw the Off checkBox
        surfaceOff = pygame.Surface(boxSize, pygame.SRCALPHA, 32)
        pygame.draw.rect(surfaceOff, self.insideColor, pygame.Rect(0, 0, w, h), 0)  # fill the box with inside color
        pygame.draw.rect(surfaceOff, PYGWIDGETS_BLACK, pygame.Rect(0, 0, w, h), 1)  # black border around everything
        if text != '':
            surfaceOff.blit(textSurface, (textOffset, 0))
            surfaceOff = pygame.Surface.convert_alpha(surfaceOff)  # optimizes blitting

        # draw the OnDown checkBox, with an X across it to show On state
        surfaceOnDown = pygame.Surface(boxSize, pygame.SRCALPHA, 32)
        pygame.draw.rect(surfaceOnDown, self.insideDownColor, pygame.Rect(0, 0, w, h), 0)
        # fill the box with inside color
        pygame.draw.rect(surfaceOnDown, PYGWIDGETS_BLACK, pygame.Rect(0, 0, w, h), 1)  # black border around everything
        pygame.draw.line(surfaceOnDown, PYGWIDGETS_BLACK, (0, 0), (w - 2, h - 1), 2)
        pygame.draw.line(surfaceOnDown, PYGWIDGETS_BLACK, (0, h), (w - 2, 0), 2)
        if text != '':
            surfaceOnDown.blit(textSurface, (textOffset, 0))
            surfaceOnDown = pygame.Surface.convert_alpha(surfaceOnDown)  # optimizes blitting

        # draw the OffDown checkBox
        surfaceOffDown = pygame.Surface(boxSize, pygame.SRCALPHA, 32)
        pygame.draw.rect(surfaceOffDown, self.insideDownColor, pygame.Rect(0, 0, w, h), 0)
        pygame.draw.rect(surfaceOffDown, PYGWIDGETS_BLACK, pygame.Rect(0, 0, w, h), 1)  # black border around everything
        if text != '':
            surfaceOffDown.blit(textSurface, (textOffset, 0))
            surfaceOffDown = pygame.Surface.convert_alpha(surfaceOffDown)  # optimizes blitting

        # draw the OnDisabled checkBox, with an X across it to show On state
        surfaceOnDisabled = pygame.Surface(boxSize, pygame.SRCALPHA, 32)
        pygame.draw.rect(surfaceOnDisabled, PYGWIDGETS_DISABLED_GRAY, pygame.Rect(0, 0, w, h),
                         0)  # fill the box with disabled color
        pygame.draw.rect(surfaceOnDisabled, PYGWIDGETS_DISABLED_GRAY, pygame.Rect(0, 0, w, h), 1)  # black border around everything
        pygame.draw.line(surfaceOnDisabled, PYGWIDGETS_BLACK, (0, 0), (w - 2, h - 1), 2)
        pygame.draw.line(surfaceOnDisabled, PYGWIDGETS_BLACK, (0, h), (w - 2, 0), 2)
        if nickname != '':
            surfaceOnDisabled.blit(textSurfaceGray, (textOffset, 0))
            surfaceOnDisabled = pygame.Surface.convert_alpha(surfaceOnDisabled)  # optimizes blitting

        # draw the OffDisabled checkBox
        surfaceOffDisabled = pygame.Surface(boxSize, pygame.SRCALPHA, 32)
        pygame.draw.rect(surfaceOffDisabled, PYGWIDGETS_DISABLED_GRAY, pygame.Rect(0, 0, w, h),
                         0)  # fill the box with disabled color
        pygame.draw.rect(surfaceOffDisabled, PYGWIDGETS_DISABLED_GRAY, pygame.Rect(0, 0, w, h),
                         1)  # black border around everything
        if text != '':
            surfaceOffDisabled.blit(textSurfaceGray, (textOffset, 0))
            surfaceOffDisabled = pygame.Surface.convert_alpha(surfaceOffDisabled)  # optimizes blitting


        super().__init__(window, loc, checkBoxRect, \
                                             surfaceOn, surfaceOff, \
                                             surfaceOnDown, surfaceOffDown, \
                                             surfaceOnDisabled, surfaceOffDisabled, \
                                             soundOnClick, value, nickname, callBack)


class CustomCheckBox(PygWidgetsCheckBox):
    """CustomCheckBox creates a checkbox with custom images.

    Each CustomCheckBox has six states:  on, off, onDown, offDown, onDisabled, offDisabled

    Only the on and off states need to be specified.
    If left out, the others will default to be a copy of the on and off images.

    Typical use:

    1) Create a CustomCheckBox - giving a location tuple - as (left, top) and at least two images:

        myCheckBox = pygwidgets.CustomButton(window, (500, 430), \
                                on='images/CheckBoxOn.png',
                                off='images/CheckBoxDown.png',
                                value=True)

    2) In your big loop, check for the button being clicked by calling its handleEvent method:

        if myCheckBox.handleEvent(event):  # When clicked on to toggle, this returns True
            #  CheckBox was clicked, do whatever you want here

    3) At the bottom of your big loop, draw the checkBox:

        myCheckBox.draw()

    Parameters:
        | window - the window to draw the checkbox in
        | loc - a tuple specifying the position (upper left corner) for where the checkBox should be drawn.
        | on - a path to a file with the checkBox's on appearance.
        | off - a path to a file with the checkBox's off appearance.
    Optional keyword parameters:
        | value = True for on, False for off (defaults to False)
        | onDown - a path to a file with the checkBox's appearance when the user has clicked on the on image.
        | offDown - a path to a file with the checkBox's appearance when the user has clicked on the off image.
        | onDisabled - a path to a file with the checkBox's on appearance when not clickable.
        | offDisabled - a path to a file with the checkBox's of appearance not clickable.
        | soundOnClick - a path to a sound effects file. Plays when the button is clicked (defaults to None)
        | nickname - Any nickname you want to use to identify this button (default is None)
        | callBack - a function or object.method to call when the button is clicked (default is None)

    """

    def __init__(self, window, loc, on, off, value=False, \
                 onDown=None, offDown=None, onDisabled=None, offDisabled=None,
                 soundOnClick=None, nickname=None, callBack=None):

        surfaceOn = pygame.image.load(on)
        surfaceOff = pygame.image.load(off)

        if onDown is None:
            surfaceOnDown = surfaceOn
        else:
            surfaceOnDown = pygame.image.load(onDown)

        if offDown is None:
            surfaceOffDown = surfaceOff
        else:
            surfaceOffDown = pygame.image.load(offDown)

        if onDisabled is None:
            surfaceOnDisabled = surfaceOn
        else:
            surfaceOnDisabled = pygame.image.load(onDisabled)

        if offDisabled is None:
            surfaceOffDisabled = surfaceOff
        else:
            surfaceOffDisabled = pygame.image.load(offDisabled)


        width, height = surfaceOn.get_size()
        checkBoxRect = pygame.Rect(loc[0], loc[1], width, height)

        # call the PygWidgetsCheckBox superclass to initialize
        super().__init__(window, loc, checkBoxRect, \
                                             surfaceOn, surfaceOff, \
                                             surfaceOnDown, surfaceOffDown, \
                                             surfaceOnDisabled, surfaceOffDisabled, \
                                             soundOnClick, value, nickname, callBack)


#
#
# RADIOBUTTON
#
#
class PygWidgetsRadioButton(PygWidget):
    """PygWidgetsRadioButton is the base class for TextRadioButton and CustomRadioButton

    This class should not be instantiated - it is an abstract class.
    Instead you should create an instance of TextRadioButton or CustomRadioButton.

    """
    #  The following is a class variable (dict) that is used to keep track of all groups of RadioButtons.
    #  Each group has a group name (used as a key), and a list of radioButton objects (as the value).
    #  This makes it easy to send a "turn yourself off" message to all members of a group,
    #     before turning on the selected button.  It also makes it easy to find the currently
    #     selected radioButton, when it is requested.
    __PygWidgets__Radio__Buttons__Groups__Dicts__ = {}


    def __init__(self, window, loc, group, buttonRect, \
                 on, off, onDown, offDown, onDisabled, offDisabled, soundOnClick, value, nickname, callBack):
        """Initializer for PygWidgetsRadioButton."""
        if type(self) is PygWidgetsRadioButton:
            raise Exception('You need to instantiate a TextRadioButton or CustomRadioButton' + \
                            ' (not PygWidgetsRadioButton directly)')

        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.group = group
        self.rect = buttonRect
        self.surfaceOn = on
        self.surfaceOff = off
        self.surfaceOnDown = onDown
        self.surfaceOffDown = offDown
        self.surfaceOnDisabled = onDisabled
        self.surfaceOffDisabled = offDisabled
        self.soundOnClick = soundOnClick
        self.value = value
        self.callBack = callBack
        self.obj = self   # save a reference to ourselves

        # used to track the state of the radioButton
        self.buttonDown = False # is the radioButton currently pushed down?
        self.mouseOverButton = False # is the mouse currently hovering over the radioButton?
        self.lastMouseDownOverButton = False # was the last mouse down event over the mouse button? (Track clicks.)
        if self.soundOnClick is not None:
            self.playSoundOnClick = True
            if type(self.soundOnClick) is str:  # user specified sound path, load it here
                pygame.mixer.init()
                self.soundOnClick = pygame.mixer.Sound(self.soundOnClick)  # save in same instance variable
        else:
            self.playSoundOnClick = False

        self.mouseIsDown = False

        if self.group in PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__:
            # find the group
            thisGroupList = PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__[self.group]
            thisGroupList.append(self.obj)  # add this radio button object to the group
            #  Testing: print('GroupList', self.group, 'is;', thisGroupList)

        else:  # new group, not seen before
            # Add a new group, and set the value to a list of the first object
            PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__[self.group] = [self.obj]



    def handleEvent(self, eventObj):
        """This method should be called every time through the main loop.

        It handles showing the up, over, and down states of the button.

        Parameters:
            | eventObj - the event object obtained by calling pygame.event.get()

        Returns:
            | False most of the time
            | True when the user selects a radio button from the group

        """

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self.visible:
            # The radioButton only cares bout mouse-related events (or no events, if it is invisible)
            return False

        if not self.isEnabled:
            return False

        clicked = False

        if (not self.mouseOverButton) and self.rect.collidepoint(eventObj.pos):
            # if mouse has entered the radioButton:
            self.mouseOverButton = True

        elif self.mouseOverButton and (not self.rect.collidepoint(eventObj.pos)):
            # if mouse has exited the radioButton:
            self.mouseOverButton = False

        if self.rect.collidepoint(eventObj.pos):

            if eventObj.type == MOUSEBUTTONDOWN:
                self.buttonDown = True
                self.lastMouseDownOverButton = True

        else:
            if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                # if an up/down happens off the radioButton, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False

        if eventObj.type == MOUSEBUTTONDOWN:
            self.mouseIsDown = True
            
        # mouse up is handled whether or not it was over the radioButton
        doMouseClick = False
        if eventObj.type == MOUSEBUTTONUP:
            self.mouseIsDown = False
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False

            if self.buttonDown:
                self.buttonDown = False

            if doMouseClick:
                self.buttonDown = False
                clicked = True

                # Turn all radio buttons in this group off
                for radioButton in PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__[self.group]:
                    radioButton.setValue(False)
                self.setValue(True)   # And turn the current one (the one that was clicked) on
                
                if self.playSoundOnClick:
                    self.soundOnClick.play()

        if clicked:
            if self.callBack is not None:
                self.callBack(self.nickname)

        return clicked

    def getSelectedRadioButton(self):
        """Returns the nickname of the currently selected radio button."""
        radioButtonListInGroup = PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__[self.group]
        for radioButton in radioButtonListInGroup:
            if radioButton.getValue():
                selectedNickname = radioButton.getNickname()
                return selectedNickname

        raise Exception('No radio button was selected')

    def draw(self):
        """Draws the current state of the radio button."""
        if not self.visible:
            return

        # Blit the radioButton's appropriate appearance
        if self.isEnabled:
            if self.mouseIsDown and self.lastMouseDownOverButton and self.mouseOverButton:
                if self.value:
                    self.window.blit(self.surfaceOnDown, self.loc)
                else:
                    self.window.blit(self.surfaceOffDown, self.loc)
            else:
                if self.value:
                    self.window.blit(self.surfaceOn, self.loc)
                else:
                    self.window.blit(self.surfaceOff, self.loc)

        else:  # show disabled state
            if self.value:
                self.window.blit(self.surfaceOnDisabled, self.loc)
            else:
                self.window.blit(self.surfaceOffDisabled, self.loc)


    def enable(self, allInGroup=False):
        """Enable the current radio button."""
        super().enable()
        if allInGroup:
            self.enableGroup()

    def enableGroup(self):
        """Enables all radio buttons in the group."""
        radioButtonListInGroup = PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__[self.group]
        for radioButton in radioButtonListInGroup:
            radioButton.enable()  # enable all in this group

    def disable(self, allInGroup=False):
        """Disables the current radio button"""
        super().disable()
        if allInGroup:
            self.disableGroup()  # disable all in this group

    def disableGroup(self):
        """Disables all radio buttons in the group"""
        radioButtonListInGroup = PygWidgetsRadioButton.__PygWidgets__Radio__Buttons__Groups__Dicts__[self.group]
        for radioButton in radioButtonListInGroup:
            radioButton.disable()  # not recursive

    def setValue(self, trueOrFalse):
        """Sets the value of the current radio button True or False."""
        self.value = trueOrFalse

    def getValue(self):
        """Returns the current value of the current radio button (True or False)."""
        return self.value




class TextRadioButton(PygWidgetsRadioButton):
    """Creates a text radio button.

    Each RadioButton has six states:  on, off, onDown, offDown, onDisabled, offDisabled

    Typical use:

    1) Create a RadioButton (giving a window, loc as (left, top), group):

        myRadioButton = pygwidgets.TextRadioButton(window, (500, 430), 'MyRadioButtonGroup')

        There are many optional parameters, that have good defaults.

    2) In your big loop, check for the radioButton being clicked by calling its handleEvent method:

        if myRadioButton.handleEvent(event):  # When clicked on to select, this returns True
            #  RadioButton was clicked, do whatever you want here

    3) At the bottom of your big loop, draw the radioButton:

        myRadioButton.draw()


    Parameters:
        | window - the window to draw the radio button in
        | loc - a tuple specifying the position (upper left corner) for where the radioButton should be drawn.
        | group - a name for the group that this radio button belongs to
        |         (all radio buttons in the group need to use the same group name)
    Optional keyword parameters:
        | value - true for on, False for off  (defaults to False)
        | soundOnClick - Aa path to a sound effect file. Plays when the button is clicked (defaults to None)
        | nickname - a nickname, which is returned when querying (see getSelectedRadioButton)
        | callBack - a function or object.method that is called when this item is clcked


    """
    DEFAULT_FONT_NAME = None # use pygame default font
    DEFAULT_FONT_SIZE = 20
    PYGWIDGETS_FONT = pygame.font.SysFont(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)
    CIRCLE_DIAMETER = 14
    CIRCLE_LINE_WIDTH = 2
    TEXT_OFFSET = 18

    def __init__(self, window, loc, group, text, value=False, soundOnClick=None, nickname=None, callBack=None):


        radius = TextRadioButton.CIRCLE_DIAMETER // 2
        center = TextRadioButton.CIRCLE_DIAMETER // 2
        if nickname is None:
            nickname = text  # use the text on the button as the internal name

        # set up to draw the different states of the radioButton
        self.font = TextRadioButton.PYGWIDGETS_FONT
        self.fontHeight = self.font.size('Anything')[1]   # returns a tuple of (width, height)

        lineSurfaceBlack = self.font.render(text, True, PYGWIDGETS_BLACK)
        lineSurfaceGray = self.font.render(text, True, PYGWIDGETS_DISABLED_GRAY)
        thisRect = lineSurfaceBlack.get_rect()
        actualWidth = thisRect.width + TextRadioButton.TEXT_OFFSET

        if TextRadioButton.CIRCLE_DIAMETER > self.fontHeight:
            actualHeight = TextRadioButton.CIRCLE_DIAMETER
        else:
            actualHeight = self.fontHeight
        thisRect = pygame.Rect(loc[0], loc[1], actualWidth, actualHeight)

        # For each state of the button, create one larger surface, then blit the circle and the text
        # Special flags are needed to set the background alpha as transparent

        # draw the On TextRadioButton
        surfaceOn = pygame.Surface((actualWidth, actualHeight), pygame.SRCALPHA, 32)
        pygame.draw.circle(surfaceOn, PYGWIDGETS_WHITE, (center, center), radius, 0)
        pygame.draw.circle(surfaceOn, PYGWIDGETS_BLACK, (center, center), radius, TextRadioButton.CIRCLE_LINE_WIDTH)
        pygame.draw.circle(surfaceOn, PYGWIDGETS_BLACK, (center, center), 3, 0)
        surfaceOn.blit(lineSurfaceBlack, (TextRadioButton.TEXT_OFFSET, 0))
        surfaceOn = pygame.Surface.convert_alpha(surfaceOn)  # optimizes blitting

        # draw the Off TextRadioButton
        surfaceOff = pygame.Surface((actualWidth, actualHeight), pygame.SRCALPHA, 32)
        pygame.draw.circle(surfaceOff, PYGWIDGETS_WHITE, (center, center), radius, 0)
        pygame.draw.circle(surfaceOff, PYGWIDGETS_BLACK, (center, center), radius, TextRadioButton.CIRCLE_LINE_WIDTH)
        surfaceOff.blit(lineSurfaceBlack, (TextRadioButton.TEXT_OFFSET, 0))
        surfaceOff = pygame.Surface.convert_alpha(surfaceOff)  # optimizes blitting

        # draw the onDown and offDown surfaces
        surfaceOnDown = pygame.Surface((actualWidth, actualHeight), pygame.SRCALPHA, 32)
        pygame.draw.circle(surfaceOnDown, PYGWIDGETS_GRAY, (center, center), radius, 0)
        pygame.draw.circle(surfaceOnDown, PYGWIDGETS_BLACK, (center, center), radius, TextRadioButton.CIRCLE_LINE_WIDTH)
        surfaceOnDown.blit(lineSurfaceBlack, (TextRadioButton.TEXT_OFFSET, 0))
        surfaceOnDown = pygame.Surface.convert_alpha(surfaceOnDown)  # optimizes blitting
        surfaceOffDown = surfaceOnDown   # Copy the same surface as the onDown state

        # draw the OnDisabled radioButton
        surfaceOnDisabled = pygame.Surface((actualWidth, actualHeight), pygame.SRCALPHA, 32)
        pygame.draw.circle(surfaceOnDisabled, PYGWIDGETS_DISABLED_GRAY, (center, center), radius, TextRadioButton.CIRCLE_LINE_WIDTH)
        pygame.draw.circle(surfaceOnDisabled, PYGWIDGETS_DISABLED_GRAY, (center, center), 3, 0)
        surfaceOnDisabled.blit(lineSurfaceGray, (TextRadioButton.TEXT_OFFSET, 0))
        surfaceOnDisabled = pygame.Surface.convert_alpha(surfaceOnDisabled)  # optimizes blitting

        # draw the OffDisabled radioButton
        surfaceOffDisabled = pygame.Surface((actualWidth, actualHeight), pygame.SRCALPHA, 32)
        pygame.draw.circle(surfaceOffDisabled, PYGWIDGETS_DISABLED_GRAY, (center, center), radius, TextRadioButton.CIRCLE_LINE_WIDTH)
        surfaceOffDisabled.blit(lineSurfaceGray, (TextRadioButton.TEXT_OFFSET, 0))
        surfaceOffDisabled = pygame.Surface.convert_alpha(surfaceOffDisabled)  # optimizes blitting

        # call the PygWidgetsRadio superclass to initialize
        super().__init__(window, loc, group, thisRect, \
                                          surfaceOn, surfaceOff, \
                                          surfaceOnDown, surfaceOffDown, \
                                          surfaceOnDisabled, surfaceOffDisabled, \
                                          soundOnClick, value, nickname, callBack)

class CustomRadioButton(PygWidgetsRadioButton):
    """Creates a custom radio button - using custom images.

    CustomRadioButton is a class that allows the user to specify their own images for a radio button.

    Each CustomRadioButton has up to six states:  on, off, onDown, offDown, onDisabled, offDisabled

    Only the on and off states need to be specified.
    If left out, the others will default to copies of the on and off surfaces.

    Typical use:

    1) Create a CustomRadioButton - giving a window, loc as (left, top), a group, and path to two images (on and off):

        myRadioButton = pygwidgets.CustomButton(window, (500, 430), \
                                'MyRadioButtonGroup',
                                'images/CheckBoxOn.png',
                                'images/CheckBoxDown.png')

    2) In your big loop, check for the radioButton being clicked by calling its handleEvent method:

        if myRadioButton.handleEvent(event):  # When clicked on to select, this returns True
            #  RadioButton was clicked, do whatever you want here

    3) At the bottom of your big loop, draw the radioButton:

        myRadioButton.draw()


    Parameters:
        | window - the window to draw the radio button in
        | loc - a tuple specifying the position (upper left corner) for where the radioButton should be drawn.
        | group - a name for the group that this radio button belongs to
        |         (all radio buttons in the group need to use the same group name)
        | on - a path to a file with the radioButton's on appearance.
        | off - a path to a file with the radioButton's off appearance.
    Optional keyword parameters:
        | value - True for selected, False for not selected (defaults to False)
        | onDown - a path to the file with the radioButton's on down appearance. (defaults to copy of on)
        | offDown - a path to the file withthe radioButton's off down appearance.(defaults to copy of off)
        | onDisabled - a path to a file with the radioButton's on appearance when not clickable. (defaults to copy of on)
        | offDisabled - a path to a file with the radioButton's of appearance not clickable. (defaults to copy of off)
        | soundOnClick - a path to a sound effects file. Plays when the button is clicked (defaults to None)
        | nickname - a nickname, which is returned when querying (see getSelectedRadioButton)
        | callBack - a function or object.method that is called when this item is clcked

    """

    def __init__(self, window, loc, group, on, off, value=False, \
                 onDown=None, offDown=None, onDisabled=None, offDisabled=None, \
                 soundOnClick=None, nickname=None, callBack=None):

        surfaceOn = pygame.image.load(on)
        surfaceOff = pygame.image.load(off)
        if onDisabled is None:
            surfaceOnDisabled = surfaceOn
        else:
            surfaceOnDisabled = pygame.image.load(onDisabled)

        if offDisabled is None:
            surfaceOffDisabled = surfaceOff
        else:
            surfaceOffDisabled = pygame.image.load(offDisabled)

        if onDown is None:
            surfaceOnDown = surfaceOn
        else:
            surfaceOnDown = pygame.image.load(onDown)

        if offDown is None:
            surfaceOffDown = surfaceOff
        else:
            surfaceOffDown = pygame.image.load(offDown)

        width, height = surfaceOn.get_size()
        thisRect = pygame.Rect(loc[0], loc[1], width, height)

        # call the PygWidgetsRadio superclass to initialize
        super().__init__(window, loc, group, thisRect, \
                                                surfaceOn, surfaceOff, \
                                                surfaceOnDown, surfaceOffDown, \
                                                surfaceOnDisabled, surfaceOffDisabled, \
                                                soundOnClick, value, nickname, callBack)

#
#
#  DISPLAYTEXT
#
#
class DisplayText(PygWidget):
    """Create a field for displaying text.

    Typical use:

    1) Create a DisplayText field:

          myDisplayText = pygwidgets.DisplayText(myWindow, (100, 200))  # Other optional arguments ...

    2) Whenever you want to change the text to be displayed in your field,
        make this call to the setValue method:

          myDisplayText.setValue('Here is some new text to display')

    3) To show the text field in your window, call the draw method every time through the main loop:

           myDisplayText.draw()

    Parameters:
        | window - The window of the to draw the text into
        | loc - location of where the text should be drawn
    Optional keyword parameters:
        | value - any initial text (defaults to the empty string)
        | fontName - name of font to use (defaults to None)
        | fontSize - size of font to use (defaults to 24)
        | width - width of the input text field (defauls to with of text to draw)
        | height - height of display text field (default to height of text to draw)
        | textColor - rgb color of the text (default to black)
        | backgroundColor - background rgb color of the text (defaults to white)
        | justified - 'left', 'center', or 'right' (defaults to 'left')
        |     Note: If you want center or right justified, you probably want to specify a width value
        |     (Otherwise, with a single text line, you will not see any difference)
        | nickname - a text name to refer to this object (defaults to None)


    Inspired by a similar module written by David Clark (da_clark at shaw.ca)
    Changed parameters, defaults, methods to call, etc.

    """
        

    def __init__(self, window, loc=(0, 0), value='',
                 fontName=None, fontSize=18, width=None, height=None, \
                 textColor=PYGWIDGETS_BLACK, backgroundColor=None, justified='left', nickname=None):


        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.text = None # special trick so that the call to setValue below will force the creation of the text image
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.userHeight = height
        self.userWidth = width
        self.justified = justified
        self.textImage = None

        self.fontHeight = self.font.size('Anything')[1]   # returns a tuple of (width, height)
        if (height is None) and (width is None):
            self.useSpecifiedArea = False
        else:
            self.useSpecifiedArea = True
        self.setValue(value) # Set the initial text for drawing


    def setValue(self, newText):
        """Sets a text value (string) into the text field."""
        newText = str(newText)  #  attempt to convert to string (might be int or float ...)
        if self.text == newText:
            return  # nothing to change

        self.text = newText  # save the new text

        textLines = self.text.splitlines()
        nLines = len(textLines)
        surfacesList = []  # build up a list of surfaces, one for each line of original text
        actualWidth = 0  # will eventually be set the width of longest line

        for line in textLines:
            lineSurface = self.font.render(line, True, self.textColor)
            surfacesList.append(lineSurface)
            thisRect = lineSurface.get_rect()
            if thisRect.width > actualWidth:
                actualWidth = thisRect.width

        heightOfOneLine = self.fontHeight
        actualHeight = nLines * heightOfOneLine
        self.rect = pygame.Rect(self.loc[0], self.loc[1], actualWidth, actualHeight)

        # Create one larger surface, then blit all line surfaces into it
        # Special flags are needed to set the background alpha as transparent
        self.textImage = pygame.Surface((actualWidth, actualHeight), flags=SRCALPHA)
        if self.backgroundColor is not None:
            self.textImage.fill(self.backgroundColor)

        thisLineTop = 0
        for lineSurface in surfacesList:
            if self.justified == 'left':
                self.textImage.blit(lineSurface, (0, thisLineTop))
            else:
                thisSurfaceWidth = lineSurface.get_rect()[2]  # element 2 is the width
                if self.justified == 'center':
                    theLeft = (actualWidth - thisSurfaceWidth) / 2
                elif self.justified == 'right':  # right justified
                    theLeft = actualWidth - thisSurfaceWidth
                else:
                    raise Exception('Value of justified was: ' + self.justified + '. Must be left, center, or right')
                self.textImage.blit(lineSurface, (theLeft, thisLineTop))
            thisLineTop = thisLineTop + heightOfOneLine


        if self.useSpecifiedArea:
            # Fit the text image into a user specified area, may truncate the text off left, right, or bottom
            textRect = self.textImage.get_rect()
            if self.userWidth is None:
                theWidth = textRect.width
            else:
                theWidth = self.userWidth
            if self.userHeight is None:
                theHeight = textRect.height
            else:
                theHeight = self.userHeight

            # Create a surface that is the size that the user asked for
            userSizedImage = pygame.Surface((theWidth, theHeight), flags=SRCALPHA)
            self.rect = pygame.Rect(self.loc[0], self.loc[1], theWidth, theHeight)
            if self.backgroundColor is not None:
                userSizedImage.fill(self.backgroundColor)

            #  Figure out the appropriate left edge within the userSizedImage
            if self.justified == 'left':
                theLeft = 0
            elif self.justified == 'center':
                theLeft = (theWidth - textRect.width) / 2
            else:  # right justified
                theLeft = theWidth - textRect.width

            # Copy the appropriate part from the text image into the user sized image
            # Then re-name it to the textImage so it can be drawn later
            userSizedImage.blit(self.textImage, (theLeft, 0))
            self.textImage = userSizedImage
            self.textImage = pygame.Surface.convert_alpha(self.textImage)  # optimizes blitting

    def setText(self, newText):
        """older name, keeping this for older code that used it, now use setValue"""
        self.setValue(newText)

    def getValue(self):
        """Returns the text entered by the user"""
        return self.text

    def getText(self):
        """older name, now, use getValue above"""
        return self.text

    def getTextImage(self):
        """Returns the current text image"""
        return self.textImage

    def draw(self):
        """Draws the current text in the window"""
        if not self.visible:
            return

        self.window.blit(self.textImage, self.loc)


#
#
# INPUT TEXT
#
#
class InputText(PygWidget):
    """Creates a field where the user enter text (an editable field).
    
    Typical use:

    1) Create an InputText field:

        myInputText = pygwidgets.InputText(myWindow, (100, 200))  # Other optional arguments ...

    2) In your big while loop, call the 'handleEvent' method of the InputText object(s)
        It will return False most of the time, and will return True when the user presses RETURN or ENTER
        Here is the typical code to use:

        if myInputText.handleEvent(event):
            theText = myInputText.getValue()  # call this method to get the text in the field
            # Do whatever you want with theText

    3) To show the text field in your window, call the draw method every time through the main loop:

        myInputText.draw()

    Parameters:
        | window - the window to draw the text field in
        | loc - Location of where the text should be drawn
    Optional keyword parameters:
        | value - any initial text (defaults to the empty string)
        | fontName - name of font to use (defaults to None)
        | fontSize - size of font to use (defaults to 24)
        | width - width of the input text field (defauls to 200 pixels)
        | textColor - rgb color of the text (default to black)
        | backgroundColor - background rgb color of the text (defaults to white)
        | focusColor - rgb color of a rectangle around the text when focused (defaults to black)
        | initialFocus - should this field have focus when at the beginning? (defaults to False)
        |       Note:  Only one field should have focus.
        |              If more than one, all focused fields will get keys
        | mask - a character used to mask the text, typically set to asterisk for password field (defaults to None)

    """

    #  Inspired by (and code borrowed from) NEAROO (Silas Gyger) Found on GitHub dated: 11/14/2014
    #  Any number of InputText fields can now be created, and only one will have focus.
    #  Major rewrite to be object oriented.
    #  Changed parameters, defaults, the way some keys are handled, repeating keys, method names,
    #  ability to click on field to set new cursor spot, etc.


    def __init__(self, window, loc, value='', \
                 fontName=None, fontSize=24, width=200, \
                 textColor=PYGWIDGETS_BLACK, backgroundColor=PYGWIDGETS_WHITE, focusColor=PYGWIDGETS_BLACK, \
                 initialFocus=False, nickname=None, callBack=None, mask=None):

        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.text = value
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.width = width
        self.focus = initialFocus
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.focusColor = focusColor  # color of focus rectangle arount text
        self.nickname = nickname
        self.callBack = callBack
        self.mask = mask

        # Get the height of the field by geting the size of the font
        self.height = self.font.get_height()
        # Set the rect of the text image
        self.imageRect = pygame.Rect(self.loc[0], self.loc[1], self.width, self.height)
        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.width, self.height)
        # Set the rect of the focus highlight rectangle (when the text has been clicked on and has focus)
        self.focusedImageRect = pygame.Rect(self.loc[0] - 3, self.loc[1] - 3, self.width + 6, self.height + 6)

        # Cursor related things:
        self.cursorSurface = pygame.Surface((1, self.height))
        self.cursorSurface.fill(self.textColor)
        self.cursorPosition = len(self.text)  # put the cursor at the end of the initial text
        self.cursorVisible = False
        self.cursorSwitchMs = 500 # Blink every half=second
        self.cursorMsCounter = 0
        self.cursorLoc = [self.loc[0], self.loc[1]]   # this is a list because element 0 will change as the user edits
        self.clock = pygame.time.Clock()


        # Create one surface, blit the text into it during _updateImage
        # Special flags are needed to set the background alpha as transparent
        self.textImage = pygame.Surface((self.width, self.height), flags=SRCALPHA)

        self.currentKey = None
        self.unicodeOfKey = None
        self._updateImage()  # create the image of the starting text

    def _updateImage(self):
        """Internal method to render text as an image."""
        # Fill the background of the image
        if self.backgroundColor is not None:
            self.textImage.fill(self.backgroundColor)

        # Render the text as a single line, and blit it onto the textImage surface
        if self.mask is None:
            lineSurface = self.font.render(self.text, True, self.textColor)
        else:
            nChars = len(self.text)
            maskedText = self.mask * nChars
            lineSurface = self.font.render(maskedText, True, self.textColor)
        self.textImage.blit(lineSurface, (0, 0))


    def handleEvent(self, event):
        """This method should be called every time through the main loop.

        It handles all of the keyboard key actions

        Parameters:
            | eventObj - the event object obtained by calling pygame.event.get()

        Returns:
            | False most of the time
            | True when the user clicks down and later up on the button.

        """

        if not self.isEnabled:
            return False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1): # user clicked
            theX, theY = event.pos
            # if self.imageRect.collidepoint(pos):
            if self.imageRect.collidepoint(theX, theY):
                if not self.focus:
                    self.focus = True   # give this field focus
                else:
                    # Field already has focus, must position the cursor where the user clicked
                    nPixelsFromLeft = theX - self.loc[0]
                    nChars = len(self.text)

                    lastCharOffset = self.font.size(self.text)[0]
                    if nPixelsFromLeft >= lastCharOffset:
                        self.cursorPosition = nChars
                    else:
                        for thisCharNum in range(0, nChars):
                            thisCharOffset = self.font.size(self.text[:thisCharNum])[0]
                            if thisCharOffset >= nPixelsFromLeft:
                                self.cursorPosition = thisCharNum  # Found the proper position for the cursor
                                break
                    self.cursorVisible = True # Show the cursor at the click point

            else:
                self.focus = False


        if not self.focus:  # if this field does not have focus, don't do anything
            return False

        keyIsDown = False  # assume False

        if event.type == pygame.KEYDOWN:
            keyIsDown = True
            self.currentKey = event.key  # remember for potential repeating key
            self.unicodeOfKey = event.unicode # remember for potential repeating key

        if event.type == pygame.USEREVENT:
            # This is a special signal to check for a repeating key
            # if the key is still down, repeat it
            keyPressedList = pygame.key.get_pressed()

            if (self.currentKey is not None) and (keyPressedList[self.currentKey]):  # Key is still down
                keyIsDown = True
            else:
                # Key is up
                pygame.time.set_timer(pygame.USEREVENT, 0)  # kill the timer
                return False


        if keyIsDown:
            if self.currentKey in (pygame.K_RETURN, pygame.K_KP_ENTER):
                # User is done typing, return True to signal that text is available (via a call to getValue)
                self.focus = False
                self.currentKey = None
                self._updateImage()

                if self.callBack is not None:
                    self.callBack(self.nickname)

                return True

            keyIsRepeatable = True  # assume it is repeatable unless specifically turned off
            if self.currentKey == pygame.K_DELETE:
                self.text = self.text[:self.cursorPosition] + \
                        self.text[self.cursorPosition + 1:]
                self._updateImage()

            elif self.currentKey == pygame.K_BACKSPACE:  # forward delete key
                self.text = self.text[:max(self.cursorPosition - 1, 0)] + \
                                    self.text[self.cursorPosition:]

                # Subtract one from cursor_pos, but do not go below zero:
                self.cursorPosition = max(self.cursorPosition - 1, 0)
                self._updateImage()

            elif self.currentKey == pygame.K_RIGHT:
                if self.cursorPosition < len(self.text):
                    self.cursorPosition = self.cursorPosition + 1

            elif self.currentKey == pygame.K_LEFT:
                if self.cursorPosition > 0:
                    self.cursorPosition = self.cursorPosition - 1

            elif self.currentKey == pygame.K_END:
                self.cursorPosition = len(self.text)
                keyIsRepeatable = False

            elif self.currentKey == pygame.K_HOME:
                self.cursorPosition = 0
                keyIsRepeatable = False

            elif self.currentKey in [pygame.K_UP, pygame.K_DOWN]:
                return False   # ignore up arrow and down arrow

            else:  # standard key
                # If no special key is pressed, add unicode of key to input_string
                self.text = self.text[:self.cursorPosition] + \
                                    self.unicodeOfKey + \
                                    self.text[self.cursorPosition:]
                self.cursorPosition = self.cursorPosition + len(self.unicodeOfKey)
                self._updateImage()

            if keyIsRepeatable:  # set up userevent to try to repeat key
                pygame.time.set_timer(pygame.USEREVENT, 200)  # wait for a short time before repeating

        return False


    def draw(self):
        """Draws the Text in the window."""
        if not self.visible:
            return

        # If this input text has focus, draw an outline around the text image
        if self.focus:
            pygame.draw.rect(self.window, self.focusColor, self.focusedImageRect, 1)

        # Blit in the image of text (set earlier in _updateImage)
        self.window.blit(self.textImage, self.loc)

        # If this field has focus, see if it is time to blink the cursor
        if self.focus:
            self.cursorMsCounter = self.cursorMsCounter + self.clock.get_time()
            if self.cursorMsCounter >= self.cursorSwitchMs:
                self.cursorMsCounter = self.cursorMsCounter % self.cursorSwitchMs
                self.cursorVisible = not self.cursorVisible

            if self.cursorVisible:
                cursorOffset = self.font.size(self.text[:self.cursorPosition])[0]
                if self.cursorPosition > 0: # Try to get between characters
                    cursorOffset = cursorOffset - 1
                if cursorOffset < self.width:  # if the loc is within the text area, draw it
                    self.cursorLoc[0] = self.loc[0] + cursorOffset
                    self.window.blit(self.cursorSurface, self.cursorLoc)

            self.clock.tick()


    # Helper methods
    def getValue(self):
        """Returns the text entered by the user"""
        return self.text

    def getText(self):
        """older name, now, use getValue above"""
        return self.text

    def setValue(self, newText):
        """Sets new text into the field"""
        self.text = newText
        self.cursorPosition = len(self.text)
        self._updateImage()

    def setText(self, newText):
        """older name, keeping this for older code that used it, now use setValue"""
        self.setValue(newText)

    def getTextImage(self):
        """Returns the image of the text."""
        return self.textImage

    def clearText(self, keepFocus=False):
        """Clear the text in the field"""
        self.text = ''
        self.focus = keepFocus
        self._updateImage()

    def removeFocus(self):
        """Remove typing focus from this field.

         Might want to call this (and getValue above), if there is some button to say user has finished typing

         """
        self.focus = False


#
#
# DRAGGER
#
#
class Dragger(PygWidget):
    """Dragger - Allows the user to drag an object around in the window.

    Typical use:

    1) Create a Dragger:

        myDragger= pygwidgets.Dragger(myWindow, (100, 200), 'images/DragMe.png')  # Other optional arguments ...

    2) In your big while loop, call the 'handleEvent' method of the Dragger object(s)
        It will return False most of the time, and will return True when the user presses and lifts up on the mouse
        Here is the typical code to use:

        if myDragger.handleEvent(event):
            # print('Done dragging')  # do whatever you want here
            # Could call inherited getRect where dragger was released (and check if it is over a target)

    3) To show the dragger in your window, the typical code is to call the draw method:

        myDragger.draw()


    Parameters:
        | window - the window of the application for the draw method to draw into
        | loc - location of where the dragger image should be drawn
        | up -  path to up image
    Optional keyword parameters:
        | down - path to down image
        | over -  path to over image
        | disabled - path to disabled image
        | nickname - any nickname you want to use to identify this dragger
        | callback - a function or method of an object to call back when done dragging.


    """    
    def __init__(self, window, loc, up, down=None, over=None, disabled=None, nickname=None, callBack=None):

        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        if down is None:
            self.surfaceDown = self.surfaceUp
        else:
            self.surfaceDown = pygame.image.load(down)
        if over is None:
            self.surfaceOver = self.surfaceUp
        else:
            self.surfaceOver = pygame.image.load(over)
        if disabled is None:
            self.surfaceDisabled = self.surfaceUp
        else:
            self.surfaceDisabled = pygame.image.load(disabled)
        self.nickname = nickname
        self.callBack = callBack

        # figure out the rect of the dragger, (used to see if the mouse is within the dragger)
        self.rect = self.surfaceUp.get_rect()
        self.rect.left = self.loc[0]
        self.rect.top = self.loc[1]
        self.startDraggingX = self.rect.left
        self.startDraggingY = self.rect.top
        self.mouseUpLoc = (0, 0)  # some initial value

        # used to track the state of the dragger
        self.mouseOver = False
        self.isEnabled = True
        self.dragging = False
        self.deltaX = 0
        self.deltaY = 0


    def handleEvent(self, eventObj):
        """This method should be called every time through the main loop.

        It handles all of the dragging

        Parameters:
            | eventObj - the event object obtained by calling pygame.event.get()

        Returns:
            | False most of the time
            | True when the user finishes dragging by lifting up on the mouse.

        """
        if not self.isEnabled:
            return False

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) :
            # The dragger only cares about mouse-related events
            return False

        clicked = False
        if eventObj.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(eventObj.pos):
                self.dragging = True
                self.deltaX = eventObj.pos[0] - self.rect.left
                self.deltaY = eventObj.pos[1] - self.rect.top
                self.startDraggingX = self.rect.left
                self.startDraggingY = self.rect.top

        elif eventObj.type == MOUSEBUTTONUP:
            if self.dragging:
                self.dragging = False
                clicked = True
                self.mouseUpLoc = (eventObj.pos[0], eventObj.pos[1])
                self.rect.left = eventObj.pos[0] - self.deltaX
                self.rect.top = eventObj.pos[1] - self.deltaY
                self.setLoc((self.rect.left, self.rect.top))


        elif eventObj.type == MOUSEMOTION:
            if self.dragging:
                self.rect.left = eventObj.pos[0] - self.deltaX
                self.rect.top = eventObj.pos[1] - self.deltaY


            else:
                self.mouseOver = self.rect.collidepoint(eventObj.pos)

        if clicked:
            if self.callBack is not None:
                self.callBack(self.nickname)

        return clicked

    def getMouseUpLoc(self):
        """Returns the location when the user let up on the mouse button."""
        return self.mouseUpLoc

    def resetToPreviousLoc(self):
        """Resets the loc of the dragger to place where dragging started.

        This could be used in a test situation if the dragger was dragged to an incorrect location.

        """
        self.rect.left = self.startDraggingX
        self.rect.top = self.startDraggingY

    def draw(self):
        """Draws the dragger at the current mouse location.

        Should be called in every frame.

        """
        if not self.visible:
            return

        if self.isEnabled:
        
            # Draw the dragger's current appearance to the window.
            if self.dragging:
                self.window.blit(self.surfaceDown, self.rect)
            else:  # mouse is up
                if self.mouseOver:
                    self.window.blit(self.surfaceOver, self.rect)
                else:
                    self.window.blit(self.surfaceUp, self.rect)
        else:
            self.window.blit(self.surfaceDisabled, self.rect)



#
#
# Image
# 
#
class Image(PygWidget):
    """Image - Show an image at a given location.

    Typical use:
    
    1) Create an Image object:

        myImage = pygwidgets.Image(myWindow, (100, 200), 'images/SomeImage.png')

        You can call the inherited getRect tmethod o get the rectangle of the image

    2) To show the Image in your window, the typical code is to call the draw method:

        myImage.draw()

    Parameters:
        | window - The window of the application so the draw method can draw into
        | loc - location of where the image should be drawn
        | pathOrLoadedImage -  path to the image (string), or an image already loaded with pygame.image.load
    Optional keyword parameters:
        | nickname - any nickname you want to use to identify this image

    """
    def __init__(self, window, loc, pathOrLoadedImage, nickname=None):

        super().__init__(nickname)  # initialize base class
        self.window = window
        self.loc = loc
        self.angle = 0
        self.percent = 100
        self.scaleFromCenter = True
        self.flipH = False
        self.flipV = False

        ###  SPECIAL NOTE HERE
        # In the following line of code, I want to call  the "replace" method
        # in the Image class.  Using the following call to specifically reference the "Image"
        # class makes thie work correctly.  I originally had:
        #      self.replace(pathOrLoadedImage)
        # but that failed when used inside the "ImageCollection" subclas, because it was
        # calling the "replace" method inside the ImageCollection class.
        # This solution allows both the Image and ImageCollection classes to have a method named "replace"
        Image.replace(self, pathOrLoadedImage)      # creates self.originalImage
        self.image = self.originalImage.copy()


    def replace(self, newPathOrImage):
        """replace sthe image with a different image.

        Parameters:
            | newPathOrImage - the path to the replacement image to show
            |                  if you specify the empty string(''), the image will go away

        """
        if newPathOrImage == '':  #Create an empty image
            self.rect = pygame.Rect(0, 0, 0, 0)
            size = self.rect.size
            self.originalImage = pygame.Surface(size)
            
        elif isinstance(newPathOrImage, str):
            try:
                self.originalImage = pygame.image.load(newPathOrImage)
            except:
                raise Exception("In Image class, could not open file: " + newPathOrImage)

        else:  # must be an image
            self.originalImage = newPathOrImage
            
        self.image = self.originalImage.copy()



        # Set the rect of the image to appropriate values - using the current image
        # then scale and rotate
        self.rect = self.image.get_rect()
        self.rect.x = self.loc[0]
        self.rect.y = self.loc[1]

        self.scale(self.percent, self.scaleFromCenter)
        self.rotate(self.angle)

    def handleEvent(self, event):
        """If you want to check for a click, this method should be called every time through the main loop.

        It checks to see if the user has done a mouse down on the image.

        Parameters:
            | eventObj - the event object obtained by calling pygame.event.get()

        Returns:
            | False most of the time
            | True when the user clicks down and later up on the button.

        """

        if event.type == MOUSEBUTTONDOWN and self.visible and self.isEnabled:
            if self.rect.collidepoint(event.pos):
                return True

        return False


    def flipHorizontal(self):
        """ flips an image object horizontally
        """
        
        self.flipH = not self.flipH
        self._transmogrophy(self.angle, self.percent, self.scaleFromCenter, self.flipH, self.flipV)

    def flipVertical(self):
        """ flips an image object vertically
        """
        
        self.flipV = not self.flipV
        self._transmogrophy(self.angle, self.percent, self.scaleFromCenter, self.flipH, self.flipV)

    def rotate(self, nDegrees):
        """rotates the image a given number of degrees

        Parameters:
            | nDegrees - the number of degrees you want the image rotated (images start at zero degrees).
            |                  Positive numbers are clockwise, negative numbers are counter-clockwise

        """
        self.angle = self.angle + nDegrees
        self._transmogrophy(self.angle, self.percent, self.scaleFromCenter, self.flipH, self.flipV)


    def rotateTo(self, angle):
        """rotates the image to a given angle

        Parameters:
            | angle - the angle that you want the image rotated to.
            |            Positive numbers are clockwise, negative numbers are counter-clockwise

        """
        self._transmogrophy(angle, self.percent, self.scaleFromCenter, self.flipH, self.flipV)


    def scale(self, percent, scaleFromCenter=True):
        """scales an Image object

        Parameters:
            | percent - a percent of the original size
            |           numbers bigger than 100 scale up
            |           numbers less than 100 scale down
            |           100 scales to the original size
        Optional keyword parameters:
            | scaleFromCenter - should the image scale from the center or from the upper left hand corner
            |           (default is True, scale from the center)

        """
        self._transmogrophy(self.angle, percent, scaleFromCenter, self.flipH, self.flipV)


    def _transmogrophy(self, angle, percent, scaleFromCenter, flipH, flipV):
        """
        Internal method to scale and rotate

        """

        self.angle = angle % 360
        self.percent = percent
        self.scaleFromCenter = scaleFromCenter

        previousRect = self.rect
        previousCenter = previousRect.center
        previousX = previousRect.x
        previousY = previousRect.y

        # Rotate - pygame rotates in the opposite direction
        pygameAngle = -self.angle
        rotatedImage = pygame.transform.rotate(self.originalImage, pygameAngle)
        rotatedRect = rotatedImage.get_rect()
        rotatedWidth = rotatedRect.width
        rotatedHeight = rotatedRect.height

        # Scale
        newWidth = int(rotatedWidth * .01 * self.percent)
        newHeight = int(rotatedHeight * .01 * self.percent)
        self.image = pygame.transform.scale(rotatedImage, (newWidth, newHeight))

        # Flip
        if flipH:
            self.image = pygame.transform.flip(self.image, True, False)
        if flipV:
            self.image = pygame.transform.flip(self.image, False, True)

        # Placement

        self.rect = self.image.get_rect()
        if self.scaleFromCenter:
            self.rect.center = previousCenter

        else:  # use previous X, Y
            self.rect.x = previousX
            self.rect.y = previousY

        self.setLoc((self.rect.left, self.rect.top))


    def getAngle(self):
        return self.angle

    def getSize(self):
        return self.image.get_size()


    def draw(self):
        """Draws the image at the given location."""
        if not self.visible:
            return

        self.window.blit(self.image, self.loc)


#
#
# ImageCollection
#
#
class ImageCollection(Image):
    """ImageCollection - Show an image chosen from a collection of images.

    Typical use:

    1) Create a ImageCollection object:

        myImage = pygwidgets.ImageCollection(myWindow, (100, 200),
         {'image1':'images/SomeImage.png', 'image2':'images/Image2.png', 'image3':'images/Image3.png'},
         'image1')

        or

        myImage = pygwidgets.ImageCollection(myWindow, (100, 200),
         {'image1':'SomeImage.png', 'image2':'Image2.png', 'image3':'Image3.png'},
         'image1', path='images/')



    2) To display a different image, call the replace method, and specify the key of the image to display:

         myImage.replace('image2')

    3) To draw the current image in your window, call the draw method:

        myImage.draw()

    Parameters:
        | window - The window of the application so the draw method can draw into
        | loc - location of where the image should be drawn
        | dictOfImages -  dictionary of key/value pairs of paths to different images
        |        Each value in the dictionary can be either a path or an image already loaded with a call to pygame.load
        |        A key of the empty string ('') is automaticaly added to the dictOfImages - use this key to make the image go away       
        | startImageKey - the key of the first image to be drawn  (This image will show until replace is called)
    Optional keyword parameters:
        | path - any path that you want to prepend to each image  for example,
        |        if all images are in a folder, give the relative path to that folder
        | nickname - any nickname you want to use to identify this ImageCollection

    """

    def __init__(self, window, loc, imagesDict, startImageKey, path='', nickname=None):


        self.window = window
        self.loc = loc
        self.percent = 100
        self.imagesDict = {}

        for key, pathOrLoadedImage in imagesDict.items():
            if isinstance(pathOrLoadedImage, str):
                fullPath = path + pathOrLoadedImage
                try:
                    image = pygame.image.load(fullPath)
                except:
                    print('Problem loading:', fullPath)
                    raise KeyError
            else:
                image = pathOrLoadedImage
            
            self.imagesDict[key] = image


        # Create an empty image and associate it with empty string as the key
        # This allows users to use the empty string to show no image
        zeroRect = pygame.Rect(0, 0, 0, 0)
        size = zeroRect.size
        blankImage = pygame.Surface(size)
        self.imagesDict[''] = blankImage

        if not (startImageKey in self.imagesDict):
            print('The starting image key "', startImageKey, '" was not found in the collection of images dictionary')
            raise KeyError
        startImage = self.imagesDict[startImageKey]

        super().__init__(window, loc, startImage, nickname)  # initialize base class

        self.percent = 100
        self.angle = 0
        self.scaleFromCenter = True
        self.replace(startImageKey)      

    def replace(self, key):
        """Selects a different image to be shown.

        Parameters:
            | key - a key in the original dictionary that specifies which image to show

        """
        if not (key in self.imagesDict):
            print('The key "', key, '" was not found in the collection of images dictionary')
            raise KeyError
        self.originalImage = self.imagesDict[key]
        self.image = self.originalImage.copy()

        # Set the rect of the image to appropriate values - using the current image
        # then scale and rotate
        self.rect = self.image.get_rect()
        self.rect.x = self.loc[0]
        self.rect.y = self.loc[1]

        self.scale(self.percent, self.scaleFromCenter)
        self.rotate(self.angle)


#
#
# PygAnimation
#
#
class PygAnimation(PygWidget):
    """Base class of the Animation class and the SpriteSheetAnimation class

    This is an abstract class. Do not instantiate this class.
    Instead, you should instantiate either an Animation class (using multiple images)
    or a SpriteSheetAnimation (single file made up of equally spaces images).
    Details are in comments for those classes below.

    """

    PLAYING = 'playing'
    PAUSED = 'paused'
    STOPPED = 'stopped'

    def __init__(self, window, loc, loop, nickname, callBack, nTimes):


        if type(self) is PygAnimation:
            raise Exception('You need to instantiate a Animation or SpriteSheetAnimation (not PygAnimation directly)')

        super().__init__(nickname)
        # Iniialize instance variables common to both types of Animations
        self.window = window
        self.loc = loc
        self.loop = loop
        self.nickname = nickname
        self.callBack = callBack
        self.nTimes = nTimes

        self.imagesList = []
        self.endTimesList = []
        self.offsetsList = []
        self.index = 0  # Used to index into all three lists
        self.elasped = 0  # Time that has elapsed in the current animation
        self.nIterationsLeft = 0

    def handleEvent(self, eventObj):
        """This method should be called every time through the main loop.

        Returns:
            False - if no event happens.
            True - if the user clicks the animation to start it playing.
        """
        if not self.visible:
            return
        if not self.isEnabled:
            return False

        if eventObj.type != MOUSEBUTTONDOWN:
            # The animation only cares about a mouse down event
            return False

        eventPointInAnimationRect = self.rect.collidepoint(eventObj.pos)
        if not eventPointInAnimationRect:  # clicked outside of animation
            return False

        if self.state == PygAnimation.PLAYING:  # if playing, ignore the click
            return False

        return True


    def play(self):
        """Starts an animation playing."""
        if self.state == PygAnimation.PLAYING:
            pass  # nothing to do

        elif self.state == PygAnimation.STOPPED:  # restart from beginning of animation
            self.index = 0  # first image in list
            self.elapsed = 0
            self.playingStartTime = time.time()
            self.elapsedStopTime = self.endTimesList[-1]  # end of last animation image time
            self.nextElapsedThreshold = self.endTimesList[0]
            self.nIterationsLeft = self.nTimes  # typically 1

        elif self.state == PygAnimation.PAUSED:  # restart where we left off
            self.playingStartTime = time.time() - self.elapsedAtPause  # recalc start time
            self.elapsed = self.elapsedAtPause
            self.elapsedStopTime = self.endTimesList[-1]  # end of last animation image time
            self.nextElapsedThreshold = self.endTimesList[self.index]

        self.state = PygAnimation.PLAYING

    def stop(self):
        """Stops a a playing animation.  A subsequent call to play will start from the beginning."""
        if self.state == PygAnimation.PLAYING:
            self.index = 0  # set up for first image in list
            self.elapsed = 0
            self.nIterationsLeft = 0

        elif self.state == PygAnimation.STOPPED:
            pass  # nothing to do

        elif self.state == PygAnimation.PAUSED:
            self.index = 0  # set up for first image in list
            self.elapsed = 0

        self.state = PygAnimation.STOPPED

    def pause(self):
        """Pauses a playing animation.  A subsequent call to play will continue where it left off."""
        if self.state == PygAnimation.PLAYING:
            self.elapsedAtPause = self.elapsed
            # only change state if it was playing
            self.state = PygAnimation.PAUSED

        elif self.state == PygAnimation.STOPPED:
            pass  # nothing to do

        elif self.state == PygAnimation.PAUSED:
            pass  # nothing to do

    def update(self):
        """Updates the currently running animation.

        This method should be called in every frame where you want an animation to run.
        Its job is to figure out if it is time to move onto the next image in the animation.

        """
        returnValue = False  # typical return value
        if self.state != PygAnimation.PLAYING:
            return returnValue

        # The job here is to figure out the index of the image to show
        # and the matching elapsed time threshold for the current image
        self.elapsed = (time.time() - self.playingStartTime)

        if self.elapsed > self.elapsedStopTime:  # anim finished
            if self.loop:  # restart the animation
                self.playingStartTime = time.time()
                self.nextElapsedThreshold = self.endTimesList[0]
            else:  # not looping
                self.nIterationsLeft = self.nIterationsLeft - 1
                if self.nIterationsLeft == 0:  # done
                    self.state = PygAnimation.STOPPED
                    if self.callBack != None:  # if there is a callBack
                        self.callBack(self.nickname)  # do it
                    returnValue = True  # animation has ended
                else:  # another iteration - start over again
                    self.playingStartTime = time.time()
                    self.nextElapsedThreshold = self.endTimesList[0]
            self.index = 0

        elif self.elapsed > self.nextElapsedThreshold:
            # Time to move on to next picture
            self.index = self.index + 1
            self.nextElapsedThreshold = self.endTimesList[self.index]

        return returnValue

    def draw(self):
        """Draws the current frame of the animation

        Should be called in every frame.

        """
        # Assumes that self.index has been set earlier (typically in update method)
        # it is used as the index of the current image/endTime/loc
        theImage = self.imagesList[self.index]  # choose the image to show

        if theImage is None:  # if there is no image to show
            return

        if self.visible:
            theOffset = self.offsetsList[self.index]
            theLoc = ((self.loc[0] + theOffset[0]), (self.loc[1] + theOffset[1]))
            self.window.blit(theImage, theLoc)  # show it

    def setLoop(self, trueOrFalse):
        """Sets a value telling the animation if it should loop or not.

        Paramter:
           | trueOrFalse - True to loop, False to not loop.

        """
        self.loop = trueOrFalse

    def getLoop(self):
        """Returns True if the animation is looping, otherwise False."""
        return self.loop


#
#
# ANIMATION
#
#
class Animation(PygAnimation):
    """Shows an animated sequence of images

    Typical use:

    1) Create an Animation object with a list of animation tuples:

        myAnimation = pygwidgets.Animation(window, loc, animTuplesList)

        See below for details and optional parameters.

    2) If you want to allow clicking on the animation to start the animation playing,
        then you need to call the handleEvent method every time through the loop.
        Most of the time it will return False, but will return True when the animation is clicked on.

        if myAnimation.handleEvent(event):
            myAnimation.start()  # tell animation to start playing when clicked on (or anything else)


    3) In your big loop, call the update method to allow the animation to update itself in every frame.
        It figures out when it is time to show the next image.
        It typically returns False, but will return True when the animation finishes.
        If you want to check for the end of the animation, you can check the returned value like this:

        if myAnimation.update():
            # Animation has finished.  Do whatever you want to do here.

        Alternatively, if you specified a callBack, that function or method will be called
        when the animation is finished.

    4) At the bottom of your big loop, draw the animation:

        myAnimation.draw()


    Parameters:
        | window - the window of the application for the draw method to draw into
        | loc - location of where the dragger image should be drawn
        | animTuplesList -  list of tuples, where each tuple looks like this:
        |     (<path to image>, <duration>, <optional offset>)
        |     In most cases you will only need a path and a duration
        |     If an optional offset is given, it is used as an offset from loc

    Optional keyword parameters:
        | autoStart - should the animation start right away (default False)
        | loop -  should the animation loop continuously (default False)
        | nickname -  an internal name to refer to this animation (default None)
        | callBack - function or object.method to call when the animation finishes (default None)
        | nIterations - number of iterations (default 1)

    """

    def __init__(self, window, loc, animTuplesList, autoStart=False, loop=False, \
                 nickname=None, callBack=None, nIterations=1):

        # Takes incoming list of animation tuples and creates three lists:
        # 1) imagesList list of images to show (empty string means no image)
        # 2) endTimesList - list of (elapsed times) when next pic should show
        # 3) offsetsList - list of offsets from the base loc to show each image
        #             if no offset given, use (0, 0) - (most typical)
        #
        # self.state is one of:  PLAYING, PAUSED, STOPPED
        # self.endTimesList is used to decide when it is time to move onto the next image

        super().__init__(window, loc, loop, nickname, callBack, nIterations)

        # Load the images
        endTime = 0
        self.rect = None
        for animTuple in animTuplesList:
            picPath = animTuple[0]
            duration = animTuple[1]
            if len(animTuple) == 2:
                self.offsetsList.append((0, 0))  # use default location - no offset
            else:
                self.offsetsList.append(animTuple[2])  # use specific location offset

            if picPath == '':
                image = None  # special value, meaning no image to show
            else:
                image = pygame.image.load(picPath)  # normal case, load an image
                image = pygame.Surface.convert_alpha(image)  # optimizes blitting
                if self.rect is None:  # first time through the loop - build rect of 1st image
                    thisWidth, thisHeight = image.get_size()
                    self.rect = pygame.Rect(self.loc[0], self.loc[1], thisWidth, thisHeight)

            self.imagesList.append(image)
            endTime = endTime + duration
            self.endTimesList.append(endTime)

        self.state = PygAnimation.STOPPED
        if autoStart:
            self.play()  # start animation playing


#
#
# SPRITESHEETANIMATION
#
#
class SpriteSheetAnimation(PygAnimation):
    """SpriteSheetAnimation.  Use with a single file containing multiple images.

    Typical use:

    1) Create SpriteSheetAnimation specifying a number of parameters:

        myAnimation = pygwidgets.SpriteSheetAnimation(
                                window, loc, imagePath, nCols, nImages, width, height, durationPerImage)

        See below for details and optional parameters.

    2) If you want to allow clicking on the animation to start the animation playing,
        then you need to call the handleEvent method every time through the loop.
        Most of the time it will return False, but will return True when the animation is clicked on

        if myAnimation.handleEvent(event):
            myAnimation.start()  # tell animation to start playing when clicked on (or anything else)


    3) In your big loop, call the update method to allow the animation to update itself in every frame.
        It figures out when it is time to show the next image.
        It typically returns False, but will return True when the animation finishes.
        If you want to check for the end of the animation, you can check the returned value like this:

        if myAnimation.update():
            # Animation has finished.  Do whatever you want to do here.

        Alternatively, if you specified a callBack, that function or method will be called
        when the animation is finished.

    4) At the bottom of your big loop, draw the animation:


        myAnimation.draw()


    Parameters:
        | window - the window of the application for the draw method to draw into
        | loc - location of where the dragger image should be drawn
        | imagePath - path to the file containing multiple images
        | nCols - number of columns in the single file
        | nImages - total number of images in the single file
        | width - width of each individual image
        | height = height of each individual image
        | durationOrDurationsList - two options:
        |     If a single value, then all images will use this duration
        |     If a list or tuple, duration to show each image.
    Optional keyword parameters:
        | autoStart - should the animation start right away (default False)
        | loop -  should the animation loop continuously (default False)
        | nickname -  an internal name to refer to this animation (default None)
        | callBack - function or object.method to call when the animation finishes (default None)
        | nIterations - number of iterations (default 1)

    """

    def __init__(self, window, loc, imagePath, nCols, nImages, width, height, durationOrDurationsList, \
                 autoStart=False, loop=False, nickname=None, callBack=None, nIterations=1):

        # Takes a single SpriteSheet image and breaks it up into multiple images.
        # All images must have the same height and width, and all have the same duration

        # Create three lists:
        # 1) imagesList list of images to show (empty string means no image)
        # 2) endTimesList - list of (elapsed times) when next pic should show
        # 3) offsetsList - list of offsets from the base loc to show each image
        #              if no loc given, use original loc in call (most typical)
        #
        # self.state is one of:  PLAYING, PAUSED, STOPPED
        # self.endTimesList is used to decide when it is time to move onto the next image

        super().__init__(window, loc, loop, nickname, callBack, nIterations)

        # Create images by taking subSurfaces of the sprite sheet
        endTime = 0
        if isinstance(durationOrDurationsList, tuple) or isinstance(durationOrDurationsList, list):
            useSameDuration = False  # this is a list of durations
            if nImages != len(durationOrDurationsList):
                raise Exception('Number of images ' + str(nImages) + \
                                ' and number of duration times ' + str(len(durationOrDurationsList)) + \
                                ' do not match.')

        else:
            useSameDuration = True  # this is a single duration

        self.rect = pygame.Rect(loc[0], loc[1], width, height)

        # Load the sprite sheet.
        spriteSheetImage = pygame.image.load(imagePath)  # .convert()
        spriteSheetImage = pygame.Surface.convert_alpha(spriteSheetImage)  # optimizes blitting

        row = 0
        col = 0
        for imageNumber in range(nImages):
            x = col * height
            y = row * width

            # Create a new blank image
            image = spriteSheetImage.subsurface(x, y, width, height)

            self.imagesList.append(image)
            self.offsetsList.append((0, 0))  # use default location - no offsets

            if useSameDuration:
                endTime = endTime + durationOrDurationsList
            else:
                endTime = endTime + durationOrDurationsList[imageNumber]
            self.endTimesList.append(endTime)

            col = col + 1
            if col == nCols:
                col = 0
                row = row + 1

        # self.nextElapsedThreshold = self.endTimesList[0]  # endpoint for current image
        self.state = PygAnimation.STOPPED
        if autoStart:
            self.play()  # start animation playing
