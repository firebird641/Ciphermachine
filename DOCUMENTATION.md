# Ciphermachine Documentation

## General Information

Ciphermachine is a Python Module for creating Symmetric Cryptosystems based on different Algorithms such as SP-Networks, Feistel-Ciphers, LFSRs and more. The following documentation covers all important functions and classes implemented in the module.

## Submodules

The Module is split into different submodules:

- Bit Operations
- Encoding Functions
- Generator Functions
- Cryptographic Functions
- Cryptoanalytic Functions

## Binary Data Representation

In most cases, Binary Data (Bits) are formatted as "Bit Strings". For example: "110100001010100111". In order to encode or decode data (like Binaries or Text), you can use the Encoding functions.

## In-Depth Documentation

### Bit Operations

**xor_bitstrings(x,y)**
XOR operation on two bitstrings (x and y). Returns one bitstring.

**xor_bitlist(bitlist)**
XOR (mod-2-Addition) on a list of bits (bitlist). Returns one Bit.

**and_bitstrings(x,y)**
AND operation on two bitstrings (x and y). Returns one bitstring.

**not_bitstring(x)**
NOT operation on a bitstring x. Returns a bitstring.

**shift_chain(chain, feedback)**
Shift chain of (LFSR/Flipflop) registers (to the right). Uses Feedback bit and returns a bitstring (flipflop register).

**bitstring_rotation_R(x,k)**
Bitrotation (right) on bitstring x (k times). Returns a bitstring.

**bitstring_rotation_L_(x,k)**
Bitrotation (left) on bitstring x (k times). Returns a bitstring.

**split_chunks(x, length, padding=True, padstring="0")**
Splits a bitstring into chunks of length. If Padding is True, pads the last chunk with the padding character padstring. Returns a list of bitstrings.

**split_half(bits)**
Splits a bitstring into two halfs. Returns a list of bitstrings (length=2).

**swap_list(l, x, y)**
Swaps two items x and y (both indices) of a list or dictionary l. Returns a list or a dictionary.

**forward_substitution(bits,sbox)**
Forward-Feed a bitstring through an S-Box. Returns a bitstring.

**reverse_substitution(bits,sbox)**
Reverse-Feed a bitstring through a bijective S-Box. Returns a bitstring.

**forward_permutation(bits,pbox)**
Forward-Feed a bitstring through a P-Box. Returns a bitstring.

**reverse_permutation(bits,pbox)**
Reverse-Feed a bitstring through a bijective P-Box. Returns a bitstring.

### Encoding and Decoding

**bits2readable(b)**
Converts a bitstring to Base64. Returns a String.

**readable2bits(b)**
Converts a Base64-String to a bitstring. Returns a bitstring.

**open_file(filename)**
Reads a File (filename) to a bitstring. Returns a bitstring.

**save_file(filename, bits)**
Writes a bitstring (bits) to a file (filename). Returns nothing.

**string2bits(string)**
Converts a UTF-8 String to a bitstring. Returns a bitstring.

**bits2string(bits)**
Converts a bitstring to a UTF-8 String. Returns a string.

**bits2list(bits)**
Converts a bitstring to a bit list. Returns a list.

**list2bits(l)**
Converts a bit list to bitstring. Returns a bitstring.

**password2key(password, keylength)**
Converts a human-readable password (password) to a key (length=keylength). Returns a bitstring.

### Random Generators

**random_bitstring(length)**
Generates a random bitstring of length. Can be used for Key or IV generation. Returns a bitstring.

**random_bijective_sbox(inputbits)**
Generates a random bijective S-Box of size inputbits. Returns a dictionary.

**random_bijective_pbox(inputbits)**
Generates a random bijective P-Box of size inputbits. Returns a list.

**random_non_bijective_sbox(inputbits,outputbits)**
Generates a random non-bijective ("one-way") S-Box mapping from n inputbits to m outputbits. Returns a dictionary.

**random_non_bijective_pbox(inputbits,outputbits)**
Generates a random non-bijective ("one-way") P-Box mapping from n inputbits to m outputbits. Returns a list.

### Cryptography

**ecb_mode(blockcipher)**
Electronic Code Book Class (initialize with a Block Cipher). Uses the encrypt(cleartext, key, blocksize) and decrypt(ciphertext, key, blocksize, paddinglength) function. encrypt() returns a tuple: ciphertext (bitstring), paddinglength (int); decrypt() returns the cleartext (bitstring).

