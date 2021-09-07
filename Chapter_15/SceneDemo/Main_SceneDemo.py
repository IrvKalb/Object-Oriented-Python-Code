# Scene Demo main program with three scenes

# This is a demo of a typical main program using the Scene Manager.
# It should start by defining the size of your window, initializing pygame and creating the window.
# Next, you  create an instance of each of your scenes.
# Then build a list of all the scenes, which would look like:
#    [<scene1Instance>, <scene2Instance>, ... <sceneNInstance>]
# The first scene in the list will be used as the starting scene.
# The ordering of the other scenes does not matter.
# Using that scenesList, and a frames per second, you instantiate the SceneMgr object
# Finally, you tell the SceneMgr object to run.
# The SceneMgr takes over, runs the main loop, and handles navigation and communication between scenes.

# 1 - Import packages
import pygame
import pyghelpers
from SceneA import *
from SceneB import *
from SceneC import *

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 180
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
# Instantiate all scenes and store them into a list
scenesList = [SceneA(window),
              SceneB(window),
              SceneC(window)]

# Create the Scene Manager, passing in the scenes list, and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Tell the Scene Manager to start running
oSceneMgr.run()
