import streamlit as st
from bibliotheque import Bibliotheque
from livre import Livre
from lecteur import Etudiant, Enseignant

st.set_page_config(page_title="Gestion Bibliothèque", layout="wide")
st.title("📚 Application de gestion de bibliothèque")

if "biblio" not in st.session_state:
    st.session_state.biblio = Bibliotheque("Bibliothèque Universitaire")

biblio = st.session_state.biblio

menu = st.sidebar.radio(
    "Menu",
    [
        "Ajouter un livre",
        "Ajouter un étudiant",
        "Ajouter un enseignant",
        "Afficher les livres",
        "Afficher les lecteurs",
        "Emprunter un livre",
        "Retourner un livre",
        "Afficher les emprunts"
    ]
)

if menu == "Ajouter un livre":
    st.header("Ajouter un livre")

    code = st.text_input("Code du livre")
    titre = st.text_input("Titre")
    auteur = st.text_input("Auteur")
    categorie = st.text_input("Catégorie")
    exemplaires = st.number_input("Nombre d'exemplaires", min_value=0, step=1)

    if st.button("Enregistrer"):
        livre = Livre(code, titre, auteur, categorie, int(exemplaires))
        biblio.ajouter_livre(livre)
        st.success("Livre ajouté avec succès")

elif menu == "Ajouter un étudiant":
    st.header("Ajouter un étudiant")

    identifiant = st.text_input("Matricule")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    annee_naissance = st.text_input("Année de naissance")
    telephone = st.text_input("Téléphone")
    filiere = st.text_input("Filière")

    if st.button("Enregistrer l'étudiant"):
        etudiant = Etudiant(identifiant, nom, prenom, annee_naissance, telephone, filiere)
        biblio.ajouter_lecteur(etudiant)
        st.success("Étudiant ajouté avec succès")

elif menu == "Ajouter un enseignant":
    st.header("Ajouter un enseignant")

    identifiant = st.text_input("Identifiant")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    annee_naissance = st.text_input("Année de naissance")
    telephone = st.text_input("Téléphone")
    departement = st.text_input("Département")

    if st.button("Enregistrer l'enseignant"):
        enseignant = Enseignant(identifiant, nom, prenom, annee_naissance, telephone, departement)
        biblio.ajouter_lecteur(enseignant)
        st.success("Enseignant ajouté avec succès")

elif menu == "Afficher les livres":
    st.header("Liste des livres")

    if not biblio.livres:
        st.info("Aucun livre enregistré.")
    else:
        data = [{
            "Code": l.code,
            "Titre": l.titre,
            "Auteur": l.auteur,
            "Catégorie": l.categorie,
            "Exemplaires": l.exemplaires
        } for l in biblio.livres]

        st.dataframe(data, use_container_width=True, height=500)

elif menu == "Afficher les lecteurs":
    st.header("Liste des lecteurs")

    if not biblio.lecteurs:
        st.info("Aucun lecteur enregistré.")
    else:
        data = []
        for lecteur in biblio.lecteurs:
            type_lecteur = "Étudiant" if isinstance(lecteur, Etudiant) else "Enseignant"

            data.append({
                "Identifiant": lecteur.identifiant,
                "Nom": lecteur.nom,
                "Prénom": lecteur.prenom,
                "Année naissance": lecteur.annee_naissance,
                "Téléphone": lecteur.telephone,
                "Type": type_lecteur
            })

        st.dataframe(data, use_container_width=True, height=500)

elif menu == "Emprunter un livre":
    st.header("Emprunter un livre")

    if not biblio.lecteurs or not biblio.livres:
        st.warning("Veuillez d'abord ajouter au moins un lecteur et un livre.")
    else:
        lecteurs = {
            f"{lecteur.identifiant} - {lecteur.nom} {lecteur.prenom}": lecteur.identifiant
            for lecteur in biblio.lecteurs
        }

        livres = {
            f"{livre.code} - {livre.titre} ({livre.exemplaires} ex.)": livre.code
            for livre in biblio.livres
            if livre.exemplaires > 0
        }

        lecteur_choisi = st.selectbox("Choisir un lecteur", list(lecteurs.keys()))

        if livres:
            livre_choisi = st.selectbox("Choisir un livre disponible", list(livres.keys()))

            if st.button("Enregistrer l'emprunt"):
                biblio.emprunter_livre(
                    lecteurs[lecteur_choisi],
                    livres[livre_choisi]
                )
                st.success("Emprunt enregistré avec succès.")
        else:
            st.error("Aucun livre disponible.")

elif menu == "Retourner un livre":
    st.header("Retourner un livre")

    emprunts_en_cours = [
        e for e in biblio.emprunts
        if e.date_retour is None
    ]

    if not emprunts_en_cours:
        st.info("Aucun emprunt en cours.")
    else:
        choix = {
            f"{e.lecteur.identifiant} - {e.lecteur.nom} {e.lecteur.prenom} | {e.livre.code} - {e.livre.titre}": e
            for e in emprunts_en_cours
        }

        emprunt_choisi = st.selectbox("Choisir l'emprunt à retourner", list(choix.keys()))

        if st.button("Retourner le livre"):
            emprunt = choix[emprunt_choisi]
            biblio.retourner_livre(emprunt.lecteur.identifiant, emprunt.livre.code)
            st.success("Livre retourné avec succès.")

elif menu == "Afficher les emprunts":
    st.header("Liste des emprunts")

    if not biblio.emprunts:
        st.info("Aucun emprunt enregistré.")
    else:
        data = []

        for e in biblio.emprunts:
            data.append({
                "Lecteur": f"{e.lecteur.nom} {e.lecteur.prenom}",
                "Livre": e.livre.titre,
                "Date emprunt": str(e.date_emprunt),
                "Date retour": str(e.date_retour) if e.date_retour else "",
                "Statut": "Retourné" if e.date_retour else "En cours"
            })

        st.dataframe(data, use_container_width=True, height=500)