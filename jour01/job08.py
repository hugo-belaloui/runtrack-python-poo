import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, newRadius):
        self.rayon = newRadius
    def circonference(self):
        return 2 * math.pi * self.rayon
    def aire(self):
        return math.pi * (self.rayon ** 2)
    def diametre(self):
        return 2 * self.rayon
    def afficherInfos(self):
        print(f"Rayon : {self.rayon}, Circonférence : {self.circonference():.2f}, Aire : {self.aire():.2f}, Diametre : {self.diametre()}")

circle_one = Cercle(4)
circle_two = Cercle(7)

circle_one.afficherInfos()
circle_two.afficherInfos()
