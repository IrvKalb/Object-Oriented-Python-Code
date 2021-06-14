# Demo of Scenes with Scene manager
# Rock, Paper, Scissors

# 1 - Import packages

import pygame
import pyghelpers
import sys
from Constants import *
from SceneSplash import *
from ScenePlay import *
from SceneResults import *


# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Instantiate all scenes and store them into a list
scenesList = [SceneSplash(window),
              ScenePlay(window),
              SceneResults(window)]

# Create the Scene Manager, passing in the scenes list, and FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Tell the scene manager to start running
oSceneMgr.run()
