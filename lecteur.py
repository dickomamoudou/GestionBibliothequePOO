from personne import Personne


class Lecteur(Personne):
    def __init__(self, identifiant, nom, prenom, annee_naissance, telephone):
        super().__init__(identifiant, nom, prenom, annee_naissance, telephone)
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        self.livres_empruntes.append(livre)

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)


class Etudiant(Lecteur):
    def __init__(self, identifiant, nom, prenom, annee_naissance, telephone, filiere):
        super().__init__(identifiant, nom, prenom, annee_naissance, telephone)
        self.filiere = filiere

    def afficher_infos(self):
        return f"Etudiant : {super().afficher_infos()} | Filière : {self.filiere}"


class Enseignant(Lecteur):
    def __init__(self, identifiant, nom, prenom, annee_naissance, telephone, departement):
        super().__init__(identifiant, nom, prenom, annee_naissance, telephone)
        self.departement = departement

    def afficher_infos(self):
        return f"Enseignant : {super().afficher_infos()} | Département : {self.departement}"