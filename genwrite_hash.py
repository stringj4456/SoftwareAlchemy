#This program will allow a user to enter a string to be hashed. Once hashed, it will be stored in a dictionary.

import hashlib

stored_hashes = {}
quit_prog = False

def hash_plaintext():
    print()
    plaintext = input("Enter the string to hash: ")
    print()
    hashed = hashlib.sha256(plaintext.encode()).hexdigest()
    stored_hashes.update({plaintext: hashed})


while quit_prog == False:
    menu_option = int(input("Enter a menu option: "))

    if menu_option == 1:
        hash_plaintext()
        
    elif menu_option == 2:
        with open("file.txt", "w") as w:
            for value in stored_hashes.values():
                w.write(str(value) + "\n")

        with open("file.txt", "r") as w:
            print(w.read())

    elif menu_option == 3:
        quit_prog = True
        quit()
