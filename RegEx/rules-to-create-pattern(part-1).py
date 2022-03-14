# ------------------------------------ Rules to create a Pattern ---------------------------------------------------

# 1) a,x,9 = Ordinary character that match themselves

'''
import re

text = "This is a python and it is easy to learn"
my_pat = "a" 

print(re.findall(my_pat,text))
'''

# 2) [abc] = a or b or c

'''
import re

text = "This is a python and it is easy to learn"
my_pat = "[abc]" 

print(re.findall(my_pat,text))
'''

# 3) [a-fh-jx-z] <==> [abcdefhijxyz] 
# ==> [a-zA-Z0-9] = Matches any letter from (a to z) or (A to Z) or (0 to 9)


'''
import re

text = "This is a python and it is easy to learn"
my_pat = "[a-d]" 

print(re.findall(my_pat,text))
'''

# 4) \w = Matches any single letter , digit or underscore <==> [a-zA-Z0-9_]

'''
import re

text = "This is a python and it is easy to learn"
my_pat = "\w" 

print(re.findall(my_pat,text))
'''

# 5) \W = Matches any character not part of \w

'''
import re

text = "This is a python and it is easy to learn"
my_pat = "\W" 

print(re.findall(my_pat,text))
'''

# 6) \d = Matches decimal digit 0-9

'''
import re

text = "This is a python9 and it is easy to learn"
my_pat = "python\d" 

print(re.findall(my_pat,text))
'''

# 7) . = Matches any single character except newline character(\n)

'''
import re

text = "This is a python9 and it is easy to learn"
my_pat = "." 

print(re.findall(my_pat,text))
'''

# 8) \ = Makes sure character is not treated as special 

'''
import re

text = "This is a python9 and it is easy to learn."
my_pat = "\." 

print(re.findall(my_pat,text))
'''

'''
import re

text = "This is my ip of a db server : 255.100.102.103"
my_pat = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d" 

print(re.findall(my_pat,text))
'''