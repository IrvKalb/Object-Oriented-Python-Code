# Dimmer Switch class

class DimmerSwitch():
    def __init__(self, label):
        self.label = label
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
        print('Label:', self.label)
        print('Light is on?', self.isOn)
        print('Brightness is:', self.brightness)
        print()

    
# Main code

# Create three DimmerSwitch objects 
oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print()
oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()
oDimmer3 = DimmerSwitch('Dimmer3')
print(type(oDimmer3))
print(oDimmer3)
print()

# With oDimmer1, turn it on and raise level twice
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# With oDimmer2, turn on and raise level 3 times

oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Leave oDimmer3 alone, use default settings

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()

# Print variables associated with a Dimmer object
print('oDimmer1 variables:', vars(oDimmer1))
