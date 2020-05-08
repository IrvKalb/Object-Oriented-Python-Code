# Club class 

class Club():

    def __init__(self, clubName, maxStudents):
        self.clubName = clubName
        self.maxStudents = maxStudents
        self.studentsList = []

    def addStudent(self, studentName):
        if len(self.studentsList) < self.maxStudents:
            self.studentsList.append(studentName)
            print('OK.', studentName, 'has been added to the', self.clubName, 'club')
        else:
            print('Sorry, but the', self.clubName, 'club already has', self.maxStudents, 'students') 

    def report(self):
        print()
        print('Here are the', len(self.studentsList), 'members of the', self.clubName, 'club:')
        print()
        for name in self.studentsList:
            print('   ' + name)

