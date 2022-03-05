"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This simple python script loads the value table L.npy and fetches the values corresponding to the last round and
stores it into a binary file called last_round.npy
"""

import numpy as np


if __name__ == '__main__':
    value_array = np.load('processed_data/L.npy')

    n = value_array.shape[0]
    ind_start = 3050
    ind_end = 3250
    last_round = np.zeros((n, ind_end - ind_start))
    for i in range(n):
        last_round[i] = value_array[i, ind_start:ind_end]

    np.save('processed_data/last_round.npy', last_round)


