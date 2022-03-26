# Code to run commands in windows or Linux (without Using Function)

'''

import os
import platform
import time

if platform.system()=="Windows":
	print("Clearing your screen")
	time.sleep(3)
	os.system("cls")
	print("Listing your dirs")
	time.sleep(3)
	os.system("dir")
else:
	print("Clearing your screen")
	time.sleep(3)
	os.system("clear")
	print("Listing your dirs")
	time.sleep(3)
	os.system("ls -lrt")

'''

# Using Function

import os
import time
import platform

def mycode(cmd1 , cmd2):
	print("Please wait. Clearing the screen....")
	time.sleep(2)
	os.system(cmd1)
	print("Please wait finding the list of dir and files")
	time.sleep(2)
	os.system(cmd2)
	return None

if platform.system() == "Windows":
	mycode("cls" , "dir")
else:
	mycode("clear" , "ls -lrt")