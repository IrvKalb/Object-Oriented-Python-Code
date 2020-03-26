#
# This the Scene B
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *


class SceneB(pyghelpers.Scene):
    def __init__(self, window, sceneKey):
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey

        self.messageField = pygwidgets.DisplayText(self.window, (15, 25), 'This is Scene B', \
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.gotoAButton = pygwidgets.TextButton(self.window, (100, 100), 'Go to Scene A')
        self.gotoCButton = pygwidgets.TextButton(self.window, (400, 100), 'Go to Scene C')


    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoAButton.handleEvent(event):
                self.goToScene(SCENE_A)

            if self.gotoCButton.handleEvent(event):
                self.goToScene(SCENE_C)

            # Testing:  Press a or c to send message to those scenes
            #           Press or 1 or 3 to get data from A and C
            #           Press x to send message to all scenes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.send(SCENE_A, 'message', 'Sending message to Scene A')

                if event.key == pygame.K_c:
                    self.send(SCENE_C, 'message', 'Sending message to Scene C')

                if event.key == pygame.K_1:
                    answer = self.request(SCENE_A, 'get data')
                    print('Recevied data from Scene A')
                    print('Answer was:', answer)

                if event.key == pygame.K_3:
                    answer = self.request(SCENE_C, 'get data')
                    print('Recevied data from Scene C')
                    print('Answer was:', answer)

                if event.key == pygame.K_x:
                    self.sendAll('all message', 'Sending message to All scenes')

    def draw(self):
        self.window.fill(GRAYB)
        self.messageField.draw()
        self.gotoAButton.draw()
        self.gotoCButton.draw()

    def receive(self, msgType, data):
        print('In B')
        print('Received a message of type:', msgType)
        print('The data received was:', data)

    def respond(self, msgType):
        if msgType == 'get data':
            return 'Here is data from scene B'