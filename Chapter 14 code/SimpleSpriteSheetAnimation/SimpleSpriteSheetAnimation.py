# SimpleSpriteSheetAnimation class

import pygame
import time

class SimpleSpriteSheetAnimation():
    def __init__(self, window, loc, imagePath, nCols, nImages, width, height, durationPerImage):
        self.window = window
        self.loc = loc
        self.nImages = nImages
        self.imagesList = []

        # Load the sprite sheet and break it up into sub surfaces.
        spriteSheetImage = pygame.image.load(imagePath)
        spriteSheetImage = pygame.Surface.convert_alpha(spriteSheetImage)  # optimizes blitting

        row = 0
        col = 0
        for imageNumber in range(nImages):
            x = col * height
            y = row * width

            # Create a subsurface from the bigger spriteSheet
            image = spriteSheetImage.subsurface(x, y, width, height)
            self.imagesList.append(image)

            col = col + 1
            if col == nCols:
                col = 0
                row = row + 1

        self.durationPerImage = durationPerImage
        self.playing = False
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
        self.elapsed = time.time() - self.imageStartTime

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
        # it is used as the index into the imagesList to find the the current image
        theImage = self.imagesList[self.index]  # choose the image to show

        self.window.blit(theImage, self.loc)   #show it
