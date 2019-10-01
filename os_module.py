import os

# Lets create amodule to icrinp and decrypt a file

def encrypt(file):
    encoded_file = os.fsencode(file)
    return encoded_file
    # encrypt some file
    # return siad incripted file

def decrypt(file):
    decoded_file = os.fsdecode(file)
    return decoded_file
    # decript file
    # return decrypted files