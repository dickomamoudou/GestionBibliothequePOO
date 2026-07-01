class Personne:
    def __init__(self, identifiant, nom, prenom, annee_naissance, telephone):
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom
        self.annee_naissance = annee_naissance
        self.telephone = telephone

    def afficher_infos(self):
        return (
            f"{self.identifiant} - {self.nom} {self.prenom} | "
            f"Année naissance : {self.annee_naissance} | "
            f"Téléphone : {self.telephone}"
        )