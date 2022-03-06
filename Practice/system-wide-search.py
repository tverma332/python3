# LEC 51 : Platform independent python script to do a system wide search for a file

import os
import string
import platform

req_file = input("Enter file name: ")

if platform.system() == "Windows":

	pd_name = string.ascii_uppercase
	vd_name = []
	for each_drive in pd_name:
		if os.path.exists(each_drive+":\\"):
			#print(each_drive)
			vd_name.append(each_drive+":\\")
	print(vd_name)

	for each_drive in vd_name:
		for r,d,f in os.walk(each_drive):
			for each_f in each_drive:
				if each_f == req_file:
					print(os.path.join(r,each_f))

else:
    
	for r,d,f in os.walk("/"):
		for each_file in f:
			if each_file == req_file:
				print(os.path.join(r,each_file))