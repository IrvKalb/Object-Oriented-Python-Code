# Rock Paper Scissors in PyGame
# Demonstration of a state machine

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import random
import sys

# 2 Define constants
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

# Set constants for each of the three states
STATE_SPLASH = 'Splash'
STATE_PLAYER_CHOICE = 'PlayerChoice'
STATE_SHOW_RESULTS = 'ShowResults'

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sounds,  etc.
startButton = pygwidgets.CustomButton(window, (210, 300), \
                                           up='images/startButtonUp.png', \
                                           down='images/startButtonDown.png', \
                                           over='images/startButtonHighlight.png')

rockButton = pygwidgets.CustomButton(window, (25, 120), \
                                 up = "images/Rock.png", \
                                 over = "images/RockOver.png", \
                                 down = "images/RockDown.png")

paperButton =  pygwidgets.CustomButton(window, (225, 120), \
                                 up = "images/Paper.png", \
                                 over = "images/PaperOver.png", \
                                 down = "images/PaperDown.png")

scissorButton =  pygwidgets.CustomButton(window, (425, 120), \
                                 up = "images/Scissors.png", \
                                 over = "images/ScissorsOver.png", \
                                 down = "images/ScissorsDown.png") 

rockImage = pygame.image.load("images/Rock.png")
paperImage = pygame.image.load("images/Paper.png")
scissorImage = pygame.image.load("images/Scissors.png")

restartButton = pygwidgets.CustomButton(window, (220, 310), \
                                    up='images/restartButtonUp.png', \
                                    down='images/restartButtonDown.png', \
                                    over='images/restartButtonHighlight.png')

# Text settings
messageField = pygwidgets.DisplayText(window, (15, 25),  'Welcome to Rock, Paper, Scissors!', \
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

chooseText = pygwidgets.DisplayText(window, (15, 395), 'Choose!', \
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

resultsField = pygwidgets.DisplayText(window, (20, 275), '', \
                                    fontSize=50, textColor=WHITE, width=610, justified='center')
playerScoreCounter = pygwidgets.DisplayText(window, (15, 315), 'Player Score:', \
                                    fontSize=50, textColor = WHITE)

computerScoreCounter = pygwidgets.DisplayText(window, (300, 315), 'Computer Score:', \
                                    fontSize=50, textColor = WHITE)

# Sounds
winnerSound = pygame.mixer.Sound("sounds/ding.wav")
tieSound = pygame.mixer.Sound("sounds/push.wav")
loserSound = pygame.mixer.Sound("sounds/buzz.wav")


# 5 - Initialize variables
playerScore = 0
computerScore = 0
state = STATE_SPLASH    # The current state that the game is in

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()        
        
        if state == STATE_SPLASH:
            if  startButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE

        elif state == STATE_PLAYER_CHOICE:  # let the user choose
            playerChoice = ''  # Indicates no choice yet
            if  rockButton.handleEvent(event):
                playerChoice = ROCK
                playerImage = rockImage
                
            if  paperButton.handleEvent(event):
                playerChoice = PAPER
                playerImage = paperImage
                
            if  scissorButton.handleEvent(event):
                playerChoice = SCISSORS
                playerImage = scissorImage

            if playerChoice != '':    # player has made a choice, make computer choice

                # Computer chooses from tuple of moves
                RPS = (ROCK, PAPER,SCISSORS)
                computerChoice = random.choice(RPS) # Computer chooses

                # Evaluate the Game
                if computerChoice == ROCK:
                    computerImage = rockImage
                elif computerChoice == PAPER:
                    computerImage = paperImage
                else:
                    computerImage = scissorImage

                # Win/Lose/Tie Conditions
                if playerChoice == computerChoice:
                    resultsField.setValue("It's a tie!")
                    tieSound.play()
                    
                elif playerChoice == ROCK and computerChoice == SCISSORS:
                    resultsField.setValue("Rock breaks Scissors.You win!")
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == ROCK and computerChoice == PAPER:
                    resultsField.setValue("Rock is covered by Paper. You lose.")
                    computerScore = computerScore + 1
                    loserSound.play()
                   
                elif playerChoice == SCISSORS and computerChoice == PAPER:
                    resultsField.setValue("Scissors cuts Paper.  You win!")
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == SCISSORS and computerChoice == ROCK:
                    resultsField.setValue("Scissors crushed by Rock. You lose.")
                    computerScore = computerScore + 1
                    loserSound.play()

                elif playerChoice == PAPER and computerChoice == ROCK:
                    resultsField.setValue("Paper covers Rock.  You win!")
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == PAPER and computerChoice == SCISSORS:
                    resultsField.setValue("Paper is cut by Scissors.  You lose.")
                    computerScore = computerScore + 1
                    loserSound.play()

                # Shows the player's score
                playerScoreCounter.setValue("Your Score: "+ str(playerScore))
                # Shows the computer's score
                computerScoreCounter.setValue("Computer Score: "+ str(computerScore))

                state = STATE_SHOW_RESULTS

        elif state == STATE_SHOW_RESULTS:
            if  restartButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE

    # 8  Do any "per frame" actions
    if state == STATE_PLAYER_CHOICE:
        messageField.setValue('       Rock             Paper         Scissors')
    elif state == STATE_SHOW_RESULTS:
        messageField.setValue('You                     Computer')

    # 9 - Clear the screen
    window.fill(GRAY)

    # 10 - Draw all screen elements
    messageField.draw()

    if state == STATE_SPLASH:
        window.blit(rockImage, (25, 120))
        window.blit(paperImage, (225, 120))
        window.blit(scissorImage, (425, 120))
        startButton.draw()

    # Draw player choices on window
    elif state == STATE_PLAYER_CHOICE:
        rockButton.draw()
        paperButton.draw()
        scissorButton.draw()
        chooseText.draw()       

    # Draw the results on to the window
    elif state == STATE_SHOW_RESULTS:
        resultsField.draw()
        window.blit(playerImage, (50, 62))
        window.blit(computerImage, (350, 62))
        playerScoreCounter.draw()
        computerScoreCounter.draw()
        restartButton.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
