# A code to recieve a uppercase and hide it's meaning then print back
# the character


# Enter a string to hide in uppercase : HIDE

# Secret Message :

# original message : HIDE

# Input "Enter a string to hide in uppercase"
secret = input('enter an upper case password: ')
print()

secret_string = ''
# Cycle through each character in the string
for char in secret:

# Store each character code in a new string
    secret_string += str(ord(char) - 23)

# Print Secret message
print('Secret message :', secret_string)
print()
# Cycle through each character in the string
secret = ''
for i in range(0, len(secret_string)-1, 2):

    # Get the 1st and 2nd for the 2 digit numbers
    char_code = secret_string[i] + secret_string[i+1]

    # Convert the code into characters and add them to a new string
    secret += chr(int(char_code) + 23)

# Print original Message
print('Original message :', secret)
