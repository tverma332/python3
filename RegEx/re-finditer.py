# re.finditer() = Return iterator object in string

import re

text = "This is python and we are having python2 and python3 version"
my_pat = r'\bpython[23]?\b'
match_ob = re.finditer(my_pat,text)

for each_ob in re.finditer(my_pat , text) :
	print(f" The match is : {each_ob.group()} , Starting Index : {each_ob.start()}" )