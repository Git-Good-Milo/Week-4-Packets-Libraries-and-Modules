# From os_module import *
from os_module import encrypt, decrypt

x_files = encrypt("README.md")
print (x_files)

de_classifeid_x_files = decrypt(x_files)
print(de_classifeid_x_files)