#  Demo of pygwidgets capabilities
#
#  4/17  Developed by Irv Kalb

# 1 - Import libraries
import os
import sys
# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
from pygame.locals import *
import pygwidgets


# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30

# The function and Test class and method below are not required.
# These are only here as a demonstration of how you could use a callback approach to handling events if you want to.

# Define a function to be used as a "callBack"
def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, a button was clicked')
    else:
        print('In myFunction, the button named', theNickname, 'was clicked')

# Define a class with a method to be used as a "callBack"
class Test():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('In myMethod, a button was clicked')
        else:
            print('In myMethod, the button named', theNickname, 'was clicked')


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # set the speed (frames per second)
oTest = Test()
 
# 4 - Load assets: image(s), sounds,  etc.
backgroundImage = pygwidgets.Image(window, (0, 0), 'images/background1.jpg')
displayTextTitle = pygwidgets.DisplayText(window, (0, 20), 'pygwidgets example by Irv Kalb', \
                                    fontSize=36, width= 640, textColor=BLACK, justified='center')

inputTextA = pygwidgets.InputText(window, (20, 100), 'Default input text',\
                                    textColor=WHITE, backgroundColor=BLACK,
                                    fontSize=24, width=250)

inputTextB = pygwidgets.InputText(window, (20, 200), initialFocus=True,\
                                    textColor=(0, 0, 255),
                                    fontSize=28)  # add: , mask='*' for passwords


displayTextA = pygwidgets.DisplayText(window, (20, 300), 'Here is some display text', \
                                    fontSize=24, textColor=WHITE, justified='center')

displayTextB = pygwidgets.DisplayText(window, (20, 400), 'Here is some display text', \
                                    fontSize=24, textColor=BLACK, backgroundColor=WHITE)

restartButton = pygwidgets.CustomButton(window, (100, 430), \
                                    'images/RestartButtonUp.png',
                                    down='images/RestartButtonDown.png',
                                    over='images/RestartButtonOver.png',
                                    disabled='images/RestartButtonDisabled.png',
                                    soundOnClick='sounds/blip.wav',
                                    nickname='RestartButton',
                                    callBack=myFunction)  #  callBack here is not required

# checkBoxA controls the availability of checkBoxB and checkBoxC
# checkBoxB will control the availiability the custom radio buttons
# checkBoxC will control the availiability of the text radio buttons
# checkBoxA and checkBoxC are text checkboxes, checkboxB is a custom checkBox

checkBoxA = pygwidgets.TextCheckBox(window, (410, 80), 'Allow Check Boxes')

checkBoxB = pygwidgets.CustomCheckBox(window, (450, 110), value=True,
                            on='images/checkBoxOn.png', off='images/checkBoxOff.png', \
                            onDown='images/checkBoxOnDown.png', offDown='images/checkBoxOffDown.png', \
                            onDisabled='images/checkBoxOnDisabled.png', offDisabled='images/checkBoxOffDisabled.png')

radioCustom1 = pygwidgets.CustomRadioButton(window, (500, 150), 'Custom Group', \
                            on='images/RadioLowOn.png', off='images/RadioLowOff.png', \
                            onDown='images/RadioLowOnDown.png', offDown='images/RadioLowOffDown.png', \
                            onDisabled='images/RadioLowOnDisabled.png', offDisabled='images/RadioLowOffDisabled.png', \
                            value=True, nickname='Low')

radioCustom2 = pygwidgets.CustomRadioButton(window, (500, 190), 'Custom Group', \
                            on='images/RadioMedOn.png', off='images/RadioMedOff.png', \
                            onDown='images/RadioMedOnDown.png', offDown='images/RadioMedOffDown.png', \
                            onDisabled='images/RadioMedOnDisabled.png', offDisabled='images/RadioMedOffDisabled.png', \
                            value=False, nickname='Med')

radioCustom3 = pygwidgets.CustomRadioButton(window, (500, 230), 'Custom Group', \
                            on='images/RadioHighOn.png', off='images/RadioHighOff.png', \
                            onDown='images/RadioHighOnDown.png', offDown='images/RadioHighOffDown.png', \
                            onDisabled='images/RadioHighOnDisabled.png', offDisabled='images/RadioHighOffDisabled.png', \
                            value=False, nickname='High')

