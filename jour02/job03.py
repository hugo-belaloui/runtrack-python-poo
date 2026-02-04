class Livre:
    def __init__(self, titre, auteur, nombresDePages, disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombresDePages = 0
        self.set_nombresDePages(nombresDePages)
        self.__disponible = disponible

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nombresDePages(self):
        return self.__nombresDePages
    def set_titre(self, name):
        self.__titre = name
    def set_auteur(self, author):
        self.__auteur = author
    def set_nombresDePages(self, value):
        if isinstance(value, int) and value > 0: 
            self.__nombresDePages = value
        else:
            print("un livre ne peut avoir un nombre negatif de pages")
    
    def vérification(self):
        if self.__disponible:
            return True
        else:
            return False
    def emprunter(self):
        if self.vérification():
            self.__disponible = False
        else:
            print("Livre indisponible")
    def rendre(self):
        if not self.vérification():
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunter")
