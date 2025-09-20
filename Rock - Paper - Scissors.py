'''Cahier des charges
Créer un jeu de pierre-papier-ciseaux en Python.
Le joueur doit pouvoir choisir entre pierre, papier ou ciseaux.
L'ordinateur doit faire un choix aléatoire entre pierre, papier ou ciseaux.

Le programme doit déterminer le gagnant en fonction des règles suivantes :
- La pierre bat les ciseaux (la pierre écrase les ciseaux)
- Les ciseaux battent le papier (les ciseaux coupent le papier)
- Le papier bat la pierre (le papier enveloppe la pierre)
Le programme doit afficher le choix du joueur, le choix de l'ordinateur et le résultat (gagnant, perdant ou égalité).
Le joueur doit pouvoir jouer plusieurs fois jusqu'à ce qu'il décide d'arrêter.

PS : Descriptions et Commentaires faite par une IA, le code à été fait manuellement.
'''

import random
import time

def choix_Ordi():
    '''
    Génère un choix aléatoire pour l'ordinateur parmi "Pierre", "Papier" et "Ciseaux".
    Retourne :
        str : Le choix de l'ordinateur.
    '''
    choix = ["Pierre", "Papier", "Ciseaux"]  # Liste des choix possibles
    return random.choice(choix)  # Retourne un choix aléatoire

def choix_Joueur():
    '''
    Demande au joueur de faire un choix entre "Pierre", "Papier" et "Ciseaux".
    Valide l'entrée utilisateur pour s'assurer qu'elle est correcte.
    Retourne :
        str : Le choix du joueur.
    '''
    choix = 0 
    while choix not in [1, 2, 3]:  # Vérifie que le choix est valide
        try:
            choix = int(input("Tu choisis quoi entre la 1.Pierre, la 2.Papier, ou le 3.Ciseaux ? "))
        except ValueError:
            choix = 0  # Réinitialise le choix en cas d'entrée invalide
    if choix == 1:
        return "Pierre"
    elif choix == 2:
        return "Papier"
    elif choix == 3:
        return "Ciseaux"

def compare(Joueur, Ordi):
    '''
    Compare les choix du joueur et de l'ordinateur pour déterminer le gagnant.
    Arguments :
        Joueur (str) : Le choix du joueur.
        Ordi (str) : Le choix de l'ordinateur.
    Retourne :
        str : "Ordi" si l'ordinateur gagne, "Joueur" si le joueur gagne, ou "Egalite" en cas d'égalité.
    '''
    if (Joueur == "Pierre" and Ordi == "Papier") or (Joueur == "Ciseaux" and Ordi == "Pierre") or (Joueur == "Papier" and Ordi == "Ciseaux"):
        return "Ordi"  # L'ordinateur gagne
    elif Joueur == Ordi:
        return "Egalite"  # Cas d'égalité
    else:
        return "Joueur"  # Le joueur gagne

def rejouer():
    '''
    Demande au joueur s'il souhaite rejouer.
    Retourne :
        str : "oui" si le joueur veut rejouer, "non" sinon.
    '''
    choix = 0
    while choix not in [1, 2]:  # Vérifie que le choix est valide
        try:
            choix = int(input("Tu veux rejouer ? 1 pour Oui, 2 pour Non. "))
        except ValueError:
            choix = 0  # Réinitialise le choix en cas d'entrée invalide
        if choix == 1:
            return "oui"
        if choix == 2:
            return "non"

def jeu():
    '''
    Gère le déroulement complet du jeu.
    Permet au joueur de jouer plusieurs parties et affiche les résultats après chaque manche.
    '''
    restart = "oui"
    while restart == "oui":  # Boucle principale pour rejouer
        choix_joueur = choix_Joueur()  # Récupère le choix du joueur
        choix_ordi = choix_Ordi()  # Récupère le choix de l'ordinateur
        if compare(choix_joueur, choix_ordi) == "Joueur":
            for i in range(3, 0, -1):  # Compte à rebours avant d'afficher le résultat
                print(i)
                time.sleep(1)
            print(f"L'ordinateur a choisi {choix_ordi} !\nTu as gagné !")
            restart = rejouer()
        elif compare(choix_joueur, choix_ordi) == "Egalite":
            for i in range(3, 0, -1):  # Compte à rebours avant d'afficher le résultat
                print(i)
                time.sleep(1)
            print(f"L'ordinateur a choisi {choix_ordi} !\nVous êtes tout les deux à égalité !")
            restart = rejouer()
        else:
            for i in range(3, 0, -1):  # Compte à rebours avant d'afficher le résultat
                print(i)
                time.sleep(1)
            print(f"L'ordinateur a choisi {choix_ordi} !\nTu as perdu...")
            restart = rejouer()

jeu()