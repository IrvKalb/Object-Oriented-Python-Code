# Animation Example
# Shows examples of Animation and SpriteSheetAnimation objects

# 11/24 Fixed a bug pointed out by Ruth Callender, in identifying if the SpriteSheetAnimationCollection class is available in the version of pygwidgets being used.

# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets
# Updated to add example of AnimationCollection
from Player import *

# 2 Define constants
SCREEN_WIDTH = 1060
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (220, 220, 220)

# Define an example function to be used as a "callback"
def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, animation ended')
    else:
        print('In myFunction, the animation with the nickname', theNickname, 'ended')

# Define an example class with an example method to be used as a "callback"
class CallBackTest():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('In myMethod, animation ended')
        else:
            print('In myMethod, the animation named', theNickname, 'ended')

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: images(s), sounds, etc.
dinosaurAnimList = [('images/Dinowalk/f1.png', .1),
                      ('images/Dinowalk/f2.png', .1),
                      ('images/Dinowalk/f3.png', .1),
                      ('images/Dinowalk/f4.png', .1),
                      ('images/Dinowalk/f5.png', .1),
                      ('images/Dinowalk/f6.png', .1),
                      ('images/Dinowalk/f7.png', .1),
                      ('images/Dinowalk/f8.png', .1),
                      ('images/Dinowalk/f9.png', .1),
                      ('images/Dinowalk/f10.png', .1),
                      ('images/Dinowalk/f11.png', .1),
                      ('images/Dinowalk/f12.png', .1),
                      ('images/Dinowalk/f13.png', .1),
                      ('images/Dinowalk/f14.png', .1),
                      ('images/Dinowalk/f15.png', .1),
                      ('images/Dinowalk/f16.png', .1),
                      ('images/Dinowalk/f17.png', .1)]

# TRex
TRexAnimationList = [('images/TRex/f1.gif', .1),
                      ('images/TRex/f2.gif', .1),
                      ('images/TRex/f3.gif', .1),
                      ('images/TRex/f4.gif', .1),
                      ('images/TRex/f5.gif', .1),
                      ('images/TRex/f6.gif', .1),
                      ('images/TRex/f7.gif', .1),
                      ('images/TRex/f8.gif', .1),
                      ('images/TRex/f9.gif', .1),
                      ('images/TRex/f10.gif', .1)]

# 5 - Initialize variables
oCallBackTest = CallBackTest() # instantiate a test object
oTitleText1 = pygwidgets.DisplayText(window, (110, 80), \
                                    'Animations                      SpriteSheetAnimations                    AnimationCollection', \
                                    fontSize=32)
oTitleText2 = pygwidgets.DisplayText(window, (110, 310), \
                                    '                                                                                          SpriteSheetAnimationCollection', \
                                    fontSize=32)
oDinosaurAnimation = pygwidgets.Animation(window, (22, 145), dinosaurAnimList,
                                     autoStart=True, loop=False, callBack=myFunction, nickname='Dinosaur')
oPlayButton = pygwidgets.TextButton(window, (20, 240), "Play")
oPauseButton = pygwidgets.TextButton(window, (20, 280), "Pause")
oStopButton = pygwidgets.TextButton(window, (20, 320), "Stop")
oLoopCheckBox = pygwidgets.TextCheckBox(window, (20, 370), "Loop", value=False)
oShowCheckBox = pygwidgets.TextCheckBox(window, (20, 400), "Show", value=True)

oTRexAnimation = pygwidgets.Animation(window, (180, 140), TRexAnimationList, \
                                       autoStart=False, loop=False, nIterations=3, callBack=oCallBackTest.myMethod)
oInstructionsText = pygwidgets.DisplayText(window, (160, 320), '(Click image to activate)')

oEffectAnimation = pygwidgets.SpriteSheetAnimation(window, (400, 150), 'images/effect_010.png',
                                         35, 192, 192, .1, autoStart=True, loop=True)

oWalkAnimation = pygwidgets.SpriteSheetAnimation(window, (460, 335), 'images/male_walkcycle.png',
                            36, 64, 64, \
                            (.1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3, \
                             .1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3), \
                             autoStart=False, loop=False)

