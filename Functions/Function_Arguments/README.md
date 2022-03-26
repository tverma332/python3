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
## Fucntion With Arguments and return Value

```py
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
```