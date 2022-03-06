# LEC 47 : Read a path and check if given path is a file or a directory

import os
path = input("Enter your path: ")

if os.path.exists(path):
	if os.path.isdir(path):
		print(f"{path} is directory")
	else:
		print(f"{path} is file")
else:
	print("Path you entered Doesn't exists")