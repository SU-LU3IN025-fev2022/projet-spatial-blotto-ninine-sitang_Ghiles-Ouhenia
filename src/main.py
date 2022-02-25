# -*- coding: utf-8 -*-

# Nicolas, 2021-03-05
from __future__ import absolute_import, print_function, unicode_literals

import random 
import numpy as np
import sys
from itertools import chain


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
    iterations = 100 # default
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
    
    
    
        
    #-------------------------------
    # Attributaion aleatoire des fioles 
    #-------------------------------
    for m in range(0,nbPlayers,2):
        objectifs1 = goalStates
        objectifs2 = goalStates
        
        random.shuffle(objectifs1)
        random.shuffle(objectifs2)
        a = random.randint(0,len(goalStates)-1)
        b = random.randint(0,len(goalStates)-1)
        print("Objectif joueur "+ str(m) + " :" ,objectifs1[a])
        print("Objectif joueur "+ str(m+1) + " :" ,objectifs2[b])

        
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
        print ("Chemin trouvé:", path1)
        p2 = ProblemeGrid2D(initStates[m+1],objectifs2[b],g,'manhattan')
        path2 = probleme.astar(p2)
        print ("Chemin trouvé:", path2)
            
        
        #-------------------------------
        # Boucle principale de déplacements 
        #-------------------------------
        
                
        posPlayers = initStates
        row1,col1 = path1[0]
        row2,col2 = path2[0]
        for i in range(iterations):
            
            # on fait bouger chaque joueur séquentiellement
            
            # Joeur 0: suit son chemin trouve avec A* 
            if (row1,col1) != objectifs1[a]:
                row1,col1 = path1[i]
                posPlayers[m]=(row1,col1)
                players[m].set_rowcol(row1,col1)
                print ("pos "+str(m)+":", row1,col1)
                if (row1,col1) == objectifs1[a]:
                    print("le joueur "+str(m)+" a atteint son but!")
            
            
            # Joueur 1: fait A*
            if (row2,col2) != objectifs2[b]:
                row2,col2 = path2[i]
                posPlayers[m+1]=(row2,col2)
                players[m+1].set_rowcol(row2,col2)
                print ("pos "+str(m+1)+":", row2,col2)
                if (row2,col2) == objectifs2[b]:
                    print("le joueur "+str(m+1)+" a atteint son but!")
            if (row1,col1) == objectifs1[a] and (row2,col2) == objectifs2[b]:
                break

            """while True: # tant que pas legal on retire une position
                x_inc,y_inc = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
                next_row = row+x_inc
                next_col = col+y_inc
                if legal_position(next_row,next_col):
                    break
            players[1].set_rowcol(next_row,next_col)
            print ("pos 1:", next_row,next_col)
        
            col=next_col
            row=next_row
            posPlayers[1]=(row,col)
                
            if (row,col) == objectifs[1]:
                print("le joueur 1 a atteint son but!")
                break"""
                
                
            
            # on passe a l'iteration suivante du jeu
            game.mainiteration()

                
        
            
    
    pygame.quit()
    
    
    
    
    #-------------------------------
    
        
        
    
    
        
    
   

if __name__ == '__main__':
    main()
    


