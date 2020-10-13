#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
from ciphermachine.data_encoding import *
from ciphermachine.bit_operations import *

# random bitstring
def random_bitstring(length):
  key = ""
  for _ in range(length):
    key += str(random.randint(0,1))
  return key

# generate random bijective sbox
def random_bijective_sbox(inputbits):
  sbox = {}
  for x in range(2**inputbits):
    b = "{0:b}".format(x).zfill(inputbits)
    sbox[b] = b
  for _ in range(2**inputbits*10):
    r1 = random.choice(list(sbox.keys()))
    r2 = random.choice(list(sbox.keys()))
    sbox = swap_list(sbox,r1,r2)
  return sbox

# generate random bijective pbox
def random_bijective_pbox(inputbits):
  pbox = [0]*inputbits
  for x in range(0,inputbits):
    pbox[x] = x
  for _ in range(inputbits*10):
    a = random.randint(0,inputbits-1)
    b = random.randint(0,inputbits-1)
    pbox = swap_list(pbox,a,b)
  return pbox

# generate random non-bijective sbox
def random_non_bijective_sbox(inputbits,outputbits):
  sbox = {}
  count = 0
  for _ in range(2**inputbits):
    x = random.randint(0,2**outputbits-1)
    b = "{0:b}".format(x).zfill(outputbits)
    c = "{0:b}".format(count).zfill(inputbits)
    sbox[c] = b
    count += 1
  return sbox

# generate random non-bijective pbox
def random_non_bijective_pbox(inputbits,outputbits):
  pbox = [0]*outputbits
  for x in range(outputbits):
    pbox[x] = random.randint(0,inputbits)
  return pbox
