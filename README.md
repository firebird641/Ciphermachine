# Ciphermachine
A python-based cryptographic library. Helps you to construct modern symmetric encryption algorithms and hash functions. 

## Importing the Modules
~~~python
import ciphermachine.bit_operations as o # contains binary operation functions
import ciphermachine.data_encoding as e # contains encoding functions for data
import ciphermachine.random_generators as g # contains generators (like keys, sboxes, pboxes, ...)
import ciphermachine.crypto_constructors as c # contains cryptographic functions
import ciphermachine.crypto_analytics as a # contains cryptoanalytic functions
~~~

## List of features
### Cryptographic Functions
- Blockcipher-Modes
	- Electronic Code Book
	- Cipher Block Chaining
	- Propagating Cipher Block Chaining
	- Cipher Feedback
	- Output Feedback
- Substitution-Permutation Network
- Feistel-Network
- Linear Feedback Shift Register
- Keccak-F-Function
- Davies Meyer Compression
- Matyas Meyer Oseas Compression
- Miyaguchi Preneel Compression
- Merkle-Damgard Construction
- Sponge Construction
- Hash-Based Message Authentication Codes
- SP-Network
### Cryptoanalytic Functions
- Avalanche Effect
- Hamming-Distance
### Bit/Data Operation Functions
- XOR on Bitstrings
- XOR (Modulo-2-Addition) on a list of bits
- AND on Bitstrings
- NOT Bitstring
- Shift Chain (Flipflops, right direction)
- Bit Rotation (right)
- Bit Rotation (left)
- Split Bitstring into Chunks (optional Padding)
- Split Bitstring into two Halfs
- Swap list items
- Forward Feed Bits through a S-Box
- Reverse Feed Bits through a bijective S-Box
- Forward Feed Bits through a P-Box
- Reverse Feed Bits through a bijective P-Box
### Encoding Functions
- Bits to Readable
- Readable to Bits
- Open File as Bit String
- Save File from Bit String
- UTF-8 String to Bitstring
- Bitstring to UTF-8 String
- Bitstring to Bit List
- Bit List to Bitstring
- Human-Readable Password to Key
### Generator Functions
- Random Bitstring (e.g for Keys and Initialization Vectors)
- Random Substitution-Box (bijective)
- Random Permutation-Box (bijective)
- Random Substitution-Box (non-bijective)
- Random Permutation-Box (non-bijective)

