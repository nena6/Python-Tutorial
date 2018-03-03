from party import PartyAnimal


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points += 6
        self.party()
        print(self.name, ' points ', self.points)
