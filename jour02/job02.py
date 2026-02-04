class Livre:
    def __init__(self, titre, auteur, nombresDePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombresDePages = 0
        self.set_nombresDePages(nombresDePages)

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def gte_nombresDePages(self):
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


#pythonic way for validation logic
    # @property 
    # def nombresDePages(self):
    #     return self.__nombresDePages
    # @nombresDePages.setter
    # def nombresDePages(self, value):
    #     if value <= 0: 
    #         print("un livre ne peut avoir un nombre negatif de pages")          
    #     else:
    #         self.__nombresDePages = value