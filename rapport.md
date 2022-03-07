# Rapport
Ce document contient la version provisoire du rapport de ce projet. Il s'agit des réponses aux questions posées dans
le sujet.

## Question 1 : Courbes de consommation
Le tracé des courbes de consommation est obtenu en exécutant le programme visual.py.
En utilisant ces tracés, on peut déterminer que le chiffrement à lieu entre les points 810 et 2360 de chaque mesure.

## Question 2 : Moyennes de consommation
En traçant la moyenne des courbes de consommation (deuxième courbe produite par visual.py), on s'aperçoit que le dernier
round de l'algorithme AES a lieu entre les points 3050 et 3250 de chaque mesure.
On isole donc cette portion de la mesure (fichier _last_round.npy_).

## Question 3 : Distance de Hamming

## Question 4 : Prédiction de la clé
La prédiction de la clé est faite par le programme `keysched.py`.
