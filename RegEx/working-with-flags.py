# ---------- Working with Flags --------------

# 1) re.I/re.IGNORECASE = Makes the regular expression Case-Insensitive

'''
import re

text = "this is a string ThIs is a new starting THIS"
my_pat = r'this'

print(re.findall(my_pat,text,re.I))
'''

# 2) re.M/re.MULTILINE = ^ and  $ will match at the beginning and at the end of each line and not just at the end or beginning of the string

'''
import re

text = """this is a string
this is second line
This is third line
asfasd this"""

my_pat = r'^this'

print(re.findall(my_pat,text,re.M|re.I))
'''