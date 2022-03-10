#!/bin/env python3
"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
Main python file of the projet.
"""

import numpy as np
import matplotlib.pyplot as plt
from AES_utils import AESUtils


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

    # Isolation du dernier Round
    n = L.shape[0]
    ind_start = 3050
    ind_end = 3250
    last_round = np.zeros((n, ind_end - ind_start))
    for i in range(n):
        last_round[i] = L[i, ind_start:ind_end]

    # Attaque
    SBox = np.array([[99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118],
            [202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192],
            [183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21],
            [4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117],
            [9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132],
            [83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207],
            [208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168],
            [81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210],
            [205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115],
            [96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219],
            [224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121],
            [231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8],
            [186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138],
            [112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158],
            [225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223],
            [140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]])
    aes = AESUtils(SBox)
