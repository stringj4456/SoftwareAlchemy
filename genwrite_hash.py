#This program will allow a user to enter a string to be hashed. Once hashed, it will be stored in a dictionary.

import hashlib

stored_hashes = {}
quit_prog = False

def hash_plaintext():
    plaintext = input("Enter the string to hash: ")
    print()
    hashed = hashlib.sha256(plaintext.encode()).hexdigest()
    stored_hashes.update({plaintext: hashed})

def display_menu():
    print("1. Hash a string")
    print("2. Write the hashes to a file")
    print("3. Read from the file")
    print("4. Quit the program")
    print()

print("Welcome to the GenWriteHash Program")
print()

while quit_prog == False:
    display_menu()
    menu_option = int(input("Enter a menu option: "))
    print()

    if menu_option == 1:
        print("Hashing a String.")
        print()
        hash_plaintext()
        
    elif menu_option == 2:
        print("Writing Hashes to a File.")
        print()
        with open("file.txt", "w") as w:
            for value in stored_hashes.values():
                w.write(str(value) + "\n")

    elif menu_option == 3:
        print("Listing All Hashes.")
        print()
        with open("file.txt", "r") as w:
            print(w.read())

    elif menu_option == 4:
        print("Exiting the Program.")
        quit_prog = True
        quit()
