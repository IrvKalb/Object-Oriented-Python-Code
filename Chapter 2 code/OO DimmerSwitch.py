# Dimmer Switch class

class DimmerSwitch():
    def __init__(self):
        self.isOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print('Switch is on?', self.isOn)
        print('Brightness is:', self.brightness)

    
# Main code

oDimmer = DimmerSwitch()
print(type(oDimmer))




