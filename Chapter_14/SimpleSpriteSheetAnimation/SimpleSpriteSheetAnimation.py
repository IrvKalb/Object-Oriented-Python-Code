# SimpleSpriteSheetAnimation class

import pygame
import time

class SimpleSpriteSheetAnimation():
    def __init__(self, window, loc, imagePath, nImages, width, height, durationPerImage):
        self.window = window
        self.loc = loc
        self.nImages = nImages
        self.imagesList = []

        # Load the sprite sheet
        spriteSheetImage = pygame.image.load(imagePath)
        # Optimizes blitting
        spriteSheetImage = pygame.Surface.convert_alpha(spriteSheetImage)

        # Calculate the number of columns in the starting image
        nCols = spriteSheetImage.get_width() // width

        # Break the starting image into subimages
        row = 0
        col = 0
        for imageNumber in range(nImages):
            x = col * height
            y = row * width

            # Create a subsurface from the bigger spriteSheet
            subsurfaceRect = pygame.Rect(x, y, width, height)
            image = spriteSheetImage.subsurface(subsurfaceRect)
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
        # Assumes that self.index has been set earlier - in the update() method.
        # It is used as the index into the imagesList to find the current image.
        theImage = self.imagesList[self.index]  # choose the image to show

        self.window.blit(theImage, self.loc)   #show it