#if '1.0.3' in pygwidgets.getVersion():
if not hasattr(pygwidgets, 'SpriteSheetAnimationCollection'):
    oPlayer = pygwidgets.DisplayText(window, (740, SCREEN_HEIGHT * .333), 'Available in pygwidgets 1.1', fontSize=24)
    oRunAnimation = pygwidgets.DisplayText(window, 740, SCREEN_HEIGHT * .666, 'Available in pygwidgets 1.1', fontSize=24)
    oCollectionsInstructionsText1 = pygwidgets.DisplayText(window, (750, 300), '')
    oCollectionsInstructionsText2 = pygwidgets.DisplayText(window, (750, 500), '')
    animCollectionsAvailable = False
else:
    oPlayer = Player(window, (800, SCREEN_HEIGHT * .333))
    # Build a dictionary of sprite sheet animations, Each key value pair looks like this:
    #      <someKey>:(<imagePath>, <nImages>, <width>, <height>, <durationsOrDurationsList>)
    animationCollectionDict = {'right' : ('images/runRight.png', 10, 30, 40, .1),
                                           'left' : ('images/runLeft.png', 10, 30, 40, .1)}

    # Create a SpriteSheetAnimationCollection object with multiple sprite sheet animations
    oRunAnimation = pygwidgets.SpriteSheetAnimationCollection(window, (810, SCREEN_HEIGHT * .75),
                                                            animationCollectionDict, 'right', autoStart=True, loop=True)
    oCollectionsInstructionsText1 = pygwidgets.DisplayText(window, (750, 250), '(Press left, up, right, down to move)')
    oCollectionsInstructionsText2 = pygwidgets.DisplayText(window, (750, 420), '(Press "l" to run left, or "r" to run right)')
    animCollectionsAvailable = True


oStartButton = pygwidgets.TextButton(window, (440, 400), "Start")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.start()

        if oPauseButton.handleEvent(event):
            oDinosaurAnimation.pause()

        if oStopButton.handleEvent(event):
            oDinosaurAnimation.stop()

        if oLoopCheckBox.handleEvent(event):
            currentLoopState = oDinosaurAnimation.getLoop()
            oDinosaurAnimation.setLoop(not currentLoopState)

        if oShowCheckBox.handleEvent(event):
            showState = oDinosaurAnimation.getVisible()
            if showState:
                oDinosaurAnimation.hide()
            else:
                oDinosaurAnimation.show()

        if oStartButton.handleEvent(event):
            oWalkAnimation.start()

        if oDinosaurAnimation.handleEvent(event):
            oDinosaurAnimation.start()

        if oTRexAnimation.handleEvent(event):
            oTRexAnimation.start()

        if event.type == pygame.KEYDOWN:
            # Allow the user to press left and right keys to switch animations
            if event.key == pygame.K_l and  animCollectionsAvailable:
                oRunAnimation.replace('left')
            elif event.key == pygame.K_r and  animCollectionsAvailable:
                oRunAnimation.replace('right')
            else:
                oPlayer.handleEvent(event)  # send it to the Player animation
 

        elif event.type == pygame.KEYUP:
            oPlayer.handleEvent(event)

    # 8 - Do any "per frame" actions
    if oTRexAnimation.update():
        print('In main code - TRex animation ended')
    if oDinosaurAnimation.update():
        print('In main code - Dinosaur animation ended')
    if oEffectAnimation.update():
        print('In main code - Effect animation ended')
    if oWalkAnimation.update():
        print('In main code - Walk animation ended')
    if animCollectionsAvailable:
        playerX, playerY = oPlayer.update()
        oRunAnimation.update()

    # 9 - Clear the window
    window.fill(BGCOLOR)

    # 10 - Draw all window elements
    oTitleText1.draw()
    oTitleText2.draw()
    oDinosaurAnimation.draw()
    oPlayButton.draw()
    oPauseButton.draw()
    oStopButton.draw()
    oLoopCheckBox.draw()
    oShowCheckBox.draw()
    oTRexAnimation.draw()
    oInstructionsText.draw()
    oEffectAnimation.draw()
    oWalkAnimation.draw()
    oStartButton.draw()
    oCollectionsInstructionsText1.draw()
    oCollectionsInstructionsText2.draw()
    oPlayer.draw()
    oRunAnimation.draw()

    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
