#Letter counter. Takes in a string and will count the number of occurrences for each letter

#The program works by cycling through the entered string character by character. If a character has not yet been encountered,
#the program will store that letter in found_char for future reference. If encountered again, the program will skip the next 
#occurrences of the letter. This ensures each unique letter is handled only once.

#Counting will then be performed for the character. Counts are stored in stored_count list. This helps to ensure a 1 to 1 mapping
#of characters and their respective counts

#Variables
char = ""               #Stores a single character of the string
stored_count = []       #Stores the counts of each letter
found_char = []         #Stores each letter of the entered string

#Loop indexes
main_i = 0 
print_i = 0

#Letter count function
def count_letter(char):
    char_count = 0
    i = 0

    while i != len(string):
        if char == string[i]:   #Check if char is equal to the current string index
            char_count += 1     #Add 1 to the character count if a match occurs
        i += 1

    return char_count

#User string input
string = input("Enter the string: ")

#Main loop. Loop through the users string
while main_i != len(string):
    
    char = string[main_i]   #Get the current letter of the string
    
    if char == " ":         #If a space is encountered then skip it
        main_i += 1
        continue

    if char in found_char:  #Check if the letter has already been found
        main_i += 1
        continue
    else:
        found_char.append(char) #If the letter has not yet been found, add it to found char list
    
    char_count = count_letter(char)     #Count the number of occurrences for the letter
    stored_count.append(char_count)     #Add the count to the stored_count list

    main_i += 1

#Display the results of the count
print()
for char in found_char:
    current_char = found_char[print_i]      #Get all characters in found_char
    current_count = stored_count[print_i]   #Get all counts in stored_char

    print(f"Occurrences for {current_char}: {current_count}") #Print the results of all counts
    print_i += 1
