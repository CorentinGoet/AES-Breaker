"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This Python script displays the power consumption in order to determine the beginning and end of the encryption.
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Program parameters
    data_directory = "processed_data"
    nb_traces = 10      # Number of traces to display

    # Loading data
    L = np.load(data_directory + "/" + "L.npy")
    key_dec = np.load(data_directory + "/" + "key_dec.npy")
    pti_dec = np.load(data_directory + "/" + "pti_dec.npy")
    cto_dec = np.load(data_directory + "/" + "cto_dec.npy")

    # Display power consumption of the first traces
    plt.figure()
    plt.title("Power Consumption ({} first traces)".format(nb_traces))
    for i in range(nb_traces):
        plt.plot(L[i])

    # Display average power consumption
    avg = np.mean(L, 0)
    plt.figure()
    plt.title("Average power consumption")
    plt.plot(avg)

    plt.show()




