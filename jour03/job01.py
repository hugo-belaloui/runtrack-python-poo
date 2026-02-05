class Ville:
    def __init__(self, name_city, amount_inhabitants):
        self.__name_city = name_city
        self.__amount_inhabitants = amount_inhabitants
    def get_name_city(self):
        return self.__name_city
    def get_amount_inhabitants(self):
        return self.__amount_inhabitants
    def set_name_city(self, value):
        self.__name_city = value
    def set_amount_inhabitants(self, value):
        self.__amount_inhabitants += value

class Personne:
    def __init__(self, name, age, residency):
        self.__name = name
        self.__age = age
        self.__residency = residency
        self.ajouterPopulation()
    def ajouterPopulation(self):
        self.__residency.set_amount_inhabitants(1)
    def get_name(self):
            return self.__name
    def get_age(self):
            return self.__age
    def get_residency(self):
        return self.__residency.get_name_city()



ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

print(f"Population de la ville de {ville1.get_name_city()} : {ville1.get_amount_inhabitants()}")
print(f"Population de la ville de {ville2.get_name_city()} : {ville2.get_amount_inhabitants()}")

john = Personne("John", 45, ville1)
myrt = Personne("Myrtille", 4, ville1)
Chl = Personne("Chloé", 18, ville2)

print(f"Mise a jour de la population de la ville de {ville1.get_name_city()} : {ville1.get_amount_inhabitants()}")
print(f"Mise a jour de la population de la ville de  {ville2.get_name_city()} : {ville2.get_amount_inhabitants()}")

print(f"{john.get_name()} {john.get_age()} {john.get_residency()}")

