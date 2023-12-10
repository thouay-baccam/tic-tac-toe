from tkinter import *
import random

# *******************************
# *     INTERFACE GRAPHIQUE     *
# *******************************

# Initialisation de la fenêtre principale
fenetre = Tk()
fenetre.title("Tic-Tac-Toe")

# Configuration des couleurs de fond et de texte, taille, et résistance au redimensionnement
couleur_fond_mode_sombre = "#121212"
couleur_texte_mode_sombre = "white"
fenetre.configure(bg=couleur_fond_mode_sombre)
fenetre.geometry("400x400")
fenetre.resizable(False, False)

# *****************************
# *         VARIABLES         *
# *****************************

joueurs = ["X", "O"]
joueur = random.choice(joueurs)

# *****************************
# *         FONCTIONS         *
# *****************************

def joueur_suivant():
    global joueur
    joueur = joueurs[1] if joueur == joueurs[0] else joueurs[0]
    etiquette.config(text=f"À ton tour, Monsieur {joueur}")

def mettre_a_jour_interface():
    fenetre.update()

def verifier_gagnant():
    for ligne_a_verifier in lignes_a_verifier:
        if boutons[ligne_a_verifier[0][0]][ligne_a_verifier[0][1]]['text'] == boutons[ligne_a_verifier[1][0]][ligne_a_verifier[1][1]]['text'] == boutons[ligne_a_verifier[2][0]][ligne_a_verifier[2][1]]['text'] != "":
            mettre_en_valeur_ligne_gagnante(ligne_a_verifier)
            return True

    if not espaces_vides():
        mettre_en_valeur_match_nul()
        return "Match nul"

    return False

def mettre_en_valeur_ligne_gagnante(ligne):
    for position in ligne:
        boutons[position[0]][position[1]].config(bg="green")

def mettre_en_valeur_match_nul():
    for ligne in range(3):
        for colonne in range(3):
            boutons[ligne][colonne].config(bg="yellow")

def espaces_vides():
    return any(boutons[ligne][colonne]['text'] == "" for ligne in range(3) for colonne in range(3))

def fin_de_partie():
    if verifier_gagnant() is True:
        etiquette.config(text=f"Monsieur {joueur} a gagné!")
    else:
        etiquette.config(text="Match nul!")

    desactiver_boutons()

def tour_suivant(ligne, colonne):
    global joueur

    if boutons[ligne][colonne]['text'] == "" and not verifier_gagnant():
        boutons[ligne][colonne]['text'] = joueur
        if not verifier_gagnant():
            joueur_suivant()
        else:
            fin_de_partie()

    mettre_a_jour_interface()

def nouvelle_partie():
    global joueur
    activer_boutons()
    joueur = random.choice(joueurs)
    etiquette.config(text=f"Tu commences, Monsieur {joueur}")
    reinitialiser_plateau()

def reinitialiser_plateau():
    for ligne in range(3):
        for colonne in range(3):
            boutons[ligne][colonne].config(text="", bg=couleur_fond_mode_sombre)

def desactiver_boutons():
    for ligne in range(3):
        for colonne in range(3):
            boutons[ligne][colonne].config(state=DISABLED)

def activer_boutons():
    for ligne in range(3):
        for colonne in range(3):
            boutons[ligne][colonne].config(state=NORMAL)

# *******************************
# *     INTERFACE GRAPHIQUE     *
# *******************************

# Création de l'étiquette pour afficher les messages du jeu
etiquette = Label(text=f"Tu commences, Monsieur {joueur}", font=('Arial', 18), bg=couleur_fond_mode_sombre, fg=couleur_texte_mode_sombre)
etiquette.pack(side="top", pady=10)

# Création du cadre pour contenir les boutons du plateau
cadre = Frame(fenetre, bg=couleur_fond_mode_sombre)
cadre.pack()

# Création des boutons du plateau
boutons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lignes_a_verifier = [((0, 0), (0, 1), (0, 2)),
                     ((1, 0), (1, 1), (1, 2)),
                     ((2, 0), (2, 1), (2, 2)),
                     ((0, 0), (1, 0), (2, 0)),
                     ((0, 1), (1, 1), (2, 1)),
                     ((0, 2), (1, 2), (2, 2)),
                     ((0, 0), (1, 1), (2, 2)),
                     ((0, 2), (1, 1), (2, 0))]

# Création des boutons avec des propriétés spécifiques
for ligne in range(3):
    for colonne in range(3):
        boutons[ligne][colonne] = Button(cadre, text="", font=('Arial', 18), width=5, height=2, command=lambda ligne=ligne, colonne=colonne: tour_suivant(ligne, colonne), bg=couleur_fond_mode_sombre, fg=couleur_texte_mode_sombre)
        boutons[ligne][colonne].grid(row=ligne, column=colonne, padx=5, pady=5)

# Création du bouton de réinitialisation
bouton_reset = Button(text="RECOMMENCER", font=('Arial', 14), command=nouvelle_partie, bg=couleur_fond_mode_sombre, fg=couleur_texte_mode_sombre)
bouton_reset.pack(side="top", pady=10)

# Lancement de la boucle principale tkinter
fenetre.mainloop()