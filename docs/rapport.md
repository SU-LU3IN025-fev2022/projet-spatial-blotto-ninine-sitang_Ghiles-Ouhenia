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
