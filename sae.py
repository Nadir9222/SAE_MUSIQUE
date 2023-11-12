import tkinter as tk

def recherche():
    # Vous pouvez ajouter ici le code pour effectuer la recherche
    pass

def accueil():
    print("Fonction Accueil")

def inscription():
    print("Fonction S'inscrire")

def connexion():
    print("Fonction Se connecter")

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("Barre de Navigation avec Barre de Recherche")

# Créer une barre de menu
barre_menu = tk.Menu(fenetre)

# Ajouter des boutons au menu
barre_menu.add_command(label="Accueil", command=accueil)
barre_menu.add_command(label="S'inscrire", command=inscription)
barre_menu.add_command(label="Se connecter", command=connexion)

# Configurer la fenêtre pour utiliser la barre de menu
fenetre.config(menu=barre_menu)

# Créer une Frame pour contenir la barre de recherche et les boutons
frame_principale = tk.Frame(fenetre)
frame_principale.pack()

# Créer une zone de texte pour la recherche
entry = tk.Entry(frame_principale, font=("Arial", 14), width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Créer un bouton de recherche
button_recherche = tk.Button(frame_principale, text="Rechercher", command=recherche, font=("Arial", 14), bg='#4285F4', fg='white')
button_recherche.grid(row=0, column=1, pady=10, padx=(0, 10))  # Ajout d'un espacement à droite

# Bouton Accueil
button_accueil = tk.Button(frame_principale, text="Accueil", command=accueil, font=("Arial", 12), bg='#4285F4', fg='white')
button_accueil.grid(row=0, column=2, padx=10)

# Bouton S'inscrire
button_inscription = tk.Button(frame_principale, text="S'inscrire", command=inscription, font=("Arial", 12), bg='#4285F4', fg='white')
button_inscription.grid(row=0, column=3, padx=10)

# Bouton Se connecter
button_connexion = tk.Button(frame_principale, text="Se connecter", command=connexion, font=("Arial", 12), bg='#4285F4', fg='white')
button_connexion.grid(row=0, column=4, padx=10)

# Lancer la boucle principale
fenetre.mainloop()