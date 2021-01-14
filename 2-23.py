#!/usr/bin/env python3
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = int(sys.argv[1])
b = int(sys.argv[2])
message = sys.argv[3]

def encrypt(a, b, message):
    cyphertext = ""

    for c in message:
        n = ord(c)- 97
        new_char = (a * n + b) % 26
        cyphertext += chr(new_char + 97)
    
    return cyphertext

def decrypt(a, b, message):
    plaintext = ""

    for c in message:
        n = ord(c)- 97
        new_char = (a*n - b) % 26
        plaintext += chr(new_char + 97)

    return plaintext

encrypted = encrypt(a, b, message)
print(encrypted)
print(decrypt(a, b, encrypted))