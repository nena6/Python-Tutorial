from cricket import CricketFan
from party import PartyAnimal

s = PartyAnimal('Sally')
s.party()
print(dir(s))
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))