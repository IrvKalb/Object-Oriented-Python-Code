#
# This is a Blank Scene
#
# This is a template for what a Scene should look like
#

import pygwidgets
import pygame
from SceneMgr import Scene


class MyScene(Scene):  # Inherits from the Scene class in the SceneMgr file
    def __init__(self, window, sceneKey):
        '''
        This method is called when the scene is created
        Create and/or load any assets (images, buttons, sounds)
        that you need for this scene
        :param window:
        :param sceneKey:
        '''
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey

        # As a sample, let's create a button
        self.navButton = pygwidgets.TextButton((self.window, (300, 230), 'Navigate'))


    def enter(self, data):
        '''
        This method is called whenever the scene changes to this scene.
        'data' is a any information that is passed from the previous scene
        Typical use is to pass in a dictionary, from which useful data can be extracted.

        :param data:
        :return:
        '''
        pass

    def handleInputs(self, events, keyPressedList):
        '''
        This method is called on every frame when an event happens
        It is passed in a list of events and a list of keyboard keys that are down
        Typical code is to loop through the events and handle any that you want to
        :param self:
        :param events:
        :param keyPressedList:
        :return:
        '''
        for event in events:
            if self.navButton.handleEvent(event):
                print('Clicked on the nav button - typically add a: self.goToScene("NewScene")')

    def update(self):
        '''
        This method is called once per frame while the scene is active
        Include in here, any code you want to execute every frame
        :param self:
        :return:
        '''
        pass

    def draw(self):
        '''
        This method is called on every frame
        Include any code that you need to draw everything in the window
        (Typical is to do a window fill or blit a background picture,
        and draw buttons, fields, characters, etc.)
        :param self:
        :return:
        '''
        self.navButton.draw()

    def leave(self):
        '''
        This method is called once when your code has asked to move on to a new scene
        It should return any data that this scene wants to pass on to the next scene
        The typical data is either None or a dictionary.
        :param self:
        :return:
        '''
        return None
