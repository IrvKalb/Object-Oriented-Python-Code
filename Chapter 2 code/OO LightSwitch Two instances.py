# LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
         self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)
    
# Main code
oLightSwitch1 = LightSwitch()  # create a LightSwitch object
oLightSwitch2 = LightSwitch()  # create another LightSwitch object

#  Test code:
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()
oLightSwitch2.turnOff()  # Should be off at start, but this makes it clearer
oLightSwitch1.show()
oLightSwitch2.show()

