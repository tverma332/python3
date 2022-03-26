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

## Function with default Arguments

```py
def display(a = 1):
	print("The value of a is : ", a)

display(4)
display()
```
```py
def add(a = 0 ,b = 0):
	result = a + b
	print(result)
	return None

add()
```

## Function with Keyword-Based Arguments

```py

def display(a,b):
	print(f'a = {a}')
	return None

display(b = 4 , a = 45)
```

## Functions with Variable length arguments

```py
def display(*arg):
	print(arg)
	return None

display(33 , 8) # Gives tuple as output
```

## Functions with variable keyword arguments

```py
def display(**karg):
	print(karg)
	return None

display(a=3,b=5) # Gives dictionary as output
```
