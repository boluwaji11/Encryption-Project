# This program creates a decryption system for text files

# Define the main function
def main():
    encryption_codes = {
        "A": "!",
        "B": "@",
        "C": "#",
        "D": "$",
        "E": "%",
        "F": "^",
        "G": "&",
        "H": "*",
        "I": "(",
        "J": ")",
        "K": "-",
        "L": "_",
        "M": "+",
        "N": "=",
        "O": "`",
        "P": "~",
        "Q": "{",
        "R": "[",
        "S": "}",
        "T": "]",
        "U": ":",
        "V": ";",
        "W": '"',
        "X": "<",
        "Y": ">",
        "Z": "0",
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "a",
        "k": "b",
        "l": "c",
        "m": "d",
        "n": "e",
        "o": "f",
        "p": "g",
        "q": "h",
        "r": "i",
        "s": "j",
        "t": "k",
        "u": "l",
        "v": "m",
        "w": "n",
        "x": "o",
        "y": "p",
        "z": "q",
    }

    # Reverse values for keys in the encryption dictionary
    # to get the decryption code
    decryption_code = {value: key for (key, value) in encryption_codes.items()}

    # Open, read and close the file to decrypt
    infile = open("encrypted_file.txt", "r")
    read_file = infile.read()
    infile.close()

    # Create and open a new file to save the decrypted file
    decrypt_file = open("decrypted_file.txt", "w")

    # Write to the new file
    for characters in read_file:
        if characters in decryption_code:
            decrypt_file.write(decryption_code[characters])
        else:
            decrypt_file.write(characters)

    print("The File has been decrypted.")


# Call the main function
main()