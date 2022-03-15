# re.compile = Python's re.compile() methos is used to compile a regular expression pattern provided as a string into a regex pattern object.
# re.findall(my_pat , text) <===> re.compile(my_pat).findall(text)

import re

text = "This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat = r'\bpython[23]?\b'

pat_ob = re.compile(my_pat , flags = re.I) # it also supports flags

print(pat_ob.search(text))
print(pat_ob.findall(text))
