# Club class 

class Club():

    def __init__(self, clubName, maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers
        self.membersList = []

    def addMember(self, name):
        # Make sure that there is enough room left
        if len(self.membersList) < self.maxMembers:
            self.membersList.append(name)
            print('OK.', name, 'has been added to the', self.clubName, 'club')
        else:
            print('Sorry, but we cannot add', name, 'to the', self.clubName, 'club.')
            print('This club already has the maximum of', self.maxMembers, 'members.') 

    def report(self):
        print()
        print('Here are the', len(self.membersList), 'members of the', self.clubName, 'club:')
        for name in self.membersList:
            print('   ' + name)
        print()

