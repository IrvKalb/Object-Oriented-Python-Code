# Club example main program

from Club import *

# Create a club with at most 5 members
oProgrammingClub = Club('Programming', 5)

oProgrammingClub.addMember('Joe Schmoe')
oProgrammingClub.addMember('Cindy Lou Hoo')
oProgrammingClub.addMember('Dino Richmond')
oProgrammingClub.addMember('Susie Sweetness')
oProgrammingClub.addMember('Fred Farkle')

oProgrammingClub.report()

# Attempt to add additional member

oProgrammingClub.addMember('Iwanna Join')
