import hashlib
import string
from itertools import product
import string

cheese_list = open("cheese_list.txt")

target_hash = input()

def encrypt(text):
    text = text.strip()
    encrypted_text = hashlib.sha256(text).hexdigest()
    if target_hash == encrypted_text:
        print (text)
        return
for line in cheese_list:
    line = line.encode()
    for s in range(256):
        for i in range(len(line) + 1):
            text = line[:i] + bytes([s]) + line[i:]
            encrypt(text)
            text = line[:i].lower() + bytes([s]) + line[i:].lower()
            encrypt(text)
            text = line[:i].upper() + bytes([s]) + line[i:].upper()

'''
for line in cheese_list:
    line = line.strip()
    for s in string.printable:
        for i in range(len(line) + 1):
            text = line[:i] + s + line[i:]
            encrypt(text.encode())
            text = line[:i].lower() + s + line[i:].lower()
            encrypt(text.encode())
            text = line[:i].upper() + s + line[i:].upper()
            encrypt(text.encode())
'''