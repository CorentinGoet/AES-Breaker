# AES-Breaker

(For the French explanations on the project, please read projet_2022.pdf).

This project is an EMA (ElectroMagnetic Analysis) attack on an AES-128 encryption algorithm implemented on an FPGA.
In order to perform this attack, the electromagnetic emissions from the FPGA have been measured during the encryption
for 20,000 different messages. By correlating these messages with the electromagnetic emissions from the electronic card,
we will are able to find the key used by the circuit.

## Preprocessing
The data from the measure campaign is presented in the following way. For each plaintext message, a CSV file has been
produced with the following information:
In the file name, we find: 
- the key used to encrypt the message (It is always the same and will be used to compare to our results)
- the plaintext message
- the ciphertext
In the file, there is a measure of the EM emissions from the card during the encryption of the message (4000 points).

Because the measure campaign contains a lot of data, only 10 of the CSV files will be added to the GitHub repository. 
They can be found ini the data_example directory.

This data will be pre-processed by the program _preprocessing.py_ to transform these files into 4 Numpy binary files:
- key_dec.npy containing the keys (since all the keys used are the same, it is actually an array of the same value)
- pti_dec.npy containing the plaintext messages
- cto_dec.npy containing the ciphertext output of the algorithm
- L.npy containing the EM measures.