checkBoxC = pygwidgets.TextCheckBox(window, (450, 295), 'Allow Radio Buttons')

radioText1 = pygwidgets.TextRadioButton(window, (500, 320), 'Default Group', 'Radio Text 1', \
                                      value=False)

radioText2 = pygwidgets.TextRadioButton(window, (500, 360), 'Default Group', 'Radio Text 2', \
                                      value=True)

radioText3 = pygwidgets.TextRadioButton(window, (500, 400), 'Default Group', 'Radio Text 3', \
                                      value=False)

statusButton = pygwidgets.TextButton(window, (500, 430), 'Show Status',
                                     callBack=oTest.myMethod)  # callBack here is not required

myDragger = pygwidgets.Dragger(window, (300, 200), 
                        'images/dragMeUp.png', \
                        'images/dragMeDown.png', \
                        'images/dragMeOver.png', \
                        'images/dragMeDisabled.png', \
                        nickname='My Dragger')

pythonIcon = pygwidgets.Image(window, (15, 500), 'images/pythonIcon.png')

myImages = pygwidgets.ImageCollection(window, (400, 490), \
                                {'start':'imageStart.jpg', \
                                 'left':'imageLeft.jpg', \
                                 'right':'imageRight.jpg', \
                                 'up':'imageUp.jpg', \
                                 'down':'imageDown.jpg'}, \
                                'start', path='images/')

myImagesInstructions = pygwidgets.DisplayText(window, (400, 595), 'Click then type l, r, d, u, s, or Space')


iconInstructions = pygwidgets.DisplayText(window, (15, 595),
                                          'Click then up or down arrow to resize,\n' + \
                                          'left or right arrow to rotate, \n' + \
                                          'h or v to flip horizontal or vertical')

frisbeeImage = pygwidgets.Image(window, (562, 2), 'images/frisbee.png')



# 5 - Initialize variables
counter = 0

angle = 0
pct = 100

