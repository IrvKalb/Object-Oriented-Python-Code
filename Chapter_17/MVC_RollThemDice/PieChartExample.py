from math import pi, cos, sin
import pygame
import pygame.gfxdraw
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
RADIUS = 200

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
PURPLE = (230, 230, 250)


WHITE = (255, 255, 255)
N_TRIALS = 10000


pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#rect = pygame.Rect((200, 200), (400, 400))

def degreesToRadians(nDegrees):
    nRadians = (pi /180) * nDegrees
    return nRadians

def drawFilledArc(centerX, centerY, radius, degrees0, degrees1, color):
    theta0 = degreesToRadians(degrees0)
    theta1 = degreesToRadians(degrees1)
    print('in drawFilledArc', theta0, theta1)
    
    pygame.gfxdraw.pie(window, centerX, centerY, radius, degrees0, degrees1, color)
    ndiv = 100
    d_theta = (theta1 - theta0) / ndiv
    centerTuple = (centerX, centerY)

    for i in range(ndiv):
        x = centerY + radius * cos(theta0 + i*d_theta)
        y = centerY + radius * sin(theta0 + i*d_theta)
        pygame.draw.line(window, color, centerTuple, (x, y), 8)

colorDict = {'red': RED, 'green': GREEN, 'blue': BLUE,
                'orange': ORANGE, 'light blue':LIGHT_BLUE, 'purple': PURPLE}
colorChoices = []
for color in colorDict.keys():
    colorChoices.append(color)

print(colorChoices)

selectionDict = {}
for i in range(N_TRIALS):
    color = random.choice(colorChoices)
    if color not in selectionDict:
        selectionDict[color] = 1
    else:
        selectionDict[color] = selectionDict[color] + 1

print(selectionDict)



#drawFilledArc(CENTER_X, CENTER_Y, RADIUS, 0, 72, RED)
#drawFilledArc(CENTER_X, CENTER_Y, RADIUS, 72, 144, GREEN)

startAngle = 0
for key, value in selectionDict.items():
    percent  = value / N_TRIALS
    endAngle = startAngle + int(percent * 360)
    rgbColor = colorDict[key]

    print(startAngle, endAngle, key)
    
    drawFilledArc(CENTER_X, CENTER_Y, RADIUS, startAngle, endAngle, rgbColor)
    startAngle = endAngle
    
    


pygame.display.flip()
