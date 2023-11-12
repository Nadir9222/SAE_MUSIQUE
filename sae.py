from tkinter import *

# creer une premiere fenetre
window = Tk()

# personaliser cette fenetre
window.title("Mon appli")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#41B77F')

# ajouter un premier bouton connecter
co_button = Button(window, text="Se connecter", font=("Arial", 20), bg='white', fg='#41B77F')
co_button.pack()

# ajouter un deuxieme bouton s'inscrire
sing_button = Button(window, text="s'inscrire", font=("Arial", 20), bg='white', fg='#41B77F')
sing_button.pack()

# ajouter un troisème bouton acceuil
home_button = Button(window, text="Acceuil", font=("Arial", 20), bg='white', fg='#41B77F')
home_button.pack()



# afficher
window.mainloop()
