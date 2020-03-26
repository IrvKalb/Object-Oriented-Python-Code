# PrivatePerson class

class PrivatePerson():

    def __init__(self, name, data):
        self.name = name
        self.__privateData = data

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

