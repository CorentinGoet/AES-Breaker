"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This program transforms the data contained in the database into a numpy file
to be used more easily in the rest of the process.
"""

import numpy as np
from os import listdir


def getInfo(filename):
    """
    Extracts the info from the name of the files. The name of the file is as follows:
    trace_AES_[trace number (dec)]_key=[key used to encrypt the plaintext (hex)]_pti=[plain text (hex)]_cto=[cipher text (hex)].csv
    :param filename: name of the file containing the data
    :return: (dict)  {'key': key, 'pti': pti, 'cto': cto}
    """
    file_info = {}
    fields = filename.split('=')
    file_info['key'] = fields[1][:-4]
    file_info['pti'] = fields[2][:-4]
    file_info['cto'] = fields[3][:-4]
    return file_info

def hex2dec(hex_str):
    """
    Transforms an hexadecimal string into an list of integers.
    Each group of 2 char gives 1 int.
    :param hex_str: hex string
    :return: list of int
    """
    res = []
    for i in range(0, len(hex_str)-1, 2):
        res.append(int(hex_str[i:i+2], 16))
    return res


if __name__ == '__main__':

    # Parameters
    nb_traces = 20000   # Nombre de mesures réalisées
    # nb_traces = 10      # example version
    nb_points = 4000    # Nombre de points par traces
    data_directory = "data"
    output_directory = "processed_data"

    # Processing
    key_list = []
    pti_list = []
    cto_list = []
    traces_array = np.zeros((nb_traces, nb_points))
    files = listdir(data_directory)
    for i in range(nb_traces):
        info = getInfo(files[i])
        key_list.append(info['key'])
        pti_list.append(info['pti'])
        cto_list.append(info['cto'])
        traces_array[i, :] = np.loadtxt(data_directory + '/' + files[i],
                                        delimiter=',')
        if i % 100 == 0:
            # gives feedback during execution
            print("trace {} processed".format(i))

    # Convert to decimal values
    key_dec = np.zeros((nb_traces, 16))
    pti_dec = np.zeros((nb_traces, 16))
    cto_dec = np.zeros((nb_traces, 16))
    for i in range(nb_traces):
        key_dec[i, :] = hex2dec(key_list[i])
        pti_dec[i, :] = hex2dec(pti_list[i])
        cto_dec[i, :] = hex2dec(cto_list[i])

    np.save(output_directory + '/' + 'key_dec.npy', key_dec)
    np.save(output_directory + '/' + 'pti_dec.npy', pti_dec)
    np.save(output_directory + '/' + 'cto_dec.npy', cto_dec)
    np.save(output_directory + '/' + 'L.npy', traces_array)


