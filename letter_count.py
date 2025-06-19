#Letter counter. Takes in a string and will count the number of occurrences for each letter

#Variables
char = ""
stored_char = []
stored_count = []
found_char = []

main_i = 0
char_count = 0
inner_i = 0

#User inputs
string = input("Enter the string: ")

#Loop through the users string and count letter occurrences
while main_i != len(string):

    char = string[main_i]
    stored_char.append(char)

    while inner_i != len(string):
        if char in string:
            char_count += 1
        inner_i += 1

    print(char_count)
    main_i += 1

print(stored_char)
