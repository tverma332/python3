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