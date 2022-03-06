# LEC 48 : Read a directory path and identify all files and directory

import os

path = input("Enter your path: ")

if os.path.exists(path):
	for x in os.listdir(path):
		f_d_p = os.path.join(path,x)
		if os.path.isdir(f_d_p):
			print(f"{os.path.join(path,x)} is directory")
		else:
			print(f"{os.path.join(path,x)} is file")
else:
	print("Path your Entered Doesn't exists")