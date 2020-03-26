## Scenes Demo Main

# This is a demo of a typical main program using the Scene Manager.
# It should start by defining the size of your window, initializing pygame and creating the window.
# Next, you  create an instance of each of your scenes.  Using those, and a "scene key"
#    a unique string (saved in the Constants.py file), you build up a scenesDict dictionary.
#    The scenesDict should look like:
#    {<scene1Key>:<scene1Instance>, <scene2Key>:<scene2Instance>, ... }
# Using that scenesDict, and a starting scene key, and a frames per second, you instantiate the SceneMgr object
# Finally, you tell the SceneMgr object to run.
# The SceneMgr takes over, runs the main loop, and handles navigation and communication between scenes.

# 1 - Import packages
import pygame
import pyghelpers
from Constants import *
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

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Create instances of all scenes.  Pass in the window and a scene key (string) for each scene
oSceneA = SceneA(window, SCENE_A)
oSceneB = SceneB(window, SCENE_B)
oSceneC = SceneC(window, SCENE_C)

# Build a dictionary of all scenes
scenesDict = {SCENE_A : oSceneA, SCENE_B : oSceneB, SCENE_C : oSceneC}

# Create the Scene Manager, passing in the scenes dictionary, the starting scene, and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesDict, SCENE_A, FRAMES_PER_SECOND)

# Tell the Scene Manager to start running
oSceneMgr.run()
