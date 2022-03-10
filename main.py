#!/bin/env python3
"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
Main python file of the projet.
"""

import numpy as np
import matplotlib.pyplot as plt
from AES_utils import AESUtils



if __name__ == '__main__':
    # Paramètres du programme
    data_directory = "processed_data"
    nb_traces = 10  # Nombre de traces à afficher

    # chargement des données
    L = np.load(data_directory + "/" + "L.npy")
    key_dec = np.load(data_directory + "/" + "key_dec.npy")
    pti_dec = np.load(data_directory + "/" + "pti_dec.npy")
    cto_dec = np.load(data_directory + "/" + "cto_dec.npy")

    # Affichage des premières traces
    plt.figure()
    plt.title("Fuites électromagnétiques ({} premières traces)".format(nb_traces))
    plt.xlabel("échantillons")
    plt.ylabel("amplitude")
    for i in range(nb_traces):
        plt.plot(L[i])

    # Affichage de la consommation moyenne
    avg = np.mean(L, 0)
    plt.figure()
    plt.title("Fuites électromagnétiques moyennes")
    plt.xlabel("échantillons")
    plt.ylabel("amplitude")
    plt.plot(avg)

    plt.show()

