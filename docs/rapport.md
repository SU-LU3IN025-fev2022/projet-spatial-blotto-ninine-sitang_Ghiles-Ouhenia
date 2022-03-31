# Rapport de projet

## Groupe 4
* Ninine SITANG 3801541
* Ghiles OUHENIA 28716807

## Description des choix importants d'implémentation
Stratégie aléatoire : Pour chaque militant on choisi aléatoirement une position d'un électeur et on l'ajoute dans une liste d'objectifs et on l'a renvoie

Stratégie têtue : cette fonction prend en paramètre un jour et si jour est différent de 0 on renvoie le même objectif que le jour précedent, sinon on appel la fonction alea pour renvoyer un objectif aléatoire.

Stratégie meilleure réponse: on compare le score du partie A et B, le perdant se sert de la stratégie du gagnant en ajoutant  +1 miliant pour chaque électeur jusqu'à ce qu'il n'y ait plus de militants, avec cette implémentation, on est sur, si il utilise la même stratégie de gagné le jours suivant. 

Stratégie fictitous_play: on utilise une liste qui contiens les stratégie de l'autre joueur(passé en parametre), puis on compte le nombre d'occurence de chaque statégie, et on parcours chaque stratégie, pour chaqu'une s'entre elle, on appel meilleure_réponse, ensuite en simule une partie avec chaqu'une des statégies qu'il a déja joué et on calcule son gain, si il gagne le gain reçois le nombre d'occurence de la strat sinon il reçois son inverse (-occ).
une fois finit on choisis la meilleur_reponse avec le gain max qu'on renvoie. (on aurai pu aussi stocké les gains dans une liste et les mettre sous forme de probabilité puis choisir l'une d'entre elles) 

Stratégie stochastique_expert: cette fonction prend en paramètre un goalstate, une liste de stratégies, et une liste de probabilités associées à chaque stratégies. Au départ on choisit aléatoirement une probabilité p entre 0 et 1 (et on le multiplie * la somme de la liste des probablités (pour évité de mettre à jours les autes proba
)) puis, on parcours le tableau de probabilités des stratégie jusqu'à trouver l'interval où il appartient et on retourne cette stratégie, et a chaque entré dans la fonction, on met à jour la liste des probabilité.(si la stratégie qu'on a jouez précédement est gagnante, on multiplie ça proba*1.3, sinon on la multiplie * 0.7)
## Description des résultats
## Fictitous vs Têtu:
![fictitous_vs_tétue](https://user-images.githubusercontent.com/100412562/161160565-2e0e94b3-87e5-4c06-8abc-8dd2174bfdd8.png)

Sur 50 campagnes, on remarque que fictitous remporte la totalité de la campagne.
En effet on a d'une part Têtue qui emploie la même stratégie durant toute la campage. Tandis que Fictitous étant donné qu'il connait déjà la stratégie qui sera jouée par son adversaire et qu'il suit une stratégie de meilleures réponses, alors il va toujours battre son adversaire.

## Fictitous vs Alea: 
![fictitous_vs_aléa](https://user-images.githubusercontent.com/100412562/161161196-38b08ec7-c37f-44fd-80fc-839733187ab5.png)

Sur 50 campagnes, on remarque qu'il y a une majorité de parties nulles.
En effet, la stratégie fictitous play enregistre les stratégies utilisées par son adversaires et effectue des prédictions en créant un tableau de probabilité avec les meilleurs réponses. Cependant, la stratégie Aléa renvoie toujours de nouvelles données qui ne suivent pas forcéments les prédictions, voir même meilleures que celles prédites par fictitous. Donc les prédictions de fictitous play ne sont pas vraiment utiles.

## Fictitous vs stochastique:
![Fictitous vs stochastique](https://user-images.githubusercontent.com/100412562/161161319-35ad296f-5815-4bc3-aeff-059e84e42c55.png)


Sur 50 campagnes, on remarque que fictitous a 18 victoires, et 32 null.
La stratégie stochastique attribut des probabilités à chacune des stratégies qu'on lui associe ,et il met à jour cette probabilité selon le résultat du jour j-1. Fictitous quant à lui suit et enregistre les stratégies qu'utilise l'autre partie, et avec ces données, il pseudo-créé une table de probabitée avec les meilleurs réponse, et vue que stochastick posséde seulement 4 stratégies, fictitous vas rapidement créé une optimal de façon a ne pas perdre, ce qui explique le faite que fictitous n'a pas perdu.

## Têtue vs Meilleure réponse : 
![tétue_vs_meilleureReponse](https://user-images.githubusercontent.com/100412562/161155900-570d52d2-032a-45f0-8aa7-30cabeab4e3e.png) 

Sur 50 campagnes, la totalité a été remportée par la stratégie meilleure réponse. 
Le jour 0, les deux deux parties choisissent aléatoirement leur stratégie, donc ils possédes tous les deux 50% de chance de gagner. Ce n'est qu'à partir du deuxième jour, que la stratégie meilleure réponse va battre son adversaire, car elle posséde déja la stratégie de l'autre camps, ce qui est en accord avec l'histogramme ci dessus.

## Têtue vs Stochastique:
![tétue_vs_stochastique](https://user-images.githubusercontent.com/100412562/161155892-b40374e3-5fbe-495b-afdf-7e557f3fb5d9.png)

Sur 50 campagnes, on observe que Têtue a 45 parties perdues, et 5 gagné. 
Têtue utilise la même stratégie tout au long de la campagne. Tandis que Stochastique possède 4 stratégies et change ses probabilités de manière à choisir la stratégie qui bat celle de Têtue, les seuls cas où tétue peut gagné est sois on a pas assez de jours, sois elle bat toute les stratégie de stochastique.
