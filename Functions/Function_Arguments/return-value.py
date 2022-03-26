def get_addition(a,b):
	result = a + b
	return result


def main():
	a = eval(input("Enter your first number: "))	
	b = eval(input("Enter your secod number: "))
	x = get_addition(a,b)
	print(f'The addition of {a} and {b} is: {x}')
	return None

main()