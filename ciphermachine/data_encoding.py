#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bitarray
import binascii
import base64

# convert bits to readable
def bits2readable(b):
  b = bitarray.bitarray(b).tobytes()
  readable = base64.b64encode(b).decode()
  return readable

# convert readable to bits
def readable2bits(readable):
  b = base64.b64decode(readable.encode())
  c = bitarray.bitarray()
  c.frombytes(b)
  c = c.tolist()
  output = ""
  for x in c:
    if x==False: output+='0'
    if x==True: output+='1'
  return output

# open file as bit string
def open_file(filename):
  try:
    f = open(filename,"rb")
    data = f.read()
    f.close()
    ba = bitarray.bitarray()
    ba.frombytes(data)
    boolarray = ba.tolist()
    output = ""
    for bit in boolarray:
      if bit==False: output+="0"
      if bit==True: output+="1"
    return output
  except:
    print("File '"+filename+"' not found.")
    exit(1)

# save file from bit string
def save_file(filename, bits):
  try:
    f = open(filename,"wb")
    ba = bitarray.bitarray(bits)
    ba.tobytes()
    f.write(ba)
    f.close()
  except:
    print("File '"+filename+"' could not be written.")
    exit(1)

# utf-8 string to bitstring
def string2bits(string):
    c = bitarray.bitarray()
    c.frombytes(string.encode())
    bits = c.tolist()
    bits = ''.join(map(str,list(map(int,bits))))
    return bits

# bitstring to utf-8 string
def bits2string(bits):
    string = ""
    c = bitarray.bitarray(bits)
    string = c.tobytes().decode()
    return string

# bitstring to bit list
def bits2list(bits):
    l = []
    for bit in bits:
        l.append(int(bit))
    return l

# bit list to bitstring
def list2bits(l):
    bits = ""
    for bit in l:
        bits += str(bit)
    return bits

# human-readable password to key
def password2key(password, keylength):
    if len(string2bits(password))>=keylength:
        key = bits2readable(string2bits(password)[:keylength])
        return key
    else:
        print("Password is too short.")
        exit(1)
