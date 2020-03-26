### PLAYER
import pygame
import pygwidgets
from Constants import *

class Player():
    def __init__(self, window):
        self.window = window
        self.image = pygwidgets.Image(window, (0, 0), 'images/player.png')
        self.playerRect = self.image.getRect()
        self.maxX = WINDOW_WIDTH - self.playerRect.width
        self.maxY = GAME_HEIGHT - self.playerRect.height

    # Every frame, move the player icon to the mouse position
    # Limits the position to the game area of the window
    def update(self):
        x, y = pygame.mouse.get_pos()
        if x < 0:
            x = 0
        elif x > self.maxX:
            x = self.maxX
        if y < 0:
            y = 0
        elif y > self.maxY:
            y = self.maxY

        self.image.setLoc((x, y))
        self.playerRect.left = x
        self.playerRect.top = y
        return self.playerRect

    def draw(self):
        self.image.draw()