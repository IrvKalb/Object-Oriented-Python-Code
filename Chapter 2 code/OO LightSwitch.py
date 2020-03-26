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
oSwitch = LightSwitch()  # create a switch object

#  Test code:
oSwitch.show()
oSwitch.turnOn()
oSwitch.show()
oSwitch.turnOff()
oSwitch.show()
oSwitch.turnOn()
oSwitch.show()
