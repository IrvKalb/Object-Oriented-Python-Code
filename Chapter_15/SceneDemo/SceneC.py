#
# This the Scene C
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *


class SceneC(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.messageField = pygwidgets.DisplayText(self.window, (15, 25), 'This is Scene C', \
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.gotoAButton = pygwidgets.TextButton(self.window, (100, 100), 'Go to Scene A')
        self.gotoBButton = pygwidgets.TextButton(self.window, (250, 100), 'Go to Scene B')
        self.gotoCButton = pygwidgets.TextButton(self.window, (400, 100), 'Go to Scene C')
        self.gotoCButton.disable()

    def getSceneKey(self):
        return SCENE_C

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoAButton.handleEvent(event):
                self.goToScene(SCENE_A)
            if self.gotoBButton.handleEvent(event):
                self.goToScene(SCENE_B)

            # Testing:  Press a or b to send message to those scenes
            #           Press or 1 or 2 to get data from A and B
            #           Press x to send message to all scenes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.send(SCENE_A, 'message', 'Sending message to Scene A')

                if event.key == pygame.K_b:
                    self.send(SCENE_B, 'message', 'Sending message to Scene B')

                if event.key == pygame.K_1:
                    answer = self.request(SCENE_A, 'get data')
                    print('Recevied data from Scene A')
                    print('Answer was:', answer)

                if event.key == pygame.K_2:
                    answer = self.request(SCENE_B, 'get data')
                    print('Recevied data from Scene B')
                    print('Answer was:', answer)

                if event.key == pygame.K_x:
                    self.sendAll('all message', 'Sending message to All scenes')

    def draw(self):
        self.window.fill(GRAYC)
        self.messageField.draw()
        self.gotoAButton.draw()
        self.gotoBButton.draw()
        self.gotoCButton.draw()

    def receive(self, msgType, data):
        print('In C')
        print('Received a message of type:', msgType)
        print('The data received was:', data)

    def respond(self, msgType):
        if msgType == 'get data':
            return 'Here is data from scene C'
