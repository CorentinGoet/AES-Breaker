# Rapport
Ce document contient la version provisoire du rapport de ce projet. Il s'agit des réponses aux questions posées dans
le sujet.

## Question 1 : Courbes de consommation
Le tracé des courbes de consommation est obtenu en exécutant le programme visual.py.
En utilisant ces tracés, on peut déterminer que le chiffrement à lieu entre les points 810 et 2360 de chaque mesure.

## Question 2 : Moyennes de consommation
En traçant la moyenne des courbes de consommation (deuxième courbe produite par visual.py), on s'aperçoit que le dernier
round de l'algorithme AES a lieu entre les points 3050 et 3250 de chaque mesure.

## Question 3 : Distance de Hamming

## Question 4 : Prédiction de la clé
La clé 4x4 attendue par l'algorithme d'inversion est:
```
[[ 76 140 223  35]
 [181 201   6 247]
 [144  87 236 113]
 [132  25  58 103]]
```

## Question 5 : Dernier Round
En utilisant le tracé de la question 2, on identifie que le dernier round à lieu entre les échantillons 3050 et 3250.
On isole donc cette portion de chaque mesure dans le programme `get_last_round.py` et on le stocke dans `last_round.npy`.

## Question 6 : Clés intermédiaires
Le programme `keysched.py` calcule les clés intermédiaires associées à chaque round et stocke la matrice dans le fichier
`keysched.npy`.
