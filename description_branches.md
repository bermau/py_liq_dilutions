# Description of branches

## 23_01_forcer_premieres_dilutions
On transmettra une liste de listes de type [[dil1, vol1], [dil2, vol2]]

L'erreur d'évolution des CT dans le cas de dilution de CT est due au fait que le tube_en_cours_de_dil n'est pas mis à jour. (vers 124)

Fixed : Evolution des CT correcte. 
   Reste à créer la dernière dilution.

23_01_forcer_premieres_dilutions : je merge sur main (même si l'objectif est incomplet).

## 23_01_forcer_premieres_dilutions_suite
La fonction dilution est capable de gérer des dilutions imposées. Tout au moins pur les tubes exprimés en CT.

## 23_01_ameliorer_signature
  * Améliorer la signature des différentes classes et fonctions (Il suffit en fait d'imposer un argument nommé dès le premier argument.
    ). 
  * protection contre les dilutions imposées supérieures à la dilution finale voulue. 
