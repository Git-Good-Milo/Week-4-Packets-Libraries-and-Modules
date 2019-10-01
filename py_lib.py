# Import random

from random import random, randrange
# This is considered best practise. You can use 'from random import *' but it can lead to intesive computation time

from time import *
from math import *

print("/////////////RanDOm////////////")
sleep(2)
print(random())
sleep(2)
print(randrange(10, 44))
sleep(1)

# LIbraries
# They come built in
# You just need to import them

# They are maintained by python organisation
# They are very stable and considered vanilla python
# Check the documentaion for more
#  https://docs.python.org/3/library/
print("/////////MAths////////")
num = 24.64

print(ceil(num))
sleep(2)
print(floor(num))