import tkinter as tk
from tkinter import *
import tkinter.font as font

from src import compte

window = Tk()
window.title("Banque Root")
window.geometry("390x750")
window.iconbitmap("logo.ico")
window.resizable(width=False, height=False)
window.config(background='#ffffff')
logo = PhotoImage(file="logo.png")
f20 = font.Font(size=20)
f15 = font.Font(size=15)
f10 = font.Font(size=10)

# creation de la page de connexion
mon_compte_epargne = compte.CompteEpargne('kilian')
mon_compte_courant = compte.CompteCourant('kilian')


# logo
def pageConnexion():
    def pageAccueil():
        def pageCc():
            label_titre.destroy()
            label_t2.destroy()
            bouton_ce.destroy()
            bouton_cc.destroy()
            label_titre_cc = Label(window, text="Voici le solde de votre compte :")
            label_titre_cc.pack()
            label_solde_cc = Label(window, text= mon_compte_courant.afficherSolde())
            label_solde_cc.pack()
            label_versement_cc = Label(window, text="Versement")
            label_versement_cc.pack()
            entry_versement_cc = Entry(window)
            entry_versement_cc.pack()
            bouton_v_cc = Button(window, text="OK", command= lambda: [mon_compte_courant.versement(int(entry_versement_cc.get())), pageCe()])
            bouton_v_cc.pack()
            label_retrait_cc = Label(window, text="Retrait")
            label_retrait_cc.pack()
            entry_retrait_cc = Entry(window)
            entry_retrait_cc.pack()
            bouton_r_cc = Button(window, text="OK", command= lambda : mon_compte_courant.retrait(int(entry_retrait_cc.get())))
            bouton_r_cc.pack()

        def pageCe():
            label_titre.destroy()
            label_t2.destroy()
            bouton_ce.destroy()
            bouton_cc.destroy()
            label_titre_ce = Label(window, text="Voici le solde de votre compte :")
            label_titre_ce.pack()
            label_solde_ce = Label(window, text= mon_compte_epargne.afficherSolde())
            label_solde_ce.pack()
            label_versement_ce = Label(window, text="Versement")
            label_versement_ce.pack()
            entry_versement_ce = Entry(window)
            entry_versement_ce.pack()
            bouton_v_ce = Button(window, text="OK", command= lambda :   mon_compte_courant.versement(int(entry_versement_ce.get())))
            bouton_v_ce.pack()
            label_retrait_ce = Label(window, text="Retrait")
            label_retrait_ce.pack()
            entry_retrait_ce = Entry(window)
            entry_retrait_ce.pack()
            bouton_r_ce = Button(window, text="OK", command= lambda : mon_compte_courant.retrait(int(entry_retrait_ce.get())))
            bouton_r_ce.pack()

        logo_label.destroy()
        bouton_connexion.destroy()
        label_titre = Label(window, text="Bonjour " + mon_compte_courant.nomProprietaire + "!")
        label_titre['font'] = f15
        label_titre.pack()
        label_t2 = Label(window, text="Quel compte souhaitez vous utiliser? ")
        label_t2['font'] = f10
        label_t2.pack()
        bouton_cc = Button(window, text="Compte Courant", command=pageCc)
        bouton_cc['font'] = f15
        bouton_cc.pack()
        bouton_ce = Button(window, text="Compte Epargne", command=pageCe)
        bouton_ce['font'] = f15
        bouton_ce.pack()

    logo_label = tk.Label(window, image=logo)
    logo_label.pack()
    # bouton connexion
    bouton_connexion = Button(window, text="Connexion", command=pageAccueil)
    bouton_connexion['font'] = f20
    bouton_connexion.pack()



pageConnexion()
window.mainloop()
