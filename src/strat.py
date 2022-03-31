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
def tetu(o1): 
    return o1

def meilleure_reponse(goalStates,nbPlayers,score_elec,score_A,score_B):
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
    if nb_joueurs>0:
        o1.append(goalStates[-1])
        
    return o1
def nb_pas_max(n):
    return n

def pos_moyenne_militant(goalStates,nbPlayers,tab_proba,A=True):
        #Si A = true ça veux dire qu'on applique fictitous sur lui sinon sur B
        trat_moyenne = [(0,0)] * len(goalStates)
        for i in range(0,nbPlayers,2):
            p = random.randint(0,100)/100
            cpt = 0
            j=0
            while j<len(tab_proba) :
                cpt += tab_proba[j]
                if cpt  < tab_proba[j] :
                    break 
                j+=1
            if A :
                trat_moyenne[j][1]+=1
            else :
                trat_moyenne[j][0]+=1
        if A :
            return meilleure_reponse(goalStates,nbPlayers,trat_moyenne,0,1)
        else :
            return meilleure_reponse(goalStates,nbPlayers,trat_moyenne,1,0)

def fictitous_play(goalStates,nbPlayers,liste_strat):
    
    strat, nb_occurence = np.unique(liste_strat,return_counts=True)
    print(strat)
    if(sum(nb_occurence)==0):
        return alea(goalStates,nbPlayers)
    gain_max = 0
    meilleurs_strat = [(0,0)] * len(goalStates)
    score_elec = [(0,0)] * len(goalStates)
    for i in range(len(strat)):
        for j in range(len(goalStates)):
            score_elec = (strat[i][j],0)
        meilleurs_strat_i = meilleure_reponse(goalStates, nbPlayers, score_elec , score_A = 1, score_B = 0)
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
        meilleurs_strat_i = meilleure_reponse(goalStates, nbPlayers, score_elec , score_A = 1, score_B = 0)
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
def stochastique_expert(goalstate,strategy,proba_stock):
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
            return o1
    return

