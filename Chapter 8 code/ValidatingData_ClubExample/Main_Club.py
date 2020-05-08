# Club Example main program

from Club import *

# Create a club with at most 5 students
oProgrammingClub = Club('Programming', 5)

oProgrammingClub.addStudent('Joe Schmoe')
oProgrammingClub.addStudent('Cindy Lou Hoo')
oProgrammingClub.addStudent('Dino Richmond')
oProgrammingClub.addStudent('Susie Sweetness')
oProgrammingClub.addStudent('Fred Farkle')

oProgrammingClub.report()

# Attempt to add additional student

oProgrammingClub.addStudent('Iwanna Join')

