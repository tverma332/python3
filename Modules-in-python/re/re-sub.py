# sub = substitution of given pattern

import re

text = "This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat = r'python[23]?'

print(re.sub(my_pat , 'javascript' , text , count = 2 , flags = re.I)) # count number represents the number of subtitution takes place irrespective of the numbers of pattern present in text