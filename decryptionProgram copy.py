import CodeGeneratorClass as cg

code = cg.CodeGenerator()

encryption_codes = code.get_code()

# Reverse values for keys in the encryption dictionary
# to get the decryption code
decryption_code = {value: key for (key, value) in encryption_codes.items()}

# Open, read and close the file to decrypt
infile = open("test.txt", "r")
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