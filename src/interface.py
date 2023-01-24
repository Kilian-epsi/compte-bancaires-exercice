import compte

# DELCARATION DES CONSTANTES ET VARIABLES
LOGO = \
    """\033[1;32m
                                 ╓▄▄▄▓████████████▓▄▄▄╖
                        ▄▄████████████████████████████▄▄
                    ╓▄████████████████████████████████████▄╖
                 ,▄██████████████████████████████████████████▄,
           ,╓▄▄▄█████████████▀▀▀╙`             ╙▀▀▀█████████████▄▄▄╖,
        ,▄███████████████▀'                           ▀▀██████████████▓,
       ▄█████████████▀╙                                  "▀█████████████▄
      ▐████████████▀                                        ▀████████████▌
      ███████████▓                                            ▀███████████H
     ▐██████████▀                                              ╙██████████▓
     ██████████▀                                                ╙██████████
     ██████████                                                  ▀█████████
     ▓████████▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█████████
     ╘████████████████████████████████████████████████████████████████████▌
    ,▄████████▀╙╙▀█████████████████████╙╙▀█████████████████████╙╙▀████████▓,
   ▄██████████@   ███████████████████▓    ▀███████████████████`  ]██████████▄
  ╔███████▀╙ ╙▓   ▐█████████████████▀      ╙█████████████████▌   ▐▀ ╙▀███████▌
  ███████▌         ▀███████████████╩        └████████████████    `    ╙███████
  ███████W            ``````````                ``````````             ███████
  ▐███████▄                         ,▄▄▄▄▄▄,                         ╓███████▓
   ▓███████████,                   '████████┘                    ▓███████████
    ▀███████████▄                                               ███████████▀
      ╙▀█████████████▓▄╖        ╓▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ,▄▄██████████████▀
         ▐████████████████▄,  ▄███████████████████   ▄████████████████▌
         ▐███████████████████▄████████████████████▓▓██████████████████▌
         ▐████████████████████████████████████████████████████████████▌
         ▐██████████████████████████        ██████████████████████████▌
         ▐██████████████████████████▄██████▓▓█████████████████████████▌
         ▐████████████████████████████████████████████████████████████▌
         ▐████████████████████████████████████████████████████████████▌
    ██████╗  █████╗ ███╗   ██╗██╗  ██╗    ██████╗  ██████╗  ██████╗ ████████╗
    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝
    ██████╔╝███████║██╔██╗ ██║█████╔╝     ██████╔╝██║   ██║██║   ██║   ██║   
    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗     ██╔══██╗██║   ██║██║   ██║   ██║   
    ██████╔╝██║  ██║██║ ╚████║██║  ██╗    ██║  ██║╚██████╔╝╚██████╔╝   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   
                                                Don't worry, you're poor.
\033"""
LOGO_COMPTE = \
    """\033[1;33m
      __  __              ____                      _                
     |  \/  | ___  ___   / ___|___  _ __ ___  _ __ | |_ ___  ___   _ 
     | |\/| |/ _ \/ __| | |   / _ \| '_ ` _ \| '_ \| __/ _ \/ __| (_)
     | |  | |  __/\__ \ | |__| (_) | | | | | | |_) | ||  __/\__ \  _ 
     |_|  |_|\___||___/  \____\___/|_| |_| |_| .__/ \__\___||___/ (_)
                                             |_|                     \033"""
LOGO_RETRAIT = """
██████╗ ███████╗████████╗██████╗  █████╗ ██╗████████╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║╚══██╔══╝
██████╔╝█████╗     ██║   ██████╔╝███████║██║   ██║   
██╔══██╗██╔══╝     ██║   ██╔══██╗██╔══██║██║   ██║   
██║  ██║███████╗   ██║   ██║  ██║██║  ██║██║   ██║   
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                               """
LOGO_VERSEMENT = """
██╗   ██╗███████╗██████╗ ███████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██║   ██║█████╗  ██████╔╝███████╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
 ╚████╔╝ ███████╗██║  ██║███████║███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   """
MESSAGE_ACCUEIL = "\nBienvenue sur votre application banquaire.\n" \
                  "Choississez un compte:\n" \
                  " ________________________\n" \
                  "| 1- Mon compte Courant  |\n" \
                  " ------------------------\n" \
                  " ________________________\n" \
                  "| 2- Mon compte Epargne  |\n" \
                  " ------------------------\n"
CHOIX_VERSEMENT_RETRAIT = "Que souhaitez vous faire :\n" \
                          " _____________________________________\n" \
                          "| 1-       Retirer de l'argent        |\n" \
                          " -------------------------------------\n" \
                          " _____________________________________\n" \
                          "| 2-       Verser de l'argent         |\n" \
                          " -------------------------------------\n" \
                          " _____________________________________\n" \
                          "| 3-             Retour               |\n" \
                          " -------------------------------------\n" \

TAB_REP = [1, 2]
TAB_REP2 = [1, 2, 3]

mon_compte_epargne = compte.CompteEpargne('kilian')
mon_compte_courant = compte.CompteCourant('kilian')

def lancement():
    print(LOGO)
    print(MESSAGE_ACCUEIL)
    print("Votre choix (1 ou 2):")
    choix1 = int(input())
    while choix1 not in TAB_REP:
        choix1 = input("Merci de choisir un compte valide (1 ou 2) : ")
        choix1 = int(choix1)
    if choix1 == 1:
        affichageCompte(mon_compte_courant, intitule="courant")
    else:
        affichageCompte(mon_compte_epargne, intitule="épargne")

def affichageCompte(mon_compte, intitule):
    print(LOGO_COMPTE)
    print("Voici le solde de votre compte {} : ".format(intitule))
    print(mon_compte.afficherSolde())
    print(CHOIX_VERSEMENT_RETRAIT)
    choix2 = int(input())
    while choix2 not in TAB_REP2:
        choix2 = input("Merci de choisir une action valide (1, 2 ou 3) : ")
        choix2 = int(choix2)
    if choix2 == 1:
        retraitCompte(mon_compte, intitule)
    elif choix2 == 2:
        versementCompte(mon_compte, intitule)
    else:
        lancement()

def retraitCompte(mon_compte, intitule):
    print(LOGO_RETRAIT)
    print("Quel montant souhaitez vous retirer ?")
    choix3 = float(input())
    while type(choix3) != float:
        choix3 = input("Merci de rentrer un montant valide")
        choix3 = float(choix3)
    mon_compte.retrait(choix3)
    affichageCompte(mon_compte, intitule)

def versementCompte(mon_compte, intitule):
    print(LOGO_VERSEMENT)
    print("Quel montant souhaitez vous verser ?")
    choix4 = float(input())
    while type(choix4) != float:
        choix4 = input("Merci de rentrer un montant valide")
        choix4 = float(choix4)
    mon_compte.versement(choix4)
    print(mon_compte.afficherSolde())
    affichageCompte(mon_compte, intitule)
