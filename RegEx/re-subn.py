# subn = Return tuple with count how many time/total replacement has occured

import re

text = "This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat = r'python[23]?'

print(re.subn(my_pat , 'javascript' , text , flags = re.I))