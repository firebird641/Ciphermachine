#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ciphermachine.data_encoding import *
from ciphermachine.bit_operations import *
import math

# electronic code book mode
class ecb_mode(object):
    def __init__(self, blockcipher):
        self.cipher = blockcipher
    def encrypt(self, cleartext, key, blocksize):
        blocks, padding_len = split_chunks(cleartext, blocksize, padding=True)
        output = ""
        for block in blocks:
            output += self.cipher.encrypt(block, key)
        return output, padding_len
    def decrypt(self, ciphertext, key, blocksize, padding_len=0):
        blocks = split_chunks(ciphertext, blocksize, padding=False)
        output = ""
        for block in blocks:
            output += self.cipher.decrypt(block, key)
        output = output[:len(output)-padding_len]
        return output

# cipher block chaining mode
class cbc_mode(object):
    def __init__(self, blockcipher):
        self.cipher = blockcipher
    def encrypt(self, cleartext, key, iv, blocksize):
        blocks, padding_len = split_chunks(cleartext, blocksize, padding=True)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                block = xor_bitstrings(block,iv)
                ciphertext = self.cipher.encrypt(block, key)
                output += ciphertext
                counter = 1
            else:
                block = xor_bitstrings(block,ciphertext)
                ciphertext = self.cipher.encrypt(block, key)
                output += ciphertext
        return output, padding_len
    def decrypt(self, ciphertext, key, iv, blocksize, padding_len=0):
        blocks = split_chunks(ciphertext, blocksize, padding=False)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                out = self.cipher.decrypt(block, key)
                output += xor_bitstrings(out,iv)
                cleartext = block
                counter = 1
            else:
                out = self.cipher.decrypt(block, key)
                output += xor_bitstrings(out,cleartext)
                cleartext = block
        output = output[:len(output)-padding_len]
        return output

# propagating cipher block chaining mode
class pcbc_mode(object):
    def __init__(self, blockcipher):
        self.cipher = blockcipher
    def encrypt(self, cleartext, key, iv, blocksize):
        blocks, padding_len = split_chunks(cleartext, blocksize, padding=True)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                lastplain = block
                block = xor_bitstrings(block,iv)
                ciphertext = self.cipher.encrypt(block, key)
                output += ciphertext
                ciphertext = xor_bitstrings(ciphertext,lastplain)
                counter = 1
            else:
                lastplain = block
                block = xor_bitstrings(block,ciphertext)
                ciphertext = self.cipher.encrypt(block, key)
                output += ciphertext
                ciphertext = xor_bitstrings(ciphertext,lastplain)
        return output, padding_len
    def decrypt(self, ciphertext, key, iv, blocksize, padding_len=0):
        blocks = split_chunks(ciphertext, blocksize, padding=False)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                lastcipher = block
                out = self.cipher.decrypt(block, key)
                cleartext = xor_bitstrings(out,iv)
                output += cleartext
                cleartext = xor_bitstrings(cleartext,lastcipher)
                counter = 1
            else:
                lastcipher = block
                out = self.cipher.decrypt(block, key)
                cleartext = xor_bitstrings(out,cleartext)
                output += cleartext
                cleartext = xor_bitstrings(cleartext,lastcipher)
        output = output[:len(output)-padding_len]
        return output

# cipher feedback mode
class cfb_mode(object):
    def __init__(self, blockcipher):
        self.cipher = blockcipher
    def encrypt(self, cleartext, key, iv, blocksize):
        blocks, padding_len = split_chunks(cleartext, blocksize, padding=True)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                keystream = self.cipher.encrypt(iv, key)
                ciphertext = xor_bitstrings(block, keystream)
                output += ciphertext
                counter = 1
            else:
                keystream = self.cipher.encrypt(ciphertext, key)
                ciphertext = xor_bitstrings(block, keystream)
                output += ciphertext
        return output, padding_len
    def decrypt(self, ciphertext, key, iv, blocksize, padding_len=0):
        blocks = split_chunks(ciphertext, blocksize, padding=False)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                keystream = self.cipher.encrypt(iv, key)
                ciphertext = block
                cleartext = xor_bitstrings(block, keystream)
                output += cleartext
                counter = 1
            else:
                keystream = self.cipher.encrypt(ciphertext, key)
                ciphertext = block
                cleartext = xor_bitstrings(block, keystream)
                output += cleartext
        output = output[:len(output)-padding_len]
        return output

