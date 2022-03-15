# --------------- Rules to create Pattern PART - 3 ----------------------

# 16) {2} = exactly 2 times | Reduce repetition for writing

'''
import re

text = "This is a pythonnnn and python3"
my_pat = r'\bpython{4}\b'

print(re.findall(my_pat,text))
'''

# 17) {2,4} = 2 , 3 or 4 times

'''
import re

text = "xaz asdfa sdf xaazz xaaaaaaz xaaaz"
my_pat = r'\bxa{1,4}z\b'

print(re.findall(my_pat,text))
'''

# 18) {2,} = two or more times

'''
import re

text = "xaz asdfa sdf xaazz xaaaaaaz xaaaz"
my_pat = r'\bxa{2,}z\b'

print(re.findall(my_pat,text))
'''

# 19) + <==> {1,} = one or more times

'''
import re

text = "xaz asdfa sdf xaaz xaaaaaaz xaaaz"
my_pat = r'\bxa+z\b'

print(re.findall(my_pat,text))
'''

# 20) * <==> {0,} = 0 or more times

'''
import re

text = "xaz asdfa sdf xaaz xaaaaaaz xaaaz xz"
my_pat = r'\bxa*z\b'

print(re.findall(my_pat,text))
'''

# 21) ? = once or none(lazy)

'''
import re

text = "xaz asdfa sdf xaaz xaaaaaaz xaaaz xz"
my_pat = r'\bxa?z\b'

print(re.findall(my_pat,text))
'''