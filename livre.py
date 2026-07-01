class Livre:
    def __init__(self, code, titre, auteur, categorie, exemplaires):
        self.code = code
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.exemplaires = exemplaires

    def est_disponible(self):
        return self.exemplaires > 0

    def afficher_infos(self):
        return (
            f"{self.code} | {self.titre} | {self.auteur} | "
            f"{self.categorie} | Exemplaires : {self.exemplaires}"
        )