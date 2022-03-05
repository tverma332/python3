# LEC 40 : Pass string and format(title/lower/upper) as command line argument and print as per the format provided by user 

import sys

if len(sys.argv) !=3:
	sys.exit()

usr_str = sys.argv[1] 
usr_action = sys.argv[2] 

if usr_action == "title":
	print(usr_str.title())
elif usr_action == "lower": 
	print(usr_str.lower())
elif usr_action == "upper":
	print(usr_str.upper())
else:
	print("Your option is invalid. Please select valid options from this list lower/upper/title")