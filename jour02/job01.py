class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    """ following code works but isn't the pythonic way """ 
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur
    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur
    """ pythonic way using decorator if a validation logic was required """
    # @property
    # def longueur(self):
    #     return self.__longueur
    # @longueur.setter
    # def longueur(self, value):
    #     self.__longueur = value
    # @property 
    # def largeur(self):
    #     return self.__largeur
    # @largeur.setter
    # def largeur(self, value):
    #     self.__largeur = value

rect = Rectangle(10, 5)
print(rect.get_longueur(), rect.get_largeur())
rect.set_largeur(12)
rect.set_longueur(17)
print(rect.get_longueur(), rect.get_largeur())