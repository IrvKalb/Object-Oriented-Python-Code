# High Scores Data class
from Constants import *
from pathlib import Path
import json

class HighScoresData():
    """The data file is stored as a list of lists in json format.
    Each list is made up of a name and a score:
        [[name, score], [name, score], [name, score] ...]
    The list is kept in order of scores, highest to lowest."""
    DATA_FILE_PATH = 'HighScores.json'

    def __init__(self):
        self.BLANK_SCORES_LIST = N_HIGH_SCORES * [['-----', 0]]
        self.oFilePath = Path(HighScoresData.DATA_FILE_PATH)

    def getScores(self):

        if self.oFilePath.is_file():
            data = self.oFilePath.read_text()
            scoresList = json.loads(data)
        else:  # file doesn't exist, set scores to blank, write out file
            scoresList = self.BLANK_SCORES_LIST.copy()
            self.saveScores(scoresList)
        return scoresList

    def saveScores(self, scoresList):
        scoresAsJson = json.dumps(scoresList)
        self.oFilePath.write_text(scoresAsJson)

    def resetScores(self):
        scoresList = self.BLANK_SCORES_LIST.copy()
        self.saveScores(scoresList)
        return scoresList
