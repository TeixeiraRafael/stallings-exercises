#!/usr/bin/env python3
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
rotation = int(sys.argv[1])
message = sys.argv[2]

def encrypt(message):
    cyphertext = ""

    for c in message:
        n = ord(c)- 97
        new_char = (n + rotation) % 26
        cyphertext += chr(new_char + 97)
    
    return cyphertext

def decrypt(message):
    plaintext = ""

    for c in message:
        n = ord(c)- 97
        new_char = (n - rotation) % 26
        plaintext += chr(new_char + 97)
    
    return plaintext

encrypted = encrypt(message)
print(encrypted)
print(decrypt(encrypted))