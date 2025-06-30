#This program will allow a user to enter a string to be hashed. Once hashed, it will be stored in a dictionary.

import hashlib

stored_hashes = {}      # Dictionary storing all of the keys and hashes
quit_prog = False       # Quit condition for the program

############################################### FUNCTIONS  ###################################################


#Menu options display function
def display_menu():
    print("1. Hash a string")
    print("2. Search for a hash")
    print("3. List all hashes")
    print("4. Write hashes to external file")
    print("5. Load hashes from external file")
    print("6. Quit the program")
    print()


#Hash generator function
def hash_plaintext():
    plaintext = input("Enter the string to hash: ")                 # Plaintext user input
    print()
    hashed = hashlib.sha256(plaintext.encode()).hexdigest()         # Hash the plaintext with sha256
    stored_hashes.update({plaintext: hashed})                       # Store the hash in the stored_hashes dict


#Hash search function
def hash_search():
    found = False                                                   # Condition on if the search is successful

    searchtext = input("Enter the string to look for: ")            # String to search for
    print()
    search_hash = hashlib.sha256(searchtext.encode()).hexdigest()
    
    #Search for the hash in the dict
    for value in stored_hashes.values():
        if search_hash == value:                                    # If the hash is found in the dict
            found = True
            print("Found!")
            print(f"The SHA256 hash for {searchtext} is: {value}")
            print()
    
    #If the hash is not found in the dict
    if found == False:
        print(f"Could not find hash for {searchtext}")
        print()


#List all keys and values function
def list_all():
    for value in stored_hashes.values():                            # Loop through stored_hashes and print everything
        print(f"{value}\n")


#Write to external file function
def write_file():
        file_name = input("Enter the file name to write to: ")      # Get the file name to write to
        print()

        with open(file_name, "w") as file:                          # Open the file, loop, and write to it
            for key, value in stored_hashes.items():
                file.write(f"{key}:{value}\n")


#Load keys and values from external file function
def load_file():
    file_name = input("Enter the file name to load: ")
    print()

    with open(file_name, "r") as file:
        file_contents = file.read()                 # Read the entire file
        key_value_list = file_contents.split()      # Split each line into a key:value string

    for values in key_value_list:                   # Loop through list of key:values
        to_split = values               
        split_values = to_split.split(":")           # Split each key:value into separate strings
        key = split_values[0]                        # Store the key
        value = split_values[1]                      # Store the value
        stored_hashes.update({key: value})           # Store the key and value in the main dict


################################################## MAIN PROGRAM ################################################

#Welcome message
print("Welcome to the GenWriteHash Program")
print()

#Main program loop
while quit_prog == False:
    display_menu()
    menu_option = int(input("Enter a menu option: "))
    print()

    #Hash a string
    if menu_option == 1:
        print("{:*^30}".format("Hashing a String"))
        print()
        hash_plaintext()
    
    #Search for a hash
    elif menu_option == 2:
        print("{:*^34}".format("Searching for a Hash"))
        print()
        hash_search()

    #List all hashes
    elif menu_option == 3:
        print("{:*^30}".format("Listing All Hashes"))
        print()
        list_all()
        
    #Write to external file
    elif menu_option == 4:
        print("{:*^40}".format("Writing to External File"))
        print()
        write_file()

    #Load from external file
    elif menu_option == 5:
        print("{:*^45}".format("Loading from External File"))
        print()
        load_file()

    #Quit the program
    elif menu_option == 6:
        print("{:*^31}".format("Exiting the Program"))
        print()
        quit_prog = True
        quit()
    
    #If an invalid menu option is selected
    else:
        print("Invalid menu option. Please enter a valid option")
        print()
