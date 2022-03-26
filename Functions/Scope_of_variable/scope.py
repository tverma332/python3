def myfunction1():
	x = 60 # This is local variable
	print("Welcome to Fucntions")
	print("x value from func1: ", x)
	myfunction2()
	return None

def myfunction2():
	print("Thank you!!")
	print("x value form fucn2:", x)
	return None

x = 10 # This is global variable
myfunction1()

# Note : Priority is given to Local variable
'''
def myfunction1():
	x = 60 # This is local variable
	print("Welcome to Fucntions")
	print("x value from func1: ", x)
	def myfunction2():
		print("Thank you!!")
		print("x value form fucn2:", x)
	myfunction2()
	return None


x = 10 # This is global variable
myfunction1()
'''