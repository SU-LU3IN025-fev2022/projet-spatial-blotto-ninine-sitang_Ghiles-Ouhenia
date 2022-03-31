# Rapport de projet

## Groupe 4
* Ninine SITANG 3801541
* Ghiles Ouhenia 28716807

## Description des choix importants d'implémentation
Stratégie aléatoire : Pour chaque militant on choisi aléatoirement une position d'un électeur et on l'ajoute dans une liste d'objectifs et on l'a renvoie

Stratégie têtue : cette fonction prend en paramètre un jour et si jour est différent de 0 on renvoie le même objectif sinon on appel la fonction alea pour renvoyer un objectif aléatoire

Stratégie meilleure réponse: on compare le score du partie A et B, le perdant se sert de la stratégie du gagnant en ajoutant  +1 miliant pour chaque électeur jusqu'à ce qu'il n'y ait plus de militants

Stratégie fictitous_play:

Stratégie stochastique_expert: cette fonction prend en paramètre un goalstate, une liste de stratégies, et une liste de probabilités associées à chaque stratégies. Au départ on choisit aléatoirement une probabilité p entre 0 et 1 puis, on parcours le tableau de probabilités jusqu'à trouver l'interval où il appartient et on retourne cette stratégie.
## Description des résultats
    ## Fictitous vs Têtue:
    Sur 50 campagnes, on remarque que fictitous remporte la totalité de la campagne.
    En effet on a d'une part Têtue qui emploie la même stratégie durant toute la campage. Tandis que Fictitous étant donnée qu'il connait déjà la stratégie qui sera jouée par son adversaire et qu'il suit une stratégie de meilleures réponses, alors il va toujours battre son adversaire.
    ## Fictitous vs Alea: 
    Sur 50 campagnes, on remarque qu'il y a une majorité de parties nulles.
    En effet, la stratégie fictitous play enregistre les stratégies utilisées par son adversaires et effectue des prédictions en créant un tableau de probabilité avec les meilleurs réponses. Cependant, la stratégie Aléa renvoie toujours de nouvelles données qui ne suivent pas forcéments les prédictions, voir même meilleures que celles prédites par fictitous. Donc les prédictions de fictitous play ne sont pas vraiment utiles.
    
    ## Fictitous vs stochastique:
    Sur 50 campagnes, on remarque que fictitous a 18 victoires, et 32 null.
    La stratégie stochastique attribut des probabilités à chacune des stratégies qu'on lui associe ,et il met à jour cette probabilité selon le résultat du jour j-1. Fictitous quant à lui suit et enregistre les stratégies qu'utilise l'autre partie, et avec ces données, il pseudo-créé une table de probabitée avec les meilleurs réponse, et vue que stochastick posséde seulement 4 stratégies, fictitous vas rapidement créé une optimal de façon a ne pas perdre, ce qui explique le faite que fictitous n'a pas perdu.
    
    ## Meilleure réponse vs Têtue: 
    Sur 50 campagnes, la totalité a été remportée par la stratégie meilleure réponse. 
    Le jour 0, les deux deux parties choisissent aléatoirement leur stratégie, donc ils possédes tous les deux 50% de chance de gagner. Ce n'est qu'à partir du deuxième jour, que la stratégie meilleure réponse va battre son adversaire, car elle posséde déja la stratégie de l'autre camps, ce qui est en accord avec l'histogramme ci dessus.
    
    ## Têtue vs Stochastique:
    Sur 50 campagnes, on observe que Têtue a 45 parties perdues, et 5 nulles. 
