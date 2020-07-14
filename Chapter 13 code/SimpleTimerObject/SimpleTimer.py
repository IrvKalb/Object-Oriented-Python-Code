# Timer class – Simple
class Timer():
    udef __init__(self, timeInSeconds, nickname=None, callBack=None):
        self.timeInSeconds = timeInSeconds
        self.nickname = nickname
        self.callBack = callBack
        self.running = False

    vdef start(self):
        self.running = True
        self.startTime = time.time()

    wdef update(self):
        if not self.running:
            return False
        timeElapsed = time.time() - self.startTime
        if timeElapsed < self.timeInSeconds:
            return False  # running but not reached limit

        else:  # Timer has finished
            self.running = False
            if self.callBack is not None:
                self.callBack(self.nickname)

            return True  # True here means that the timer has ended
