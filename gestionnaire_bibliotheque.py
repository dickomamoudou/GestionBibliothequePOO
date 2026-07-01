from bibliotheque import Bibliotheque
from livre import Livre
from lecteur import Etudiant, Enseignant


class GestionnaireBibliotheque:
    def __init__(self):
        self.bibliotheque = Bibliotheque("Bibliothèque Universitaire")

    def menu(self):
        while True:
            print("\n========== MENU BIBLIOTHEQUE ==========")
            print("1. Ajouter un livre")
            print("2. Ajouter un étudiant")
            print("3. Ajouter un enseignant")
            print("4. Afficher les livres")
            print("5. Afficher les lecteurs")
            print("6. Emprunter un livre")
            print("7. Retourner un livre")
            print("8. Afficher les emprunts")
            print("0. Quitter")

            choix = input("Votre choix : ")

            if choix == "1":
                self.ajouter_livre()
            elif choix == "2":
                self.ajouter_etudiant()
            elif choix == "3":
                self.ajouter_enseignant()
            elif choix == "4":
                self.bibliotheque.afficher_livres()
            elif choix == "5":
                self.bibliotheque.afficher_lecteurs()
            elif choix == "6":
                self.emprunter_livre()
            elif choix == "7":
                self.retourner_livre()
            elif choix == "8":
                self.bibliotheque.afficher_emprunts()
            elif choix == "0":
                print("Fin du programme.")
                break
            else:
                print("Choix invalide.")

    def ajouter_livre(self):
        code = input("Code du livre : ")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        categorie = input("Catégorie : ")

        try:
            exemplaires = int(input("Nombre d'exemplaires : "))
            livre = Livre(code, titre, auteur, categorie, exemplaires)
            self.bibliotheque.ajouter_livre(livre)
        except ValueError:
            print("Le nombre d'exemplaires doit être un entier.")

    def ajouter_etudiant(self):
        identifiant = input("Matricule étudiant : ")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        annee_naissance = input("Année de naissance : ")
        telephone = input("Téléphone : ")
        filiere = input("Filière : ")

        etudiant = Etudiant(
            identifiant, nom, prenom, annee_naissance, telephone, filiere
        )
        self.bibliotheque.ajouter_lecteur(etudiant)

    def ajouter_enseignant(self):
        identifiant = input("Identifiant enseignant : ")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        annee_naissance = input("Année de naissance : ")
        telephone = input("Téléphone : ")
        departement = input("Département : ")

        enseignant = Enseignant(
            identifiant, nom, prenom, annee_naissance, telephone, departement
        )
        self.bibliotheque.ajouter_lecteur(enseignant)

    def emprunter_livre(self):
        identifiant = input("Identifiant du lecteur : ")
        code = input("Code du livre : ")
        self.bibliotheque.emprunter_livre(identifiant, code)

    def retourner_livre(self):
        identifiant = input("Identifiant du lecteur : ")
        code = input("Code du livre : ")
        self.bibliotheque.retourner_livre(identifiant, code)