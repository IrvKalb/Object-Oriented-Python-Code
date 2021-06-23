#  Dodger Main program
#
# Instantiates 3 scenes, creates and starts the Scene Manager


# 1 - Import packages
import os
import sys
# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
import pyghelpers
from pygame.locals import *
from Constants import *
from SceneSplash import *
from ScenePlay import *
from SceneHighScores import *

# 2 - Define constants
FRAMES_PER_SECOND = 40

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Instantiate all scenes and store them into a list
scenesList = [SceneSplash(window),
              SceneHighScores(window),
              ScenePlay(window)]

# Create the Scene Manager, passing in the scenes list and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)  #

# Tell the scene manager to start running
oSceneMgr.run()
