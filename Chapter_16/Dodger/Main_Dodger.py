#  Dodger main program
#
# Instantiates 3 scenes, creates and starts the scene manager
#
#  Original version by Al Sweigart from his book "Invent With Python"
#    (concept, graphics, and sounds used by permission from Al Sweigart)

# 1 - Import packages
import os
# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
import pyghelpers
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
# Instantiate all scenes and store them in a list
scenesList = [SceneSplash(window),
                    SceneHighScores(window),
                    ScenePlay(window)]

# Create the scene manager, passing in the scenes list and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Tell the Scene Manager to start running
oSceneMgr.run()
