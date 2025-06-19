#Letter counter. Takes in a string and will count the number of occurrences for each letter

#Variables
char = ""
stored_count = []
found_char = []

main_i = 0
char_count = 0
count = 0

#Letter count function
def count_letter(count, char):
    char_count = 0
    i = 0

    while i != len(string):
        if char in string:
            char_count += 1
        i += 1
    return char_count

string = input("Enter the string: ")

#Loop through the users string and count letter occurrences
while main_i != len(string):

    char = string[main_i]
   
    #Get the current letter of the string
    if char in found_char:
        main_i += 1
        continue
    else:
        found_char.append(char)
    
    #Count number of occurrences for the letter
    # char_count = count_letter(count, char)
    # stored_count.append(char_count)

    main_i += 1
print(found_char)
