class Student:
    def __init__(self, nom, prénom, numéro_étudiants):
        self.__nom = nom
        self.__prénom = prénom
        self.__numéro_étudiants = numéro_étudiants
        self.__crédits = 0
        self.__level = self.__studentEval()
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prénom
    def get_credits(self):
        return self.__crédits
    def add_credits(self, value):
        if self.get_credits() >= 0:
            self.__crédits += value
            self.__level = self.__studentEval()
        else:
            print("Valeur doit etre supérieur a zero")
    def __studentEval(self):
        if self.get_credits() >= 90:
            return "Excellent"
        elif self.get_credits() >= 80:
            return "Tres bien"
        elif self.get_credits() >= 70:
            return "Bien"
        elif self.get_credits() >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prénom}")
        print(f"id = {self.__numéro_étudiants}")
        print(f"Niveau = {self.__level}")


student = Student("John", "Doe", "145")
student.add_credits(5)
student.add_credits(15)
student.add_credits(10)

print(f"le nombre de credits de {student.get_nom()} {student.get_prenom()} est de {student.get_credits()} points")

student.studentInfo()

student.add_credits(5)
student.add_credits(15)
student.add_credits(50)

student.studentInfo()