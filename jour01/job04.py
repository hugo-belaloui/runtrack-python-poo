class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Create a person

person1 = Personne("John", "Doe")
person2 = Personne("Jean", "Dupond")

print(person1.SePresenter())
print(person2.SePresenter())