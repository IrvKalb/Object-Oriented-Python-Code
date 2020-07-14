# Timers
# Includes:
#    CountUpTimer
#    CountDownTimer

import time

#
# CountUpTimer class
#
class CountUpTimer():
    NSECONDS_PER_HOUR = 60 * 60
    NSECONDS_PER_MINUTE = 60
    def __init__(self):
        self.running = False
        self.savedSecondsElapsed = 0
        
    def start(self):
        self.secondsStart = time.time()  # get the current seconds, and save it away
        self.running = True
        self.savedSecondsElapsed = 0

    def getTime(self):
        if self.running:
            secondsNow = time.time()
            secondsElapsed = secondsNow - self.secondsStart
        else:
            secondsElapsed = self.savedSecondsElapsed
        return secondsElapsed  # returns a float

    def getTimeInSeconds(self):
        nSeconds = self.getTime()
        nSeconds = int(nSeconds)
        return nSeconds

    def getTimeInHHMMSS(self):
        nSeconds = self.getTime()
        nSeconds = int(nSeconds)
        output = ''
        if nSeconds > CountDownTimer.NSECONDS_PER_HOUR:
            nHours = nSeconds // CountDownTimer.NSECONDS_PER_HOUR
            nSeconds = nSeconds - (nHours * CountDownTimer.NSECONDS_PER_HOUR)
            output = str(nSeconds) + ":"
        if nSeconds > CountDownTimer.NSECONDS_PER_MINUTE:
            nMinutes = nSeconds // CountDownTimer.NSECONDS_PER_MINUTE
            nSeconds = nSeconds - (nMinutes * CountDownTimer.NSECONDS_PER_MINUTE)
            if (output != '') and (nMinutes < 10):
                output = output + '0' + str(nMinutes) + ":"
            else:
                output = output + str(nMinutes) + ":"
        if (output != '') and (nSeconds < 10):
            output = output + '0' + str(nSeconds)
        else:
            output = output + str(nSeconds)
        return output


    def stop(self):
        self.running = False
        secondsNow = time.time()
        self.savedSecondsElapsed = secondsNow - self.secondsStart

#
# CountDownTimer class
#
class CountDownTimer():
    NSECONDS_PER_HOUR = 60 * 60
    NSECONDS_PER_MINUTE = 60
    def __init__(self, nStartingSeconds, stopAtZero=True):
        self.running = False
        self.secondsSavedRemaining = 0
        self.nStartingSeconds = nStartingSeconds
        self.stopAtZero = stopAtZero
        
    def start(self):
        secondsNow = time.time()  
        self.secondsEnd = secondsNow + self.nStartingSeconds
        self.reachedZero = False
        self.running = True

    def getTime(self):
        if self.running:
            secondsNow = time.time()
            secondsRemaining = self.secondsEnd - secondsNow
            if self.stopAtZero and (secondsRemaining <= 0):
                secondsRemaining = 0
                self.running = False
                self.reachedZero = True
        else:
            secondsRemaining = self.secondsSavedRemaining
        return secondsRemaining  # returns a float

    def getTimeInSeconds(self):
        nSeconds = self.getTime()
        nSeconds = int(nSeconds)
        return nSeconds

    def getTimeInHHMMSS(self):
        nSeconds = self.getTime()
        nSeconds = int(nSeconds)
        output = ''
        if nSeconds > CountDownTimer.NSECONDS_PER_HOUR:
            nHours = nSeconds // CountDownTimer.NSECONDS_PER_HOUR
            nSeconds = nSeconds - (nHours * CountDownTimer.NSECONDS_PER_HOUR)
            output = str(nSeconds) + ":"
        if nSeconds > CountDownTimer.NSECONDS_PER_MINUTE:
            nMinutes = nSeconds // CountDownTimer.NSECONDS_PER_MINUTE
            nSeconds = nSeconds - (nMinutes * CountDownTimer.NSECONDS_PER_MINUTE)
            if (output != '') and (nMinutes < 10):
                output = output + '0' + str(nMinutes) + ":"
            else:
                output = output + str(nMinutes) + ":"
        if (output != '') and (nSeconds < 10):
            output = output + '0' + str(nSeconds)
        else:
            output = output + str(nSeconds)
        return output

    
    def stop(self):
        self.running = False
        secondsNow = time.time()
        self.secondsSavedRemaining = self.secondsEnd - secondsNow

    def ended(self):
        return self.reachedZero