# 6 - Loop forever
while True:

    # 7 - Check for and handle events

    for event in pygame.event.get():
       # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if inputTextA.handleEvent(event):  # pressed Return or Enter
            theText = inputTextA.getValue()
            print('The text of inputTextA is: ' + theText)

        if inputTextB.handleEvent(event):  # pressed Return or Enter
            theText = inputTextB.getValue()
            print('The text of inputTextB is: ' + theText)

        if restartButton.handleEvent(event):  # clicked
            counter = 0
            print('Content of first input text is:', inputTextA.getValue())
            print('Content of second input text is:', inputTextB.getValue())

        if checkBoxA.handleEvent(event):  # toggled
            A_OnOrOff = checkBoxA.getValue()
            checkBoxA.enableDependents = A_OnOrOff
            print('checkBoxA was clicked, new value is:', A_OnOrOff)

            if A_OnOrOff:
                checkBoxB.enable()
                checkBoxC.enable()
            else:
                checkBoxB.disable()
                checkBoxC.disable()

        if checkBoxB.handleEvent(event):  # toggled
            B_OnOrOff = checkBoxB.getValue()
            checkBoxB.enableDependents = B_OnOrOff
            print('checkBoxB was clicked, new value is:', B_OnOrOff)
            if B_OnOrOff:
                radioCustom1.enable()
                radioCustom2.enable()
                radioCustom3.enable()
            else:
                radioCustom1.disable()
                radioCustom2.disable()
                radioCustom3.disable()
        if radioCustom1.handleEvent(event):  # selected
            print('Radio button custom1 was clicked')

        if radioCustom2.handleEvent(event):  # selected
            print('Radio button custom2 was clicked')

        if radioCustom3.handleEvent(event):  # selected
            print('Radio button custom3 was clicked')

        if checkBoxC.handleEvent(event):  # toggled
            C_OnOrOff = checkBoxC.getValue()
            checkBoxC.enableDependents = C_OnOrOff
            print('checkBoxC was clicked, new value is:', C_OnOrOff)
            if C_OnOrOff:
                radioText1.enableGroup()  # disable all buttons in this group
                # could alternatively have have used (does the same as):
                # radioText1.enable()
                # radioText2.enable()
                # radioText3.enable()
            else:
                radioText1.disableGroup()    # enable all radio buttons in group that contains this radio button
                # could alternatively have used (does the same as):
                # radioText1.disable()
                # radioText2.disable()
                # radioText3.disable()

        if radioText1.handleEvent(event):  # selected
            print('Radio button text1 was clicked')

        if radioText2.handleEvent(event):  # selected
            print('Radio button text2 was clicked')

        if radioText3.handleEvent(event):  # selected
            print('Radio button text3 was clicked')

        if statusButton.handleEvent(event):  # clicked
            nickname = radioCustom1.getSelectedRadioButton()
            print('The currently selected custom Radio Button is:', nickname)
            nickname = radioText1.getSelectedRadioButton()
            print('The currently selected Text Radio Button is:', nickname)

        if myDragger.handleEvent(event):
            print('Done dragging, dragger nickname was:', myDragger.getNickname())
            print('  Mouse up at:', myDragger.getMouseUpLoc())
            print('  Dragger is now located at', myDragger.getLoc())

        if myImages.handleEvent(event):
            print('Got click on image collection at', event.pos)

        if frisbeeImage.handleEvent(event):
            print('Got click on the frisbee image at', event.pos)



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                myImages.replace('left')
            elif event.key == pygame.K_r:
                myImages.replace('right')
            elif event.key == pygame.K_u:
                myImages.replace('up')
            elif event.key == pygame.K_d:
                myImages.replace('down')
            elif event.key == pygame.K_s:
                myImages.replace('start')
            elif event.key == pygame.K_SPACE:
                myImages.replace('')

            elif event.key == pygame.K_h:
                pythonIcon.flipHorizontal()
            elif event.key == pygame.K_v:
                pythonIcon.flipVertical()

    keyPressedList = pygame.key.get_pressed()
    if keyPressedList[pygame.K_LEFT]:
        pythonIcon.rotate(-5)
    if keyPressedList[pygame.K_RIGHT]:
        pythonIcon.rotate(5)

        # If we wanted to keep track of the angle, we could start with:  angle = 0
        # Then for every left arrow:  angle = angle + 5
        # and for every right arrow:  angle = angle - 5
        # Finally, call:  pythonIcon.rotateTo
    if keyPressedList[pygame.K_UP]:
        scaleFromCenter = not (keyPressedList[pygame.K_LSHIFT] or keyPressedList[pygame.K_RSHIFT])
        pct = pct + 10
        pythonIcon.scale(pct, scaleFromCenter=scaleFromCenter)
        #print('Scaling up to', pct, '%')
    if keyPressedList[pygame.K_DOWN]:
        scaleFromCenter = not (keyPressedList[pygame.K_LSHIFT] or keyPressedList[pygame.K_RSHIFT])
        if pct > 0:
            pct = pct - 10
        pythonIcon.scale(pct, scaleFromCenter=scaleFromCenter)
        #print('Scaling down to', pct, '%')


       


    # 8  Do any "per frame" actions
    counter = counter + 1
    displayTextA.setValue('Here is some centered display text.\n' + \
                         'Showing the \nnumber of frames.\nLoop    counter:' + str(counter))
    displayTextB.setValue('Here is some display text.  Loop counter:' + str(counter))
    
    # 9 - Clear the screen
    backgroundImage.draw()

    # 10 - Draw all screen elements
    pythonIcon.draw()
    displayTextTitle.draw()
    inputTextA.draw()
    inputTextB.draw()
    displayTextA.draw()
    displayTextB.draw()
    restartButton.draw()
    checkBoxA.draw()
    checkBoxB.draw()
    radioCustom1.draw()
    radioCustom2.draw()
    radioCustom3.draw()
    checkBoxC.draw()
    radioText1.draw()
    radioText2.draw()
    radioText3.draw()
    statusButton.draw()
    myDragger.draw()
    myImages.draw()
    frisbeeImage.draw()
    myImagesInstructions.draw()
    iconInstructions.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
