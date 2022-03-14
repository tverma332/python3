# ------------ Rules to create Pattern : PART 2 ------------------------

# 9) ^(Caret) = Start of the string (and start of the line in-case of multiline string)

'''
import re

text = "it is a python and it is easy to learn"
my_pat = '^i[st]'
print(re.findall(my_pat,text))
'''

# 10) $(Dollar) = End of the string (and newline character in case of multiline string)

'''
import re

text = "it is a python and it is easy to learn"
my_pat = 'learn$'
print(re.findall(my_pat,text))
'''

# 11) \b = Empty string at the end or beginning of the word (\b treated as space in pattern)
# looking for a word 

'''
import re

text = "it is a python learn and itlearn is easy to learn"
my_pat = r'\blearn'
print(re.findall(my_pat,text))
'''

# 12) \B = Opposite to \b means no space at the beginning and ending

'''
import re

text = "it is a python learn and itlearno is easy to learn"
my_pat = r'\Blearn\B'
print(re.findall(my_pat,text))
'''

# 13) \t = Matches tab

'''
import re

text = "it is a python learn and itlearno is easy	to learn"
my_pat = r'\t'
print(re.findall(my_pat,text))
'''

# 14) \n = Matches new line

'''
import re

text = "it is a python learn and itl\nearno is easy	\n to learn"
my_pat = r'\n'
print(re.findall(my_pat,text))
'''

# 15) \r = Matches return

'''
import re

text = "it is a python learn and itlearn \ri\rs easy to learn"
my_pat = r'\r'
print(re.findall(my_pat,text))
'''