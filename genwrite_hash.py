#This program will allow a user to enter a string to be hashed. Once hashed, it will be stored in a dictionary.

import hashlib

stored_hashes = {}
quit_prog = False

#Menu options display function
def display_menu():
    print("1. Hash a string")
    print("2. Write the hashes to a file")
    print("3. Read from the file")
    print("4. Search for a hash")
    print("5. Quit the program")
    print()

#Hash generator function
def hash_plaintext():
    plaintext = input("Enter the string to hash: ")
    print()
    hashed = hashlib.sha256(plaintext.encode()).hexdigest()
    stored_hashes.update({plaintext: hashed})

#Hash search function
def hash_search():
    found = False

    searchtext = input("Enter the string to look for: ")
    print()
    search_hash = hashlib.sha256(searchtext.encode()).hexdigest()
    
    #Search for the hash in the dict
    for value in stored_hashes.values():
        if search_hash == value:
            found = True
            print("Found!")
            print(f"The SHA256 hash for {searchtext} is: {value}")
            print()
    
    #If the hash is not found in the dict
    if found == False:
        print(f"Could not find hash for {searchtext}")
        print()

def load_file():
    with open("file.txt", "r") as file:
        file_contents = file.read()
        file_lines = file_contents.split()
        print(file_lines)

load_file()

#Welcome message
print("Welcome to the GenWriteHash Program")
print()


#Main program loop
while quit_prog == False:
    display_menu()
    menu_option = int(input("Enter a menu option: "))
    print()

    #Hashing menu option
    if menu_option == 1:
        print("Hashing a String.")
        print()
        hash_plaintext()
        
    #Write menu option
    elif menu_option == 2:
        print("Writing Hashes to a File.")
        print()
        with open("file.txt", "w") as file:
            for value in stored_hashes.values():
                file.write(str(value) + "\n")

    #Read menu option
    elif menu_option == 3:
        print("Listing All Hashes.")
        print()
        with open("file.txt", "r") as file:
            print(file.read())

    #Search for a hash
    elif menu_option == 4:
        print("Searching for a hash.")
        print()
        hash_search()

    #Quit program menu option
    elif menu_option == 5:
        print("Exiting the Program.")
        print()
        quit_prog = True
        quit()
