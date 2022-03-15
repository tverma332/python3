# split = split the text based on pattern

import re

text = "This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat = r'python[23]'

print(re.split(my_pat , text , maxsplit = 1 , flags = re.I)) # maxsplit split based on number supplied from left to right irrespective of the numbers of pattern present in text