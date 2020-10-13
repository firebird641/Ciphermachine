#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ciphermachine.data_encoding import *
from ciphermachine.bit_operations import *
from ciphermachine.crypto_constructors import *
import time

# count differences between to bitstrings
def hamming_distance(x,y):
    if len(x) != len(y):
        print("[ERROR] Hamming Distance could not be calculated. Unequal input lengths.")
        exit(1)
    distance = 0
    for a in range(len(x)):
        if x[a]==y[a]:
            pass
        else:
            distance += 1
    return distance

# test avalanche effect for a specific cipher
def avalanche_test(x,y):
    if len(x)==len(y):
        hamming = hamming_distance(x,y)
        avalanche = hamming/len(x)*100
        return avalanche
    else:
        print("Avalanche test failed. Unequal output lengths.")
        exit(1)
