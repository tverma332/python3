# LEC 49 : Python program to check if the number is odd or even

my_list = [23,453,76,675,46,7,0]

for each in my_list:
	rem = each % 2
	if rem == 0:
		print(f"{each} is even")
	else:
		print(f"{each} is odd")