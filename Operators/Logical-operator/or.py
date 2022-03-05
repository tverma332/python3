# Python program to demonstrate
# logical or operator

a = 10
b = 10
c = -10

if any([a == b , 4 > 5]): # (a==b or 4 > 5)
	print("True")

else:
	print("False")