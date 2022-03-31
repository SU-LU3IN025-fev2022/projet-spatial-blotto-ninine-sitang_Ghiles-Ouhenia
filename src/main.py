# -*- coding: utf-8 -*-

# Nicolas, 2021-03-05
from __future__ import absolute_import, print_function, unicode_literals

import random
from tracemalloc import start 
import numpy as np
import sys
from itertools import chain

import strat 
import pygame

from pySpriteWorld.gameclass import Game,check_init_game_done
from pySpriteWorld.spritebuilder import SpriteBuilder
from pySpriteWorld.players import Player
from pySpriteWorld.sprite import MovingSprite
from pySpriteWorld.ontology import Ontology
import pySpriteWorld.glo

from search.grid2D import ProblemeGrid2D
from search import probleme




# ---- ---- ---- ---- ---- ----
# ---- Misc                ----
# ---- ---- ---- ---- ---- ----




# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----

game = Game()

def init(_boardname=None):
    global player,game
    name = _boardname if _boardname is not None else 'blottoMap'
    game = Game('./Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5  # frames per second
    game.mainiteration()
    player = game.player
    
def main():

    #for arg in sys.argv:
    iterations = 100# default
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])
    print ("Iterations: ")
    print (iterations)

    init()
    

    
    #-------------------------------
    # Initialisation
    #-------------------------------
    
    nbLignes = game.spriteBuilder.rowsize
    nbCols = game.spriteBuilder.colsize
       
    print("lignes", nbLignes)
    print("colonnes", nbCols)
    
    
    players = [o for o in game.layers['joueur']]
    nbPlayers = len(players)
    print("Trouvé ", nbPlayers, " militants")
    
       
           
    # on localise tous les états initiaux (loc du joueur)
    # positions initiales des joueurs
    initStates = [o.get_rowcol() for o in players]
    print ("Init states:", initStates)
    
    # on localise tous les secteurs d'interet (les votants)
    # sur le layer ramassable
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    print ("Goal states:", goalStates)
    
        
    # on localise tous les murs
    # sur le layer obstacle
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    print ("Wall states:", wallStates)
    
    def legal_position(row,col):
        # une position legale est dans la carte et pas sur un mur
        return ((row,col) not in wallStates) and row>=0 and row<nbLignes and col>=0 and col<nbCols
    
    
    NB_JOURS=3 #nombre de jours que dure la campagne 
    score_A=0 
    score_B=0
    #-------------------------------
    # Attributaion aleatoire des fioles 
    #-------------------------------
    pas_max = 100
    
    iterations = strat.nb_pas_max(pas_max)
    proba_fictitous_A = [0] * len(goalStates)
    proba_fictitous_B = [0] * len(goalStates)
    liste_strat_A = []
    liste_strat_B = []
    for j in range(NB_JOURS):
        #FAIRE L'INITIALISATION DES TABLEAU DE PROBA
        """if j == 0 :
            objectifs1= strat.alea(goalStates,nbPlayers)
            objectifs2= strat.alea(goalStates,nbPlayers)
        if j>0:
            if score_A > score_B:
                objectifs1 = strat.tetu(objectifs1) # A garde la meme trategie vue qu'il a gagnié
                objectifs2 = strat.perdant(goalStates,nbPlayers,score_elec,score_A,score_B)
            if score_A < score_B:
                objectifs1 = strat.perdant(goalStates,nbPlayers,score_elec,score_A,score_B) # B garde la meme trategie vue qu'il a gagnié
                objectifs2 = strat.tetu(objectifs2)
            if score_A == score_B:
                objectifs1= strat.alea(goalStates,nbPlayers)
                objectifs2= strat.alea(goalStates,nbPlayers)
        #objectifs1= strat_tetu(goalStates,nbPlayers,o1)"""
        
        score_elec=[(0,0)] * len(goalStates)
        a=0
        objectifs1= strat.fictitous_play(goalStates,nbPlayers,liste_strat_B)
        objectifs2= strat.alea(goalStates,nbPlayers)
        
        for m in range(0,nbPlayers,2):
            #-----------------------
            #On definit les objectifs celon la strategie
            #-----------------------
            
            
            

            
            #-------------------------------
            # Carte demo 
            # 2 joueurs 
            # Joueur 0: A*
            # Joueur 1: random walk
            #-------------------------------
            
            #-------------------------------
            # calcul A* pour le joueur 0
            #-------------------------------
            

            
            g =np.ones((nbLignes,nbCols),dtype=bool)  # par defaut la matrice comprend des True  
            for w in wallStates:            # putting False for walls
                g[w]=False
            p1 = ProblemeGrid2D(initStates[m],objectifs1[a],g,'manhattan')
            path1 = probleme.astar(p1)
            #print ("Chemin trouvé:", path1)
            p2 = ProblemeGrid2D(initStates[m+1],objectifs2[a],g,'manhattan')
            path2 = probleme.astar(p2)
            #print ("Chemin trouvé:", path2)
                
            
            #-------------------------------
            # Boucle principale de déplacements 
            #-------------------------------
            
                    
            posPlayers = initStates
            row1,col1 = path1[0]
            row2,col2 = path2[0]
            for i in range(iterations):
                
                # on fait bouger chaque joueur séquentiellement
                
                # Joeur 0: suit son chemin trouve avec A*
                if ((row1,col1) == objectifs1[a]) and (i==0):#si le militant est deja dans son objectif, alors pas de déplacement à faire
                    
                    elec = goalStates.index((row1,col1))
                    x,y = score_elec[elec]
                    x += 1
                    score_elec[elec]= (x,y)
                if (row1,col1) != objectifs1[a]:
                    row1,col1 = path1[i]
                    posPlayers[m]=(row1,col1)
                    players[m].set_rowcol(row1,col1)

                    #print ("pos "+str(m)+":", row1,col1)
                    if (row1,col1) == objectifs1[a]:
                        #print("le joueur "+str(m)+" a atteint son but!")
                        elec = goalStates.index((row1,col1))
                        x,y = score_elec[elec]
                        x += 1
                        score_elec[elec]= (x,y)
                        
                
                
                # Joueur 1: fait A*
                if ((row2,col2) == objectifs2[a]) and (i==0):#si le militant est deja dans son objectif, alors pas de déplacement à faire
                    
                    elec = goalStates.index((row2,col2))
                    x,y = score_elec[elec]
                    y += 1
                    score_elec[elec]= (x,y)
                if (row2,col2) != objectifs2[a]:
                    row2,col2 = path2[i]
                    posPlayers[m+1]=(row2,col2)
                    players[m+1].set_rowcol(row2,col2)
                    #print ("pos "+str(m+1)+":", row2,col2)
                    if (row2,col2) == objectifs2[a]:
                        #print("le joueur "+str(m+1)+" a atteint son but!")
                        elec = goalStates.index((row2,col2))
                        x,y = score_elec[elec]
                        y += 1
                        score_elec[elec]= (x,y)
                if (row1,col1) == objectifs1[a] and (row2,col2) == objectifs2[a]:
                    break
                    
                    
                
                # on passe a l'iteration suivante du jeu
                #game.mainiteration()
            a+=1
        print("----------------------------",score_elec)
        for v in range(len(score_elec)):
            x,y = score_elec[v]        
            if x>y:
                score_A +=1
            elif y>x:
                score_B +=1

        print("score de A :", score_A)      
        print("score de B :", score_B)
        strat_A=[0] * len(goalStates)
        strat_B=[0] * len(goalStates)
        for m in range(len(goalStates)):
            strat_A[m],strat_B[m] =  score_elec[m]
        
        liste_strat_A.append(strat_A)
        liste_strat_B.append(strat_B)
        print(liste_strat_B)  
        
            
    
    pygame.quit()
    
    
    
    
    #-------------------------------
    
        
        
    
    
        
    
   

if __name__ == '__main__':
    main()
    


