from datetime import date


class Emprunt:
    def __init__(self, lecteur, livre):
        self.lecteur = lecteur
        self.livre = livre
        self.date_emprunt = date.today()
        self.date_retour = None

    def retourner(self):
        self.date_retour = date.today()

    def afficher_infos(self):
        statut = "Retourné" if self.date_retour else "En cours"
        return (
            f"Lecteur : {self.lecteur.nom} {self.lecteur.prenom} | "
            f"Livre : {self.livre.titre} | "
            f"Date emprunt : {self.date_emprunt} | Statut : {statut}"
        )