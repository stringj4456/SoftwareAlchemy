# Letter counter. Takes in a string and will count the number of occurrences for each letter

#User inputs
string = input("Enter the string: ")
char = input("Enter the letter to count: ")

char_count = 0

#Loop through the users string and count letter occurrences
for letter in string:
    if char == letter:
        char_count += 1

#Print the output
print()
print(f"Occurences of {char}: {char_count}")
