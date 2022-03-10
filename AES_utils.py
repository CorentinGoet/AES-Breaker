"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""


class AESUtils:
    """
    Classe contenant les différentes méthodes et opérations nécessaires au craquage de l'AES.
    """
    def __init__(self):
        # TODO: add the SBox and other data as variables
        pass

    def AddRoundKey(self, key, plaintext):
        """
        Première opération de chiffrement réalisée par l'algorithme. Il s'agit de l'addition dans un Corps de Gallois
        entre la clé secrète et le bloc de texte clair.

        :param key: clé secrète (128 bits)
        :param plaintext: Bloc de message clair
        :return:
        """
        pass

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
        pass

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
    pass
