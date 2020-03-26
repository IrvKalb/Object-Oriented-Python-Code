# LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the light on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the light off
         self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)
    
# Main code
oSwitch1 = LightSwitch()  # create a switch object
oSwitch2 = LightSwitch()  # create another switch object

#  Test code:
oSwitch1.show()
oSwitch2.show()
oSwitch1.turnOn()
oSwitch2.turnOff()  # Should be off at start, but this makes it clearer
oSwitch1.show()
oSwitch2.show()

