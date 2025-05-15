"""
Simple ROT13 Encoder. For this first instance, only the first character can be
successfully shifted. Uses 1 based indexing not 0 based.
"""

#Alphabet character list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Get the plaintext string from the user
plaintext = list(input("Enter the string to rotate: "))
print()
first = plaintext[0]

#Find the first letter of the plaintext in the alphabet list
for index,value in enumerate(alphabet):
    if first == value:
        found = index
        break

#Shift the found index 13 places
shift_index = found + 13

#Check if the new index exceeds the alphabet list size
if shift_index > 25:
    cycle_index = shift_index - len(alphabet)
    shifted = alphabet[cycle_index]

    #Test prints
    print(f"Original Value: {first}")
    print(f"Original Index: {found}")
    print()
    print(f"Shifted Index: {cycle_index}")
    print(f"Shifted Value: {shifted}")
else:
    shifted2 = alphabet[shift_index]

    #Test prints
    print(f"Original Value: {first}")
    print(f"Original Index: {found}")
    print()
    print(f"Shifted Index: {shift_index}")
    print(f"Shifted Value: {shifted2}")
