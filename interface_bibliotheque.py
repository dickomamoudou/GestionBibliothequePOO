import tkinter as tk
from tkinter import ttk, messagebox

from bibliotheque import Bibliotheque
from livre import Livre
from lecteur import Etudiant, Enseignant


class InterfaceBibliotheque(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Bibliothèque - POO")
        self.geometry("1100x650")
        self.minsize(950, 580)

        self.bibliotheque = Bibliotheque("Bibliothèque Universitaire")

        self._configurer_style()
        self._creer_interface()
        self.actualiser_tout()

    def _configurer_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TNotebook.Tab", padding=(18, 8), font=("Segoe UI", 10, "bold"))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", padding=6)
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))

    def _creer_interface(self):
        titre = ttk.Label(self, text="Système de Gestion de Bibliothèque", style="Title.TLabel")
        titre.pack(pady=10)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=12, pady=8)

        self.frame_livres = ttk.Frame(self.notebook)
        self.frame_lecteurs = ttk.Frame(self.notebook)
        self.frame_emprunts = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_livres, text="📚 Livres")
        self.notebook.add(self.frame_lecteurs, text="👤 Lecteurs")
        self.notebook.add(self.frame_emprunts, text="🔄 Emprunts / Retours")

        self._onglet_livres()
        self._onglet_lecteurs()
        self._onglet_emprunts()

    def _onglet_livres(self):
        form = ttk.LabelFrame(self.frame_livres, text="Ajouter un livre")
        form.pack(fill="x", padx=10, pady=10)

        self.var_code = tk.StringVar()
        self.var_titre = tk.StringVar()
        self.var_auteur = tk.StringVar()
        self.var_categorie = tk.StringVar()
        self.var_exemplaires = tk.StringVar()

        champs = [
            ("Code", self.var_code),
            ("Titre", self.var_titre),
            ("Auteur", self.var_auteur),
            ("Catégorie", self.var_categorie),
            ("Exemplaires", self.var_exemplaires),
        ]
        for i, (label, var) in enumerate(champs):
            ttk.Label(form, text=label).grid(row=0, column=i, padx=5, pady=5, sticky="w")
            ttk.Entry(form, textvariable=var, width=20).grid(row=1, column=i, padx=5, pady=5)

        ttk.Button(form, text="Ajouter", command=self.ajouter_livre).grid(row=1, column=len(champs), padx=10)
        ttk.Button(form, text="Vider", command=self.vider_livre).grid(row=1, column=len(champs) + 1, padx=5)

        colonnes = ("code", "titre", "auteur", "categorie", "exemplaires")
        self.tree_livres = ttk.Treeview(self.frame_livres, columns=colonnes, show="headings")
        for col, text, width in [
            ("code", "Code", 100), ("titre", "Titre", 260), ("auteur", "Auteur", 200),
            ("categorie", "Catégorie", 160), ("exemplaires", "Exemplaires", 100),
        ]:
            self.tree_livres.heading(col, text=text)
            self.tree_livres.column(col, width=width, anchor="center")
        self.tree_livres.pack(fill="both", expand=True, padx=10, pady=10)

    def _onglet_lecteurs(self):
        form = ttk.LabelFrame(self.frame_lecteurs, text="Ajouter un lecteur")
        form.pack(fill="x", padx=10, pady=10)

        self.var_type = tk.StringVar(value="Etudiant")
        self.var_id = tk.StringVar()
        self.var_nom = tk.StringVar()
        self.var_prenom = tk.StringVar()
        self.var_naissance = tk.StringVar()
        self.var_tel = tk.StringVar()
        self.var_specialite = tk.StringVar()

        champs = [
            ("Type", "combo"), ("Identifiant", self.var_id), ("Nom", self.var_nom),
            ("Prénom", self.var_prenom), ("Année naissance", self.var_naissance),
            ("Téléphone", self.var_tel), ("Filière/Département", self.var_specialite),
        ]
        for i, (label, var) in enumerate(champs):
            ttk.Label(form, text=label).grid(row=0, column=i, padx=4, pady=5, sticky="w")
            if var == "combo":
                ttk.Combobox(form, textvariable=self.var_type, values=("Etudiant", "Enseignant"), width=13, state="readonly").grid(row=1, column=i, padx=4, pady=5)
            else:
                ttk.Entry(form, textvariable=var, width=17).grid(row=1, column=i, padx=4, pady=5)

        ttk.Button(form, text="Ajouter", command=self.ajouter_lecteur).grid(row=1, column=len(champs), padx=10)
        ttk.Button(form, text="Vider", command=self.vider_lecteur).grid(row=1, column=len(champs) + 1, padx=5)

        colonnes = ("type", "id", "nom", "prenom", "naissance", "telephone", "specialite")
        self.tree_lecteurs = ttk.Treeview(self.frame_lecteurs, columns=colonnes, show="headings")
        for col, text, width in [
            ("type", "Type", 100), ("id", "Identifiant", 120), ("nom", "Nom", 150),
            ("prenom", "Prénom", 150), ("naissance", "Naissance", 100),
            ("telephone", "Téléphone", 130), ("specialite", "Filière/Département", 190),
        ]:
            self.tree_lecteurs.heading(col, text=text)
            self.tree_lecteurs.column(col, width=width, anchor="center")
        self.tree_lecteurs.pack(fill="both", expand=True, padx=10, pady=10)

    def _onglet_emprunts(self):
        form = ttk.LabelFrame(self.frame_emprunts, text="Emprunter ou retourner un livre")
        form.pack(fill="x", padx=10, pady=10)

        self.var_emprunt_lecteur = tk.StringVar()
        self.var_emprunt_livre = tk.StringVar()

        ttk.Label(form, text="Identifiant lecteur").grid(row=0, column=0, padx=6, pady=5, sticky="w")
        ttk.Entry(form, textvariable=self.var_emprunt_lecteur, width=25).grid(row=1, column=0, padx=6, pady=5)
        ttk.Label(form, text="Code livre").grid(row=0, column=1, padx=6, pady=5, sticky="w")
        ttk.Entry(form, textvariable=self.var_emprunt_livre, width=25).grid(row=1, column=1, padx=6, pady=5)
        ttk.Button(form, text="Emprunter", command=self.emprunter_livre).grid(row=1, column=2, padx=8)
        ttk.Button(form, text="Retourner", command=self.retourner_livre).grid(row=1, column=3, padx=8)
        ttk.Button(form, text="Actualiser", command=self.actualiser_tout).grid(row=1, column=4, padx=8)

        colonnes = ("lecteur", "livre", "date", "statut")
        self.tree_emprunts = ttk.Treeview(self.frame_emprunts, columns=colonnes, show="headings")
        for col, text, width in [
            ("lecteur", "Lecteur", 260), ("livre", "Livre", 300), ("date", "Date emprunt", 150), ("statut", "Statut", 120),
        ]:
            self.tree_emprunts.heading(col, text=text)
            self.tree_emprunts.column(col, width=width, anchor="center")
        self.tree_emprunts.pack(fill="both", expand=True, padx=10, pady=10)

    def ajouter_livre(self):
        code = self.var_code.get().strip()
        titre = self.var_titre.get().strip()
        auteur = self.var_auteur.get().strip()
        categorie = self.var_categorie.get().strip()
        exemplaires_txt = self.var_exemplaires.get().strip()

        if not all([code, titre, auteur, categorie, exemplaires_txt]):
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs du livre.")
            return
        if self.bibliotheque.chercher_livre(code):
            messagebox.showerror("Doublon", "Ce code de livre existe déjà.")
            return
        try:
            exemplaires = int(exemplaires_txt)
            if exemplaires < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Le nombre d'exemplaires doit être un entier positif.")
            return

        self.bibliotheque.ajouter_livre(Livre(code, titre, auteur, categorie, exemplaires))
        self.vider_livre()
        self.actualiser_tout()
        messagebox.showinfo("Succès", "Livre ajouté avec succès.")

    def ajouter_lecteur(self):
        identifiant = self.var_id.get().strip()
        nom = self.var_nom.get().strip()
        prenom = self.var_prenom.get().strip()
        naissance = self.var_naissance.get().strip()
        tel = self.var_tel.get().strip()
        specialite = self.var_specialite.get().strip()

        if not all([identifiant, nom, prenom, naissance, tel, specialite]):
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs du lecteur.")
            return
        if self.bibliotheque.chercher_lecteur(identifiant):
            messagebox.showerror("Doublon", "Cet identifiant de lecteur existe déjà.")
            return

        if self.var_type.get() == "Etudiant":
            lecteur = Etudiant(identifiant, nom, prenom, naissance, tel, specialite)
        else:
            lecteur = Enseignant(identifiant, nom, prenom, naissance, tel, specialite)

        self.bibliotheque.ajouter_lecteur(lecteur)
        self.vider_lecteur()
        self.actualiser_tout()
        messagebox.showinfo("Succès", "Lecteur ajouté avec succès.")

    def emprunter_livre(self):
        identifiant = self.var_emprunt_lecteur.get().strip()
        code = self.var_emprunt_livre.get().strip()
        lecteur = self.bibliotheque.chercher_lecteur(identifiant)
        livre = self.bibliotheque.chercher_livre(code)

        if lecteur is None:
            messagebox.showerror("Erreur", "Lecteur introuvable.")
            return
        if livre is None:
            messagebox.showerror("Erreur", "Livre introuvable.")
            return
        if not livre.est_disponible():
            messagebox.showwarning("Indisponible", "Ce livre n'est pas disponible.")
            return

        self.bibliotheque.emprunter_livre(identifiant, code)
        self.actualiser_tout()
        messagebox.showinfo("Succès", "Emprunt enregistré avec succès.")

    def retourner_livre(self):
        identifiant = self.var_emprunt_lecteur.get().strip()
        code = self.var_emprunt_livre.get().strip()
        trouve = any(
            e.lecteur.identifiant == identifiant and e.livre.code == code and e.date_retour is None
            for e in self.bibliotheque.emprunts
        )
        if not trouve:
            messagebox.showwarning("Introuvable", "Aucun emprunt en cours trouvé pour ce lecteur et ce livre.")
            return
        self.bibliotheque.retourner_livre(identifiant, code)
        self.actualiser_tout()
        messagebox.showinfo("Succès", "Livre retourné avec succès.")

    def vider_livre(self):
        for var in [self.var_code, self.var_titre, self.var_auteur, self.var_categorie, self.var_exemplaires]:
            var.set("")

    def vider_lecteur(self):
        for var in [self.var_id, self.var_nom, self.var_prenom, self.var_naissance, self.var_tel, self.var_specialite]:
            var.set("")
        self.var_type.set("Etudiant")

    def actualiser_tout(self):
        self.actualiser_livres()
        self.actualiser_lecteurs()
        self.actualiser_emprunts()

    def actualiser_livres(self):
        self.tree_livres.delete(*self.tree_livres.get_children())
        for livre in self.bibliotheque.livres:
            self.tree_livres.insert("", "end", values=(livre.code, livre.titre, livre.auteur, livre.categorie, livre.exemplaires))

    def actualiser_lecteurs(self):
        self.tree_lecteurs.delete(*self.tree_lecteurs.get_children())
        for lecteur in self.bibliotheque.lecteurs:
            type_lecteur = lecteur.__class__.__name__
            specialite = getattr(lecteur, "filiere", getattr(lecteur, "departement", ""))
            self.tree_lecteurs.insert("", "end", values=(
                type_lecteur, lecteur.identifiant, lecteur.nom, lecteur.prenom,
                lecteur.annee_naissance, lecteur.telephone, specialite
            ))

    def actualiser_emprunts(self):
        self.tree_emprunts.delete(*self.tree_emprunts.get_children())
        for emprunt in self.bibliotheque.emprunts:
            statut = "Retourné" if emprunt.date_retour else "En cours"
            lecteur = f"{emprunt.lecteur.identifiant} - {emprunt.lecteur.nom} {emprunt.lecteur.prenom}"
            livre = f"{emprunt.livre.code} - {emprunt.livre.titre}"
            self.tree_emprunts.insert("", "end", values=(lecteur, livre, emprunt.date_emprunt, statut))


if __name__ == "__main__":
    app = InterfaceBibliotheque()
    app.mainloop()
