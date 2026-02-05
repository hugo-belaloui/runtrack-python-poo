class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__liste_plats = {}  
        self.__statut_commande = "en cours"
    def ajouter_plat(self, nom_plat, prix_plat):
        self.__liste_plats[nom_plat] = {"prix": prix_plat, "statut": "commandé"}
        print(f"Plat ajouté : {nom_plat}")
    def annuler_commande(self):
        self.__statut_commande = "annulée"
        print("la commande a été annulée")
    def __calculer_total(self):
        total = 0
        for plat in self.__liste_plats.values():
            total += plat["prix"]
        return total
    def calculer_tva(self, taux=0.20):
        total = self.__calculer_total()
        return total * taux
    def afficher_commande(self):
        print(f"commande N°{self.__numero_commande}")
        print(f"Statut : {self.__statut_commande}")
        for nom, details in self.__liste_plats.items():
            print(f"{nom} : {details['prix']} € ({details['statut']})")
        total = self.__calculer_total()
        tva = self.calculer_tva()
        print(f"Total HT  : {total} €")
        print(f"TVA (20%) : {tva} €")
        print(f"Total TTC : {total + tva} €")