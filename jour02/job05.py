class Voiture:
    def __init__(self, marque, modele, année, kilométrage, en_marche = False, reservoir = 50):
        self.__marque = marque
        self.__modele = modele
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_année(self):
        return self.__année
    def get_kilométrage(self):
        return self.__kilométrage
    def get_en_marche(self):
        return self.__en_marche
    def set_marque(self, x_marque):
        self.__marque = x_marque 
    def set_modele(self, x_modele):
        self.__modele = x_modele
    def set_année(self, x_année):
        self.__année = x_année
    def set_kilométrage(self, x_kilométrage):
        self.__kilométrage = x_kilométrage 
    def set_en_marche(self, x_en_marche):
        self.__en_marche = x_en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.set_en_marche(True)
    def arreter(self):
        self.set_en_marche(False)
    def __verifier_plein(self):
        return self.__reservoir
    
