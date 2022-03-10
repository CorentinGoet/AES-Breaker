# AES-Breaker

This project is an EMA (Electro-Magnetic Analysis) attack on an AES-128 encryption algorithm implemented on an FPGA.
In order to perform this attack, the electromagnetic emissions from the FPGA have been measured during the encryption
for 20,000 different messages. By correlating these messages with the electromagnetic emissions from the electronic card,
we will are able to find the key used by the circuit.

Ce projet est une attaque par canaux cachés sur un algorithme de chiffrement AES-128 implémenté sur une carte FPGA.
Cette attaque consiste à corréler des mesures de rayonnement électromagnétique de la carte avec les messages chiffrés en
sortie de l'algorithme pour retrouver la clé.

## Contexte
Ce projet est réalisé au sein du cours de Sécurité des Composants de l'ENSTA Bretagne, il a été réalisé par Corentin
Goetghebeur et Chris Arridi entre le 28/02/2022 et le 13/03/2022.

This project is included in an Electronic Components Security in ENSTA Bretagne (French Engineering School). It was made
by Corentin Goetghebeur and Chris Arridi between 28/02/2022 and 13/03/2022.

Pour plus de détails sur ce projet, voir rapport.md.

