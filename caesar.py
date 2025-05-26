#Simple Caesar Cipher. Supports lowercase, uppercase, and space characters

#List of characters
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

shifted = []    # Store the shifted letters

#Take in inputs
plaintext = list(input("Enter the string to shift: "))
shift = int(input("Enter the shift value: "))

plain_index = 0     # Plaintext list index

#Loop through the plaintext word
for letter in plaintext:

    #Space character
    if letter == " ":
        shifted.append(plaintext[plain_index])
        continue

    #Lowercase letters
    if letter in lower:
        shift_index = lower.index(letter) + shift   # Calculate the shift index
        if shift_index > 26:                        # Wrap around if the shift exceeds length of list
            shift_index = shift_index % 26  
        shifted.append(lower[shift_index])          # Append the new character to the output list

    #Uppercase characters
    if letter in upper:
        shift_index = upper.index(letter) + shift
        if shift_index > 26:
            shift_index = shift_index % 26
        shifted.append(upper[shift_index])

    plain_index += 1    # Increment through the plaintext list

# Join the shifted letters together and print
output = "".join(shifted)
print()
print(f"Your shifted string is {output}")

