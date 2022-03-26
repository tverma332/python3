# Python Function Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma

```py
def get_result(num):
	result = num + 10  # parameters/positional arguments
	print(f'Your result is: {result}')
	return None

def main():
	num = eval(input("Enter you number: "))
	get_result(num) # Arguments
	return None

main()
```