# output feedback mode
class ofb_mode(object):
    def __init__(self, blockcipher):
        self.cipher = blockcipher
    def encrypt(self, cleartext, key, iv, blocksize):
        blocks, padding_len = split_chunks(cleartext, blocksize, padding=True)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                keystream = self.cipher.encrypt(iv, key)
                ciphertext = xor_bitstrings(block,keystream)
                output += ciphertext
                counter = 1
            else:
                keystream = self.cipher.encrypt(keystream, key)
                ciphertext = xor_bitstrings(keystream,block)
                output += ciphertext
        return output, padding_len
    def decrypt(self, ciphertext, key, iv, blocksize, padding_len=0):
        blocks = split_chunks(ciphertext, blocksize, padding=False)
        output = ""
        counter = 0
        for block in blocks:
            if counter==0:
                keystream = self.cipher.encrypt(iv, key)
                cleartext = xor_bitstrings(block,keystream)
                output += cleartext
                counter = 1
            else:
                keystream = self.cipher.encrypt(keystream, key)
                cleartext = xor_bitstrings(block,keystream)
                output += cleartext
        output = output[:len(output)-padding_len]
        return output

# feistel cipher
class feistel_network(object):
    def __init__(self, roundfunction, keyschedule):
        self.roundfunction = roundfunction
        self.keyschedule = keyschedule
    def encrypt(self, cleartext, key):
        keys = self.keyschedule(key)
        split_block = split_half(cleartext)
        L = split_block[0]
        R = split_block[1]
        for key in keys:
            R_function = self.roundfunction(R,key)
            L_old = L
            L = R
            R = xor_bitstrings(L_old,R_function)
        output = ''.join([R,L])
        return output
    def decrypt(self, ciphertext, key):
        keys = self.keyschedule(key)
        keys = list(reversed(keys))
        split_block = split_half(ciphertext)
        L = split_block[0]
        R = split_block[1]
        for key in keys:
            R_function = self.roundfunction(R,key)
            L_old = L
            L = R
            R = xor_bitstrings(L_old,R_function)
        return ''.join([R,L])

# linear feedback shift register
class LFSR(object):
    def __init__(self, iv):
        self.registers = iv
    def shift(self, inputbit):
        self.registers = shift_chain(self.registers, inputbit)
    def state(self):
        return ''.join(map(str,self.registers))
    def output(self, x):
        return self.registers[x]

# sponge construction for keccak-based hashing
class sponge_construction(object):
    def __init__(self, round_function, block_length, f_length):
        self.roundfunc = round_function
        self.blocklength = block_length
        self.flength = f_length
    def hash(self, inputbits):
        bit_blocks, padding = split_chunks(inputbits, self.blocklength, padding=True)
        iv = "0"*self.flength
        r = iv[:self.blocklength]
        c = iv[self.blocklength:]
        # absorbtion
        for block in bit_blocks:
            r = xor_bitstrings(r,block)
            i = r+c
            f = self.roundfunc(i)
            r = f[:self.blocklength]
            c = f[self.blocklength:]
        # output
        return r[:self.blocklength]
    def pseudorandom(self, seed, bitcount):
        bit_blocks, padding = split_chunks(seed, self.blocklength, padding=True)
        iv = "0"*self.flength
        r = iv[:self.blocklength]
        c = iv[self.blocklength:]
        # absorbtion
        for block in bit_blocks:
            r = xor_bitstrings(r,block)
            i = r+c
            f = self.roundfunc(i)
            r = f[:self.blocklength]
            c = f[self.blocklength:]
        # squeezing
        count = math.ceil(bitcount/self.blocklength)
        output = ""
        for q in range(count):
            output += r
            i = r+c
            f = self.roundfunc(i)
            r = f[:self.blocklength]
            c = f[self.blocklength:]
        return output[:self.blocklength]

