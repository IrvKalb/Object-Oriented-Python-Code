# Dimmer Switch class

class DimmerSwitch():
    def __init__(self):
        self.isOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.isOn = True
        # turn the light on at self.brightness

    def turnOff(self):
        self.isOn = False
        # turn the light off

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print('Light is on?', self.isOn)
        print('Brightness is:', self.brightness)

    

# Main code

# Create first Dimmer Switch, turn on and raise level twice
oDimmer1 = DimmerSwitch()
print(type(oDimmer1))
print(oDimmer1)
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Create second Dimmer Switch, turn on and raise level 3 times
oDimmer2 = DimmerSwitch()
print(type(oDimmer2))
print(oDimmer2)
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Create third Dimmer Switch, leave alone, use default settings
oDimmer3 = DimmerSwitch()
print(type(oDimmer3))
print(oDimmer3)

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()





