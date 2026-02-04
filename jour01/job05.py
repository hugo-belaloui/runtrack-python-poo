class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        print(f"Coordonnées sont x : {self.x} y : {self.y}")
    def afficherX(self):
        print(self.x)
    def afficherY(self):
        print(self.y)
    def changerX(self, newX):
        self.x = newX
    def changerY(self, newY):
        self.y = newY

