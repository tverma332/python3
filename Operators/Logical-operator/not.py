# Python program to demonstrate
# logical not operator

a = 10


if not (a%3 == 0 or a%5 == 0):
	print("10 is not divisible by either 3 or 5")
else:
	print("10 is divisible by either 3 or 5")
