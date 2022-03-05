# Python program to demonstrate
# logical and operator

a = 10
b = 10
c = -10

if all([a == b , 4 > 5]): # (a==b and 4 > 5)
	print("True")

else:
	print("False")