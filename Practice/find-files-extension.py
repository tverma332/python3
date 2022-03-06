# LEC 51 : Find all the files in a directory with extension .py/.txt/.sh etc

import os

req_path=input("Enter your directory path: ")


if os.path.isfile(req_path):
	print(f"The given path is {req_path} is a file. Please pass only directory path")
else:
	all_f_ds = os.listdir(req_path)
	if len(all_f_ds) == 0:
		print(f"the {req_path} is an empty path")
	else:
		req_ext = input("your path is valid please enter ext like .py .txt: ")
		req_files = []
		for each_f in all_f_ds:
			if each_f.endswith(req_ext):
				req_files.append(each_f)  
		if len(req_files) == 0:
			print(f"There are no {req_ext} files in location {req_path}")
		else:
			print(f"There are {len(req_files)} files in location of {req_path}")
			print(req_files)
