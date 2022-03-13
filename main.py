#!/bin/env python3
"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
Main python file of the projet.
"""

import numpy as np
import matplotlib.pyplot as plt
from AES_utils import AESUtils
import time

def hammingWeight(byte: int):
    """
    Calcule le poids de Hamming d'un octet.

    :param byte: octet donc on veut calculer le poid
    :return: poids
    """
    bin_byte = bin(byte)[2:]
    output = 0
    for bit in bin_byte:
        output += int(bit)
    return output



if __name__ == '__main__':
    # Paramètres du programme
    data_directory = "processed_data"
    nb_traces = 10  # Nombre de traces à afficher

    # chargement des données
    L = np.load(data_directory + "/" + "L.npy")
    key = np.load(data_directory + "/" + "key_dec.npy")
    pti = np.load(data_directory + "/" + "pti_dec.npy")
    cto = np.load(data_directory + "/" + "cto_dec.npy")

    # Affichage des premières traces
    plt.figure()
    plt.title("Courbes de consommation ({} premières traces)".format(nb_traces))
    plt.xlabel("temps")
    plt.ylabel("fuites électromagnétiques")
    for i in range(nb_traces):
        plt.plot(L[i])

    # Affichage de la consommation moyenne
    avg = np.mean(L, 0)
    plt.figure()
    plt.title("Courbe de consommation moyenne")
    plt.xlabel("temps")
    plt.ylabel("fuites électromagnétiques")
    plt.plot(avg)

    plt.show()

    # Affichage de la clé attendue
    print("Clé attendue en sortie de l'algorithme d'inversion: ")
    key_4x4 = np.reshape(np.array(key[0], dtype=np.int32), (4, 4))
    print(key_4x4)

    # Isolation du dernier Round
    n = L.shape[0]
    ind_start = 3050
    ind_end = 3300
    last_round = np.zeros((n, ind_end - ind_start))
    for i in range(n):
        last_round[i] = L[i, ind_start:ind_end]

    ### Prédiction de l'état précédent le dernier round ###
    aes = AESUtils()
    # Création des hypothèses de clé
    key_hypotheses = np.arange(0, 256, 1)   # Hypothèses de clés sur 8 bits

    # Répétition de la matrice de cypher
    try:
        state_predict = np.load('processed_data/state_predict.npy')
        print("matrice de prédictions chargée")
    except FileNotFoundError:
        state_predict = np.zeros((key_hypotheses.size, cto.shape[0], cto.shape[1]), dtype=np.int32)
        for i in range(256):
            state_predict[i, :, :] = cto

        print("Début du calcul de l'état initial")
        print("SOYEZ PATIENT CETTE ETAPE PEUT PRENDRE PLUS DE 20 MINUTES")
        t0 = time.time()
        for trace in range(cto.shape[0]):
            for key_i in key_hypotheses:
                # AddRoundKey <=> xor
                state_predict[key_i, trace, :] = aes.addRoundKey(state_predict[key_i, trace, :], key_i)
                # shiftRow inverse
                state_predict[key_i, trace, :] = aes.invShiftRow(state_predict[key_i, trace, :])
                # SubByte inverse
                state_predict[key_i, trace, :] = aes.invSubByte(state_predict[key_i, trace, :])
            if trace % 100 == 0:    # pour observer le progrès du calcul
                print("Prédiction terminée pour la trace n° {} - temps écoulé : {}".format(trace, round(time.time() - t0, 2)))

        print("Prédiction terminée - temps total écoulé: ", time.time() - t0)
        np.save('processed_data/state_predict.npy', state_predict)

    #print(state_predict)

    # Calcul des poids de Hamming
    try:
        hamming_weight = np.load('processed_data/hamming_weight.npy')
        print("Matrice de poids de Hamming chargée !")
    except FileNotFoundError:
        t0 = time.time()
        hamming_weight = np.zeros(state_predict.shape, dtype=np.int32)
        for trace in range(state_predict.shape[1]):
            for key_i in range(state_predict.shape[0]):
                for i in range(state_predict.shape[2]):
                    hamming_weight[key_i, trace, i] = hammingWeight(state_predict[key_i, trace, i])
            if trace % 100 == 0:    # pour observer le progrès du calcul
                print("Calcul du poids de Hamming terminé pour la trace n° {} "
                      "- temps écoulé : {}".format(trace, round(time.time() - t0, 2)))
        np.save('processed_data/hamming_weight.npy', hamming_weight)
        print("matrice de poids de Hamming calculée et enregistrée !")





