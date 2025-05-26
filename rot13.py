"""
Simple ROT13 Encoder. Uses 1 based indexing instead of 0 based. Only supports lowercase letters
currently. Now supports spaces.
"""

#Alphabet character list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Shifted letter array
shifted = []

#Get the plaintext string from the user
plaintext = list(input("Enter the string to rotate: "))
print()

#Plaintext index
plaintext_i = 0

#Loop through the alphabet list for each plaintext list character
for letter in plaintext:
    if letter == " ":           #If a space is encountered
        shifted.append(plaintext[plaintext_i])
        plaintext_i += 1
        continue                #End this iteration and goto the next
        
    #Find the letter and store its index
    for index, value in enumerate(alphabet):
        if letter == value:     #If a match is found
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

    plaintext_i += 1    #Increment plaintext index

#Join and print the shifted letters
output = "".join(shifted)
print(f"Your shifted string is: {output}")
