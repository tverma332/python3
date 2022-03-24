# re.match() = Match will look only at the 0th index position (Even in multiline it will look only at 0th index) 

import re

text = "python is for python3 and there are two mahor vers python2 and python3 in future python4"

my_pat = r'\bpython\d?\b'
match_ob = re.match(my_pat , text)

if match_ob :
	print(f"Match from your pattern : {match_ob.group()}")
	print(f"Starting Index : {match_ob.start()}")
	print(f"Ending Index : {match_ob.end() - 1}")
	print(f"Length : {match_ob.end() - match_ob.start()}")
else :
	print("No Match F-ound")