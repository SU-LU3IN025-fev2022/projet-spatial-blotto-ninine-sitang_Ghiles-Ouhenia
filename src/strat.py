from itertools import count
import random 
import numpy as np
import sys


def alea(goalStates,nbPlayers):

        o1 = goalStates
        
        random.shuffle(o1)
        objectifs1=[]
        for i in range(0,nbPlayers,2):
            objectifs1.append(o1[random.randint(0,len(goalStates)-1)])

        return objectifs1
def tetu(goalStates,nbPlayers,o1,jour): 
    if jour==0:
        return alea(goalStates,nbPlayers)
    return o1

def meilleure_reponse(goalStates,nbPlayers,score_elec,score_A,score_B,jour):
    if jour==0:
        return alea(goalStates,nbPlayers)
    nb_joueurs = nbPlayers // 2
    o1=[]
    
    for c in range(len(score_elec)):
        if score_A > score_B:
            x,y = score_elec[c]
        else :
            y,x = score_elec[c]
        if nb_joueurs > x:
            
            y=x+1
            nb_joueurs -= y
            for i in range(y):
                o1.append(goalStates[c])
        else:
            if x==y :
                if x>1:
                    y=0
                else :
                    y=x
                    nb_joueurs -= y
                    for i in range(y):
                        o1.append(goalStates[c])
            else :
                y=0
    while nb_joueurs>0:
        o1.append(goalStates[-1])
        nb_joueurs-=1
        
    return o1
def nb_pas_max(n):
    return n


def unique(liste_strat):
    strat = []
    occ = []
    for i in liste_strat :
        if i in strat :
            occ[strat.index(i)]+=1
        else :
            strat.append(i)
            occ.append(1)
    return strat,occ
def fictitous_play(goalStates,nbPlayers,liste_strat,jour):
    if(jour==0):
        return alea(goalStates,nbPlayers)
    strat , nb_occurence = unique(liste_strat)
    
    gain_max = 0
    score_elec = [(0,0)] * len(goalStates)
    for i in range(len(strat)):
        for j in range(len(goalStates)):
            score_elec[j] = (strat[i][j],0)
        meilleurs_strat_i = meilleure_reponse(goalStates, nbPlayers, score_elec , score_A = 1, score_B = 0 ,jour = 5)
        if i==0 :
            meilleurs_strat = meilleurs_strat_i
        for j in range(len(goalStates)):
            elec = goalStates.index(meilleurs_strat_i[j])
            x,y = score_elec[elec]
            y += 1
            score_elec[elec]= (x,y)
        gain_i = 0
        for k in range(len(strat)):
            score_A = 0
            score_B = 0
            for j in range(len(goalStates)):
                x,y = score_elec[j]
                score_elec[j] = (strat[k][j],y)
            for v in range(len(score_elec)):
                x,y = score_elec[v]        
                if x>y:
                    score_A +=1
                elif y>x:
                    score_B +=1

            if score_A > score_B :
                gain_i -= nb_occurence[k] #on pourrait aussi devisé pour avoir une proba (ça ne changera pas le résultat final )
            elif score_A < score_B : #cas où meilleure réponse bat la stat_k
                gain_i += nb_occurence[k]
        if gain_i > gain_max:
            gain_max = gain_i
            meilleurs_strat = meilleurs_strat_i
    
    return meilleurs_strat
def stochastique_expert(goalstate,strategy,proba_stock,score_A_j,score_B_j,objectif,jour):
    if jour !=0 :    
        tmp = [0]*len(goalstate)
        for t in range(len(objectif)):
            tmp[goalstate.index(objectif[t])]+=1
        if score_A_j > score_B_j:
            if tmp in strategy:
                strat_index= strategy.index(tmp)
                proba_stock[strat_index] *= 1.3
        if score_A_j < score_B_j:
            if tmp in strategy:
                strat_index= strategy.index(tmp)
                proba_stock[strat_index] *= 0.7
    p=np.random.randint(0,100)/100
    p=p*sum(proba_stock) # car même si la somme des probabilités n'est pas égal à 1 on revient à la même chose en fesant p*sum(proba_stock)
    cpt = 0
    o1=[]
    for i in range(len(proba_stock)):
        cpt  += proba_stock[i]
        if p < cpt:
            for e in range(len(strategy[i])):
                for m in range(strategy[i][e]):
                    o1.append(goalstate[e])
            return o1,proba_stock
    return
