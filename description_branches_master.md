# Description of branches

## 23_01_forcer_premieres_dilutions
On transmettra une liste de listes de type [[dil1, vol1], [dil2, vol2]]

L'erreur d'évolution des CT dans le cas de dilution de CT est due au fait que le tube_en_cours_de_dil n'est pas mis à jour. (vers 124)

Fixed : Evolution des CT correcte. 
   Reste à créer la dernière dilution.

je merge sur main (même si l'objectif est incomplet).

## 23_01_forcer_premieres_dilutions_suite
La fonction dilution est capable de gérer des dilutions imposées. Tout au moins pur les tubes exprimés en CT.

## 23_01_ameliorer_signature
  * Améliorer la signature des différentes classes et fonctions (Il suffit en fait d'imposer un argument nommé dès le premier argument.
    ). 
  * protection contre les dilutions imposées supérieures à la dilution finale voulue. 

## 23_01_utilisation
Ajout d'exemples (3) réels

## 23_01_bug_fix_solution_fille
J'ai trouvé un bug : 

Dilution 1
Prélever 13.14 µl de solution mère <Aliquot, vol : 500 contenant <Liquid : CephVRS_GAI/VAL>>, ajouter 986.86 de diluent 
En sortie on aura le tube : <Aliquot, vol : 1000 contenant <Liquid : CephVRS_GAI/VAL/dil_1>>
Dilution 2
Prélever 13.14 µl de solution mère <Aliquot, vol : 500 contenant <Liquid : CephVRS_GAI/VAL>>, ajouter 986.86 de diluent 
En sortie on aura le tube : <Aliquot, vol : 1000 contenant <Liquid : CephVRS_GAI/VAL/dil_2>>

La seconde occurence de 500 contenant <Liquid : CephVRS_GAI/VAL>> est fausse (il faut écrire : <Liquid : CephVRS_GAI/VAL/dil_1>)

explication : le bug n'existe plus si on utilise l'argument `lst_imposed_dil=dil_imposes`.
MERGED sur main