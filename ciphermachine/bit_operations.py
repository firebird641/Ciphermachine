#!/usr/bin/python3
# -*- coding: utf-8 -*-

# xor two bitstrings
def xor_bitstrings(x,y):
    if len(x) != len(y):
        print("[Error] XOR-Bitstrings of unequal length.")
        exit(1)
    z = ""
    for c in range(len(x)):
        z += str(int(int(x[c])^int(y[c])))
    return z

# xor a list of bits with each other
def xor_bitlist(bitlist):
    XOR = 0
    for bit in bitlist:
        XOR += bit
    XOR = XOR % 2
    return XOR

# and between two bitstrings
def and_bitstrings(x,y):
    if len(x) != len(y):
        print("[Error] AND-Bitstrings of unequal length.")
        exit(1)
    z = ""
    for c in range(len(x)):
        z += str(int(int(x[c])&int(y[c])))
    return z

# invert bitstring
def not_bitstring(x):
    o = ""
    for bit in x:
        o += str(1-int(bit))
    return o

# shift register chain
def shift_chain(chain, feedback):
    shifted = [feedback]
    for x in chain[:-1]:
        shifted.append(x)
    return shifted

# right bit rotation,
def bitstring_rotation_R(x,k):
    rot = -int(k,2) % len(x)
    output = x[rot:]+x[:rot]
    return output

# left bit rotation
def bitstring_rotation_L(x,k):
    rot = int(k,2) % len(x)
    output = x[rot:]+x[:rot]
    return output

# split a bitstring into chunks (with optional padding)
def split_chunks(x, length, padding=True, padstring="0"):
    if len(x)==0:
        x = padstring*length
    a = [x[i:i+length] for i in range(0, len(x), length)]
    last = a[-1]
    missing = length-len(last)
    if padding:
        a[-1] = last+padstring*missing
        padding_length = missing
        return a, padding_length
    else:
        return a

# split a bitstring into 2 halfs
def split_half(bits):
    if len(bits)%2 != 0:
        print("[ERROR] Bitstring can not be split into equal halfs.")
        exit(1)
    l = len(bits)
    half = int(l/2)
    output = []
    output.append(''.join(bits[:half]))
    output.append(''.join(bits[half:]))
    return output

# swap two list items
def swap_list(l, x, y):
    a = l[x]
    b = l[y]
    l[x] = b
    l[y] = a
    return l

# forward feed through an sbox
def forward_substitution(bits,sbox):
  if 2**len(bits) == len(sbox.items()):
    y = sbox[bits]
    return y
  else:
    print("[Error] Forward Substitution failed because of invalid input lengths.")
    exit(1)
    
# reverse feed through a bijective sbox
def reverse_substitution(bits,sbox):
  if 2**len(bits) == len(sbox.items()):
    for key, replacement in sbox.items():
      if replacement == bits:
        return key
  else:
    print("[Error] Reverse Substitution failed because of invalid input lengths.")
    exit(1)

# forward feed through a pbox
def forward_permutation(bits,pbox):
  output = []
  for i in pbox:
      output.append(bits[i])
  output = ''.join(output)
  return output

# reverse feed through bijective a pbox
def reverse_permutation(bits,pbox):
  size = len(bits)
  if size != len(pbox):
      print("[ERROR] Reverse Permutation failed because of invalid input lengths.")
      exit(1)
  output = ['0']*size
  c = 0
  for x in pbox:
    output[c] = str(bits[x])
    c+=1
  output = ''.join(output)
  return output
