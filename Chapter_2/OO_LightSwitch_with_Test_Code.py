# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
         self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)
    
# Main code
oLightSwitch = LightSwitch()  # create a LightSwitch object

#  Calls to methods
oLightSwitch.show() # call the show method of oLightSwitch
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOff() # call the turnOff method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()
