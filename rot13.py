"""
Simple ROT13 Encoder. Uses 1 based indexing instead of 0 based. Only supports lowercase letters
currently. Uppercase letters to be added eventually for more complexity.
"""

#Alphabet character list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Shifted letter array
shifted = []

#Get the plaintext string from the user
plaintext = list(input("Enter the string to rotate: "))
print()

#Loop through the alphabet list for each plaintext list character
for letter in plaintext:

    #Find the letter and store its index
    for index, value in enumerate(alphabet):
        if letter == value:
            found = index
            break

    #Shift the found index 13 places
    shift_index = found + 13

    #Check if the new index exceeds the alphabet list size
    if shift_index > 25:
        cycle_index = shift_index - len(alphabet)
        shifted.append(alphabet[cycle_index])
    else:
        shifted.append(alphabet[shift_index])

#Join and print the shifted letters
output = "".join(shifted)
print(f"Your shifted string is: {output}")
