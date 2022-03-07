"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
script python chargé de la prédiction de la clé pour une étape
"""

import numpy as np


def keysched(key):
    SBox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71,
            240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113,
            216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110,
            90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76,
            88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157,
            56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100,
            93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6,
            36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101,
            122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102,
            72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135,
            233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
    RCon = np.array([[1, 2, 4, 8, 16, 32, 64, 128, 27, 54],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    key_1, key_2, key_3, key_4 = [key[:, i] for i in range(4)]
    w = np.zeros((np.shape(key)[0], np.shape(key)[1], 11))
    w[:, :, 1] = key

    for r in range(1, 11):
        tmp = [SBox[int(key_4[i])] for i in [1, 2, 3, 0]]
        tmp = np.bitwise_xor(tmp, RCon[:, r-1])
        key_1 = np.bitwise_xor(key_1, tmp)
        key_2 = np.bitwise_xor(key_2, key_1)
        key_3 = np.bitwise_xor(key_3, key_2)
        key_4 = np.bitwise_xor(key_4, key_3)
        w[:, :, r] = [key_1, key_2, key_3, key_4]

    return w

if __name__ == '__main__':
    keys = np.load('processed_data/key_dec.npy')
    key = np.reshape(keys[0], (4, 4))
    np.save('processed_data/keysched.npy', keysched(key))
