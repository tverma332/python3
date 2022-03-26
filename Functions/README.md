# Functions in Python
* Block of code for some specific operation
* Function code is re-usable
* A function is a block of code which only runs when it is called
* You can pass data, known as parameters, into a function
* A function can return data as a result

> **Why we need Function** ?

Whenever you've repetitive logic in your code then instead of repeating logic in different places , we're going to write that logic at one place and give that some name , giving name simply means defining a Fucntion.

## Defining a Funcion
In Python a function is defined using the `def` keyword , def is short for *define*. 

`Syntax` : def functionname(parameter):
```py
def mycode():
  print("This is first line")
```
## Calling a Function
To call a function, use the function name followed by parenthesis
```py
def mycode():
  print("This is first line")

mycode()
```

## Rules to Define Function Name
1. Function name should have only a-z , A-Z , 0-9 , _
2. It should not start with number but can start with _
3. Don't include any space
4. Function must be define before calling it
