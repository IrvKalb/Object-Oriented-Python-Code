# SimpleAnimation object

import pygame
import time

class SimpleAnimation():
    def __init__(self, window, loc, picPathsList, durationPerImage):
        """
        A simple animation only requires a:
        window - to draw into
        loc - location in the window to draw the images
        picPathsList - a list of paths to images
        durationPerImage - how long (milliseconds) to show each image

        Save values in instance variables
        Loop through the list of paths, and load all images into another list

        self.index is the index of the current image to show
        """

        self.window = window
        self.loc = loc
        self.imagesList = []
        for picPath in picPathsList:
            image = pygame.image.load(picPath)  # normal case, load an image
            image = pygame.Surface.convert_alpha(image)  # optimizes blitting
            self.imagesList.append(image)

        self.playing = False
        self.durationPerImage = durationPerImage
        self.nImages = len(self.imagesList)
        self.index = 0

    def play(self):
        if self.playing:
            return
        self.playing = True
        self.imageStartTime = time.time()
        self.index = 0

    def update(self):
        if not self.playing:
            return

        # How much time has elapsed since we started showing this image
        self.elapsed = (time.time() - self.imageStartTime)

        # If enough time has elapsed, move onto the next image
        if self.elapsed > self.durationPerImage:
            self.index = self.index + 1

            if self.index < self.nImages: # move on to next image
                self.imageStartTime = time.time()
            else:  # animation is finished
                self.playing = False
                self.index = 0  # reset to the beginning

    def draw(self):
        # Assumes that self.index has been set earlier - in update method
        # it is used as the index into the imagesList to find the current image
        theImage = self.imagesList[self.index]  # choose the image to show

        self.window.blit(theImage, self.loc)   #show it
            
