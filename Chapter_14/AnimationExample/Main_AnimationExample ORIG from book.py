# Animation Example
# Shows examples of Animation and SpriteSheetAnimation objects

# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets

# 2 Define constants
SCREEN_WIDTH = 640
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
oTitleText = pygwidgets.DisplayText(window, (110, 80), \
                                    'Animations                      SpriteSheetAnimations', fontSize=32)
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


    # 8 - Do any "per frame" actions
    if oTRexAnimation.update():
        print('In main code - TRex animation ended')
    if oDinosaurAnimation.update():
        print('In main code - Dinosaur animation ended')
    if oEffectAnimation.update():
        print('In main code - Effect animation ended')
    if oWalkAnimation.update():
        print('In main code - Walk animation ended')

    # 9 - Clear the window
    window.fill(BGCOLOR)

    # 10 - Draw all window elements
    oTitleText.draw()
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

    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
