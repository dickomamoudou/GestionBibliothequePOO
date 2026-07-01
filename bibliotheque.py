from emprunt import Emprunt


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []
        self.lecteurs = []
        self.emprunts = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print("Livre ajouté avec succès.")

    def ajouter_lecteur(self, lecteur):
        self.lecteurs.append(lecteur)
        print("Lecteur ajouté avec succès.")

    def chercher_livre(self, code):
        for livre in self.livres:
            if livre.code == code:
                return livre
        return None

    def chercher_lecteur(self, identifiant):
        for lecteur in self.lecteurs:
            if lecteur.identifiant == identifiant:
                return lecteur
        return None

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre enregistré.")
        else:
            for livre in self.livres:
                print(livre.afficher_infos())

    def afficher_lecteurs(self):
        if not self.lecteurs:
            print("Aucun lecteur enregistré.")
        else:
            for lecteur in self.lecteurs:
                print(lecteur.afficher_infos())

    def emprunter_livre(self, identifiant_lecteur, code_livre):
        lecteur = self.chercher_lecteur(identifiant_lecteur)
        livre = self.chercher_livre(code_livre)

        if lecteur is None:
            print("Lecteur introuvable.")
            return

        if livre is None:
            print("Livre introuvable.")
            return

        if not livre.est_disponible():
            print("Livre non disponible.")
            return

        emprunt = Emprunt(lecteur, livre)
        self.emprunts.append(emprunt)

        livre.exemplaires -= 1
        lecteur.emprunter_livre(livre)

        print("Emprunt enregistré avec succès.")

    def retourner_livre(self, identifiant_lecteur, code_livre):
        for emprunt in self.emprunts:
            if (
                emprunt.lecteur.identifiant == identifiant_lecteur
                and emprunt.livre.code == code_livre
                and emprunt.date_retour is None
            ):
                emprunt.retourner()
                emprunt.livre.exemplaires += 1
                emprunt.lecteur.retourner_livre(emprunt.livre)
                print("Livre retourné avec succès.")
                return

        print("Aucun emprunt en cours trouvé.")

    def afficher_emprunts(self):
        if not self.emprunts:
            print("Aucun emprunt enregistré.")
        else:
            for emprunt in self.emprunts:
                print(emprunt.afficher_infos())