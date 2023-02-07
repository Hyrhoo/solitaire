# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:12:58 2022

@author: jojoj
"""

from random import shuffle, choice
import pygame
pygame.init()
reso = (1000,700)
vert = (0,157,0)
fenetre_de_jeu = pygame.display.set_mode(reso)
clock = pygame.time.Clock()

num_carte = [1,2,3,4,5,6,7,8,9,10,11,12,13]
couleur = ["pi","co","ca","tr"]

couleur_carte = {"pi":"noir",
                 "tr":"noir",
                 "co":"rouge",
                 "ca":"rouge"}

defauce = []
pioche = [[i,y, 0] for i in num_carte for y in couleur]
        
shuffle(pioche)
piles = [[],[],[],[]]
tab_jeu = [[],[],[],[],[],[],[]]
for i in range(7):
    for y in range(i+1):
        cart = choice(pioche)
        pioche.remove(cart)
        if y == i:
            cart[-1] = 1
        tab_jeu[i].append(cart)

def affichage():
    """
    The affichage function is used to display the game on the screen.
    It displays all of the cards in their respective piles, and also displays them in order from left to right.
    The function also shows which card is selected by highlighting it with a yellow rectangle.
    
    :return: The display of the game
    :doc-author: Trelent
    """
    fenetre_de_jeu.fill(vert)
    for x in range(len(tab_jeu)):
        image = None
        for y,carte in enumerate(tab_jeu[x]):
            if carte[-1] == 1:
                zone_chercher = "cartes/"+str(carte[0])+carte[1]+".gif"
            elif carte[-1] == 0:
                zone_chercher = "cartes/back.gif"
            image = pygame.image.load(zone_chercher).convert()
            image_load = pygame.transform.scale(image,(71,96))
            fenetre_de_jeu.blit(image_load,(10+75*x,131+20*y))
        if not image:
            image = pygame.image.load("cartes/case_vide.gif").convert()
            image_load = pygame.transform.scale(image,(71,96))
            fenetre_de_jeu.blit(image_load,(10+75*x,131))
    
    image = None
    for x,i in enumerate(defauce):
        if i[-1] == 1:
            zone_chercher = "cartes/"+str(i[0])+i[1]+".gif"
        elif i[-1] == 0:
            zone_chercher = "cartes/back.gif"
        image = pygame.image.load(zone_chercher).convert()
        image_load = pygame.transform.scale(image,(71,96))
        fenetre_de_jeu.blit(image_load,(700+3*x,10))
    if not image:
        image = pygame.image.load("cartes/case_vide.gif").convert()
        image_load = pygame.transform.scale(image,(71,96))
        fenetre_de_jeu.blit(image_load,(700,10))
    
    image = None
    for x,i in enumerate(pioche):
        if i[-1] == 1:
            zone_chercher = "cartes/"+str(i[0])+i[1]+".gif"
        elif i[-1] == 0:
            zone_chercher = "cartes/back.gif"
        image = pygame.image.load(zone_chercher).convert()
        image_load = pygame.transform.scale(image,(71,96))
        fenetre_de_jeu.blit(image_load,(850+3*x,10))
    if not image:
        image = pygame.image.load("cartes/case_vide.gif").convert()
        image_load = pygame.transform.scale(image,(71,96))
        fenetre_de_jeu.blit(image_load,(850,10))
    
    for x in range(len(piles)):
        image = None
        for i,carte in enumerate(piles[x]):
            if carte[-1] == 1:
                zone_chercher = "cartes/"+str(carte[0])+carte[1]+".gif"
            #elif z[-1] == 0:
            #    zone_chercher = "cartes/back.gif"
            image = pygame.image.load(zone_chercher).convert()
            image_load = pygame.transform.scale(image,(71,96))
            fenetre_de_jeu.blit(image_load,(10+75*x,10+2*i))
        if not image:
            image = pygame.image.load("cartes/case_vide.gif").convert()
            image_load = pygame.transform.scale(image,(71,96))
            fenetre_de_jeu.blit(image_load,(10+75*x,10))
    
    pygame.display.flip()

def verif_pile_vide():
    """
    The verif_pile_vide function verifies if the pile is empty.
        Args:
            None
    
        Returns:
            bool : True if the pile is empty, False otherwise.
    
        
    
    :return: True if the pile is empty, and false otherwise
    :doc-author: Trelent
    """
    for i in range(4):
        if len(piles[i]) == 0: return i
    return None

def verif_pile(carte):
    """
    The verif_pile function checks if the card can be placed on top of a pile.
    It checks if the pile is empty or not, and then compares the value of both cards to see if they are equal.
    If they are equal, it will check for a 1 higher value in order to place it on top.
    
    :param carte: Check if the card is a valid move
    :return: True if the card is a valid move, false otherwise
    :doc-author: Trelent
    """
    for i in range(len(piles)):
        if len(piles[i]) >= 1:
            if carte[1] == piles[i][-1][1]:
                if carte[0]-1 == piles[i][-1][0]:
                    return i
    return None

def verif_colonne(carte):
    """
    The verif_colonne function checks if the card played is valid.
    It checks if the column is empty or not and also checks for the color of 
    the card played and compares it to the last one in that column. If all these 
    conditions are met, then it returns True.
    
    :param carte: Store the card that is being played
    :return: The number of the column where the card can be placed
    :doc-author: Trelent
    """
    for i in range(len(tab_jeu)):
        if len(tab_jeu[i]) == 0:
            if carte[0] == 13:
                return i
        elif couleur_carte[carte[1]] != couleur_carte[tab_jeu[i][-1][1]]:
            if carte[0]+1 == tab_jeu[i][-1][0]:
                return i
    return None

def decider_coup(coup, carte, pioche, defauce):
    """
    The decider_coup function takes in a coup, carte, pioche and defauce.
    It then decides what to do with the card depending on the coup.
    If it is a pio_coup then it will take the card from pioche and put it into defauce.
    If there is no carte
    
    :param coup: Determine which action the player will do
    :param carte: Store the card that will be played
    :param pioche: Store the cards that are drawn from the deck
    :param defauce: Store the last card played
    :return: The result of the coup
    :doc-author: Trelent
    """
    if coup == "pio":
        pioche, defauce = piocher(pioche, defauce, carte)
    
    elif carte:
        if coup == "def":
            endroi, niv = verif_coup_possible(carte)
            if endroi:
                les_diff_tab[endroi][niv].append(carte)
                defauce.pop(-1)
        
        elif coup[0] == "pil":
            print(carte)
            niv = verif_colonne(carte)
            if niv is not None:
                tab_jeu[niv].append(carte)
                piles[coup[1]].pop(-1)
        
        else:
            endroi, niv = verif_coup_possible(carte)
            if endroi:
                if carte == tab_jeu[coup[0]][-1]:
                    les_diff_tab[endroi][niv].append(carte)
                    tab_jeu[coup[0]].pop(-1)
                
                else:
                    les_cartes = [carte]
                    if endroi != 2:
                        niv = verif_colonne(carte)
                        if niv is not None:
                            endroi = 2
                    if endroi == 2:
                        for y,i in enumerate(tab_jeu[coup[0]]):
                            if y > coup[1]:
                                les_cartes.append(tab_jeu[coup[0]][y])
                        for i in les_cartes:
                            les_diff_tab[endroi][niv].append(i)
                            tab_jeu[coup[0]].pop(-1)
    
    return pioche, defauce

def verif_coup_possible(carte):
    """
    The verif_coup_possible function checks if the move is possible.
    It returns a tuple with the type of move and its coordinates.
    
    :param carte: Check if the card is a 1 or not
    :return: A tuple of two elements
    :doc-author: Trelent
    """
    print(carte)
    if carte[0] == 1:
        return 1, verif_pile_vide()
    pile = verif_pile(carte)
    if pile != None:
        return 1, pile
    colonne = verif_colonne(carte)
    if colonne != None:
        return 2, colonne
    return None, None

def piocher(pioche, defauce, carte):
    """
    The piocher function takes a list of cards and returns the card at the end of the list. If there are no more cards in 
    the deck, it shuffles all used cards and puts them back into a new deck. It also removes any used card from its old position
    and places it at the end of that same
    
    :param pioche: Store the cards that are not used
    :param defauce: Store the cards that have been played
    :param carte: Store the card that is drawn
    :return: The last card of the defauce pile
    :doc-author: Trelent
    """
    if carte:
        carte[-1] = 1
        defauce.append(carte)
        pioche.pop(-1)
    else:
        shuffle(defauce)
        pioche = defauce.copy()
        defauce = defauce.clear()
        defauce = []
        for i in range(len(pioche)):
            pioche[i][-1] = 0
    return pioche, defauce

def retourner_carte():
    """
    The retourner_carte function takes a list of lists as an argument and returns the first card in each sublist.
    The function assumes that all sublists are of equal length.
    
    :return: The first card from the deck
    :doc-author: Trelent
    """
    for i in range(len(tab_jeu)):
        if len(tab_jeu[i]) > 0:
            tab_jeu[i][-1][-1] = 1

les_diff_tab = {1: piles,
                2: tab_jeu,
                3: pioche,
                4: defauce}

affichage()
partie = True
while partie:
    gagner = False
    if pygame.event.get(pygame.QUIT):
        partie = False
    for event in pygame.event.get(pygame.MOUSEBUTTONUP):
        #if event.type == pygame.QUIT:
        #    partie = False
        if event.type == pygame.MOUSEBUTTONUP:
            coup = None
            if event.pos[0] in range(535) and event.pos[1] in range(131, 500):
                coup = ((event.pos[0]-10) // 75, (event.pos[1]-131) // 20)
                if len(tab_jeu[coup[0]]) >= 1:
                    try: carte = tab_jeu[coup[0]][coup[1]]
                    except IndexError: carte, coup = tab_jeu[coup[0]][-1], (coup[0], -1)
                    if carte[-1] == 0: carte, coup = None, None
                else: carte, coup = None, None
            elif event.pos[0] in range(310) and event.pos[1] in range(10, 106):
                coup = ("pil", (event.pos[0]-10) // 75)
                if len(piles[coup[1]]) == 0:
                    carte = None
                else:
                    carte = piles[coup[1]][-1]
            elif event.pos[0] in range(700,843) and event.pos[1] in range(10,106):
                if len(defauce) == 0:
                    coup, carte = "def", None
                else:
                    coup, carte = "def", defauce[-1]
            elif event.pos[0] in range(850,993) and event.pos[1] in range(10,106):
                if len(pioche) == 0:
                    coup, carte = "pio", None
                else:
                    coup, carte = "pio", pioche[-1]
            if coup: 
                pioche, defauce = decider_coup(coup, carte, pioche, defauce)
                retourner_carte()
                affichage()
                gagner = True
                for i in piles:
                    if len(i) != 13:
                        gagner = False
    if gagner:
        print("vous avez gagner")
        while partie:
            for event in pygame.event.get(pygame.QUIT):
                if event.type == pygame.QUIT:
                    partie = False
            clock.tick(25)
    clock.tick(60)

pygame.quit()