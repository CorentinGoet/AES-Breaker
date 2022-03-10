"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import numpy as np


class AESUtils:
    """
    Classe contenant les différentes méthodes et opérations nécessaires au craquage de l'AES.
    """
    def __init__(self, SBox):
        # TODO: add the SBox and other data as variables
        self.SBox = SBox

    def addRoundKey(self, plaintext):
        """
        Première opération de chiffrement réalisée par l'algorithme. Il s'agit de l'addition dans un Corps de Gallois
        entre la clé secrète et le bloc de texte clair.

        :param plaintext: Bloc de message clair
        :return: Tableau des résultats possibles en fonction du plaintext
        """

        if not np.size(plaintext) == 16:
            raise ValueError("L'argument doit être un tableau de 16 octets")

        # Création du vecteur de clés et de la matrice de résultats
        key = np.arange(0, 256, 1)
        output = np.zeros((16, 256))

        # Calcul
        for i in range(16):
            output[i] = np.bitwise_xor(key, plaintext[i])

        return output

    def computeKeySchedule(self, key):
        """
        Calcule les sous-clés utilisées dans chaque round du chiffrement.

        :param key: Clé secrète (128 bits)
        """
        pass

    def subByte(self, initialByte):
        """
        Opération de substitution d'octets. La substitution est réalisée à partir d'un tableau de 16x16 appelé SBox.
        Les 4 bits de poids fort déterminent la ligne et les 4 bits de poids faible déterminent la colonne.
        Cette opération est non-linéaire.

        :param initialByte: Octet d'entrée à substituer
        :return: Octet substitué
        """
        indCol = initialByte & 0x00FF
        indLin = (initialByte & 0xFF00) >> 4

        return self.SBox[indLin, indCol]

    def shiftRow(self, byteMat):
        """
        Opération de rotation d'octet sur la matrice de 4x4 octets donnée en entrée. Cette opération réalise un décalage
        circulaire d'un nombre octet vers la droite correspondant à l'indice de la ligne (0 pour la première ligne,
        1 pour la deuxième, ...).

        :param byteMat: Matrice de 4x4 octets
        :return: Matrice résultat de la rotation
        """
        pass

    def mixColumns(self, byteMat):
        """
        Opération de diffusion linéaire de l'information sur les différentes colonnes.

        :param byteMat: Matrice de 4x4 octets
        :return: Matrice diffusée
        """
        pass


if __name__ == '__main__':
    pti = np.load('processed_data/pti_dec.npy')
    print(pti.shape)

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
    print(aes.addRoundKey(pti[0]))

