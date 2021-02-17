# This program creates an encryption system for text files
import random

# Define the main function
def main():
    code_generator()
    encryption(code_generator())
    decryption(code_generator())


# Define the code generator function
def code_generator():
    # Using ASCII characters as the code for encryption
    FIRST_ASCII = 33
    LAST_ASCII = 126

    code_values = list(range(FIRST_ASCII, LAST_ASCII + 1))

    # Randomize the list of code values
    code_values = random.sample(code_values, len(code_values))

    # Create empty dictionary to hold the encryption codes
    encryption_codes = {}
    for i in range(len(code_values)):
        encryption_codes[chr(i + FIRST_ASCII)] = chr(code_values[i])

    # Return dictionary of encryption code
    return encryption_codes


# Define the encryption function
def encryption(encryption_codes):

    # Open, read and close the file to encrypt
    infile = open("info_security.txt", "r")
    read_file = infile.read()
    infile.close()

    # Create and open a new file to save the encrypted file
    encryption_file = open("encrypted_file_1.txt", "w")

    # Write to the new file
    for characters in read_file:
        if characters in encryption_codes:
            encryption_file.write(encryption_codes[characters])
        else:
            encryption_file.write(characters)


def decryption(encryption_codes):

    # Open, read and close the file to decrypt
    infile1 = open("encrypted_file_1.txt", "r")
    read_file_1 = infile1.read()
    infile1.close()

    # Reverse values for keys in the encryption dictionary
    # to get the decryption code
    decryption_code = {value: key for (key, value) in encryption_codes.items()}

    # Create and open a new file to save the decrypted file
    decrypt_file = open("decrypted_file_1.txt", "w")

    # Write to the new file
    for characters in read_file_1:
        if characters in decryption_code:
            decrypt_file.write(decryption_code[characters])
        else:
            decrypt_file.write(characters)


# Call the main function
# main()