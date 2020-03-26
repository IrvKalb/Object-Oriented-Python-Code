# DimmerSwitch Procedural Code

def turnOn():    
    on = True
    # turn  on the light at the given setting
    return on

def turnOff():
    on = False
    #turn off the light
    return on

def raiseLevel(currentSetting):
    newSetting = currentSetting
    if newSetting <= 10:
        newSetting = newSetting + 1
    return newSetting

def lowerLevel(currentSetting):
    newSetting = currentSetting
    if newSetting > 0:
        newSetting = newSetting - 1
    return newSetting

    
# Main code

brightness = 0   # a global integer variable
switchIsOn = False  # global boolean

##  Test code:
switchIsOn = turnOn()
brightness = raiseLevel(brightness)
brightness = raiseLevel(brightness)
brightness = raiseLevel(brightness)
brightness = raiseLevel(brightness)
brightness = raiseLevel(brightness)
print  'Light is on? ', switchIsOn, '  Brightness is: ', brightness
brightness = lowerLevel(brightness)
switchIsOn = turnOff()
print  'Light is on? ', switchIsOn, '  Brightness is: ', brightness
switchIsOn = turnOn()
brightness = raiseLevel(brightness)
brightness = raiseLevel(brightness)
brightness = raiseLevel(brightness)
print  'Light is on? ', switchIsOn, '  Brightness is: ', brightness
