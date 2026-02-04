class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)
    def afficher(self):
        list_product = [
            (
                f"Nom produit : {self.nom}, "
                f"Prix HT : {self.prixHT}, "
                f"Prix TTC : {self.CalculerPrixTTC()}"
            )
        ]
        return list_product
    def change_name(self, new_name):
        self.nom = new_name
    def change_price(self, new_price):
        self.prixHT = new_price
    def get_name(self):
        return self.nom

    def get_prix_ht(self):
        return self.prixHT

    def get_tva(self):
        return self.TVA

product_one = Produit("TV", 699, 0.2)
product_two = Produit("Telephone", 400, 0.2)
product_three = Produit("Pomme-de-terre", 0.9, 0.2)


print(product_one.afficher())
print(product_two.afficher())
print(product_three.afficher())

product_one.change_name("Xbox")
product_one.change_price(499)

product_two.change_name("Iphone")
product_two.change_price(1200)

print(product_one.afficher())
print(product_two.afficher())