# substitution-permutation network
class sp_network(object):
    def __init__(self, sboxes, pbox, keyschedule):
        self.sboxes = sboxes
        self.pbox = pbox
        self.keyschedule = keyschedule
    def encrypt(self, cleartext, key):
        keys = self.keyschedule(key)
        c = 0
        xor = cleartext
        if len(keys)>=3:
            for key in keys:
                if c < len(keys)-2:
                    xor = xor_bitstrings(xor, key)
                    p_input = ""
                    for i in range(len(self.sboxes)):
                        box = self.sboxes[i]
                        s_input = split_chunks(xor,  int(math.log(len(box),2)), padding=False)[i]
                        p_input += forward_substitution(s_input,box)
                    xor = forward_permutation(p_input,self.pbox)
                if c == len(keys)-2:
                    xor = xor_bitstrings(xor, key)
                    p_input = ""
                    for i in range(len(self.sboxes)):
                        box = self.sboxes[i]
                        s_input = split_chunks(xor, int(math.log(len(box),2)), padding=False)[i]
                        p_input += forward_substitution(s_input,box)
                if c == len(keys)-1:
                    output = xor_bitstrings(p_input, key)
                c += 1
        else:
            for key in keys:
                xor = xor_bitstrings(xor, key)
                p_input = ""
                for i in range(len(self.sboxes)):
                    box = self.sboxes[i]
                    s_input = split_chunks(xor,  int(math.log(len(box),2)), padding=False)[i]
                    p_input += forward_substitution(s_input,box)
                xor = forward_permutation(p_input,self.pbox)
            output = xor
        return output
    def decrypt(self, ciphertext, key):
        keys = self.keyschedule(key)
        keys = list(reversed(keys))
        c = 0
        xor = ciphertext
        if len(keys)>=3:
            for key in keys:
                if c == 0:
                    xor_output = xor_bitstrings(xor, key)
                if c == 1:
                    xor_input = ""
                    for i in range(len(self.sboxes)):
                        box = self.sboxes[i]
                        s_input = split_chunks(xor_output,  int(math.log(len(box),2)), padding=False)[i]
                        xor_input += reverse_substitution(s_input,box)
                    xor_output = xor_bitstrings(xor_input, key)
                if c > 1:
                    p_output = reverse_permutation(xor_output,self.pbox)
                    xor_input = ""
                    for i in range(len(self.sboxes)):
                        box = self.sboxes[i]
                        s_input = split_chunks(p_output,  int(math.log(len(box),2)), padding=False)[i]
                        xor_input += reverse_substitution(s_input,box)
                    xor_output = xor_bitstrings(xor_input, key)
                c += 1
                output= xor_output
        else:
            for key in keys:
                p_output = reverse_permutation(xor,self.pbox)
                xor_input = ""
                for i in range(len(self.sboxes)):
                    box = self.sboxes[i]
                    s_input = split_chunks(p_output,  int(math.log(len(box),2)), padding=False)[i]
                    xor_input += reverse_substitution(s_input,box)
                xor = xor_bitstrings(xor_input, key)
            output = xor
        return output

# compression function for oneway-hashing
def davies_meyer_compression(m, H, blockcipher):
    E = blockcipher.encrypt(H, m)
    output = xor_bitstrings(E, H)
    return output

# compression function for oneway-hashing
def matyas_meyer_oseas_compression(m, H, blockcipher):
    E = blockcipher.encrypt(m, H)
    output = xor_bitstrings(E, m)
    return output

# compression function for oneway-hashing
def miyaguchi_preneel_compression(m, H, blockcipher):
    E = blockcipher.encrypt(m, H)
    output = xor_bitstrings(xor_bitstrings(E, m),H)
    return output

# merkle damgard construction
class merkle_damgard_construction(object):
    def __init__(self, compression_function, blockcipher, block_length):
        self.compression = compression_function
        self.blockcipher = blockcipher
        self.blocklength = block_length
    def hash(self, inputbits):
        iv = "0"*self.blocklength
        blocks,padding = split_chunks(inputbits, self.blocklength, padding=True, padstring="0")
        H = iv
        for m in blocks:
            H = self.compression(m, H, self.blockcipher)
        return H

# hash-based message authentication code
class HMAC(object):
    def __init__(self, hash_function):
        self.hashfunction = hash_function
    def authenticate(self, inputbits, key):
        ipad = ("00110110"*math.ceil(len(key)/4))[:len(key)]
        opad = ("01011100"*math.ceil(len(key)/4))[:len(key)]
        inner_hash = self.hashfunction.hash(xor_bitstrings(key,ipad)+inputbits)
        outer_hash = self.hashfunction.hash(xor_bitstrings(key,opad)+inner_hash)
        return outer_hash
