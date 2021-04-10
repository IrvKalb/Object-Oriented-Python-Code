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
# create instances of all scenes.  Specify the window and the key (label) for each scene
oSplashScene = SceneSplash(window, SCENE_SPLASH)
oPlayScene = ScenePlay(window, SCENE_PLAY)
oResultsScene = SceneResults(window, SCENE_RESULTS)

# 5 - Initialize variables

# build a dictionary of all scenes
scenesDict = {SCENE_SPLASH: oSplashScene, SCENE_PLAY:oPlayScene, SCENE_RESULTS:oResultsScene}

# Create the Scene Manager, passing in the scenes dictionary, the starting scene, and FPS
oSceneMgr = pyghelpers.SceneMgr(scenesDict, SCENE_SPLASH, FRAMES_PER_SECOND)

# Tell the scene manager to start running
oSceneMgr.run()