**cbc_mode(blockcipher)**
Cipher Block Chaining Class (initialize with a Block Cipher). Uses the encrypt(cleartext, keys, iv, blocksize) and decrypt(ciphertext, key, iv, blocksize, paddinglength) function. encrypt() returns a tuple: ciphertext (bitstring), paddinglength (int); decrypt() returns the cleartext (bitstring).

**pcbc_mode(blockcipher)**
Propagating Cipher Block Chaining Class (initialize with a Block Cipher). Uses the encrypt(cleartext, keys, iv, blocksize) and decrypt(ciphertext, key, iv, blocksize, paddinglength) function. encrypt() returns a tuple: ciphertext (bitstring), paddinglength (int); decrypt() returns the cleartext (bitstring).

**cfb_mode(blockcipher)**
Cipher Feedback Class (initialize with a Block Cipher). Uses the encrypt(cleartext, keys, iv, blocksize) and decrypt(ciphertext, key, iv, blocksize, paddinglength) function. encrypt() returns a tuple: ciphertext (bitstring), paddinglength (int); decrypt() returns the cleartext (bitstring).

**ofb_mode(blockcipher)**
Output Feedback Class (initialize with a Block Cipher). Uses the encrypt(cleartext, keys, iv, blocksize) and decrypt(ciphertext, key, iv, blocksize, paddinglength) function. encrypt() returns a tuple: ciphertext (bitstring), paddinglength (int); decrypt() returns the cleartext (bitstring).

**feistel_network(roundfunction, keyschedule)**
Balanced Feistel Network Class (initialize with a round function, round function needs input data and key input, output needs to be half as long as the feistel input cleartext, init also with keyschedule to generate round keys). Uses encrypt(cleartext, key) and decrypt(ciphertext, key) function. encrypt() returns ciphertext (bitstring); decrypt(ciphertext) returns cleartext (bitstring).

**LFSR(iv)**
LFSR (linear feedback shift register) class (initialize with a set of bits). Uses shift(inputbit) function (takes a feedback input bit), state() function and output(x) function (takes an index for the output bit). shift() returns nothing. state() returns all registers as a bitstring and output returns one bit as a character ("0" or "1").

**sp_network(sboxes, pbox, keyschedule)**
Substitution-Permutation-Network class. Takes a list of sboxes and a pbox as an input as well as a keyschedule. Uses the encrypt(cleartext, key) function (returns the ciphertext bitstring) and decrypt(ciphertext, key) function (returns the cleartext bitstring). Make sure that all S-boxes together must be as big as the P-Box. The message (cleartext / ciphertext) has to be as long as the P-Box. The Key must have a multiple length of the Message / P-Box.

**davies_meyer_compression(m,H,blockcipher)**
Davies-Meyer compression function for oneway-hashing. Takes two bitstrings m (input block) and H (last Hash value or IV) and a blockcipher object. Returns a bitstring.

**matyas_meyer_oseas_compression(m,H,blockcipher)**
Matyas-Meyer-Oseas compression function for oneway-hashing. Takes two bitstrings m (input block) and H (last Hash value or IV) and a blockcipher object. Returns a bitstring.

**miyaguchi_preneel_compression(m,H,blockcipher)**
Miyaguchi-Preneel compression function for oneway-hashing. Takes two bitstrings m (input block) and H (last Hash value or IV) and a blockcipher object. Returns a bitstring.

**merkle_damgard_construction(compression_function, blockcipher)**
Merkle-Damgard Construction class. Takes a compression function and a blockcipher as inputs. Function hash(inputbits, blocksize, iv) returns a hash value of blocksize (bitstring).

**sponge_construction(round_function,  block_length, f_length)**
Sponge Construction class used in SHA-3 / Keccak. Takes round_function, block_length (bitstring) and f_length (integer, representing the input and output length of the round function). Uses two methods: hash(inputbits) generates a one-way hash; pseudorandom(seed, bitcount) generates a random number (bitstring) of length bitcount (int).

**HMAC(hash_function)**
Class for hash-based message authentication codes. Initialization with an existing Hash Function. Method authenticate(inputbits, key) takes 2 bitstrings (message and key). The authenticate method returns a bitstring (length based on the hash function output size).

### Cryptanalysis

**hamming_distance(x,y)**
Calculates the Hamming-Distance between two strings (can be bitstrings or UTF-8 Strings). Returns an integer.

**avalanche_test(x,y)**
Performs an avalanche-effect test on two strings  (can be bitstrings or UTF-8 Strings). Returns a float (percentage).
