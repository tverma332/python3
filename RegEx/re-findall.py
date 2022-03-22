# 1) findall = findall() module is used to search for “all” occurrences that match a given pattern

import re

text = "This is a python and it is easy to learn"
my_pat = "is"

print(re.findall(my_pat,text))

print(len(re.findall(my_pat,text))) # number of occurence using len function 

# NOTE : We're not searching for words but string (Pattern represents strings)