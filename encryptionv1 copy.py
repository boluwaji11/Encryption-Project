import CodeGeneratorClass as cg

code = cg.CodeGenerator()

code.generate_code()
# Open, read and close the file to encrypt
infile = open("info_security.txt", "r")
read_file = infile.read()
infile.close()

# Create and open a new file to save the encrypted file
encryption_file = open("test.txt", "w")

# Write to the new file
for characters in read_file:
    if characters in code.get_code():
        encryption_file.write(code.get_code()[characters])
    else:
        encryption_file.write(characters)