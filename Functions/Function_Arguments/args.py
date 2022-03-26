def get_result(num):
	result = num + 10  # parameters/positional arguments
	print(f'Your result is: {result}')
	return None

def main():
	num = eval(input("Enter you number: "))
	get_result(num) # Arguments
	return None

main()