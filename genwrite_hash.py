#This program will allow a user to enter a string to be hashed. Once hashed, it will be stored in a dictionary.

import hashlib

stored_hashes = {}

plaintext = input("Enter the string to hash: ")
hashed = hashlib.sha256(plaintext.encode()).hexdigest()

stored_hashes.update({plaintext: hashed})
print(stored_hashes)
