# LEC 44 : Write a platform independent script to clear terminal

import os
import platform

my_os = platform.system()

if my_os == "Windows":
	os.system("cls")
else:
	os.system("clear")