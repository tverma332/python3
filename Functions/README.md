# Functions in Python
* Block of code for some specific operation
* Function code is re-usable
* A function is a block of code which only runs when it is called
* You can pass data, known as parameters, into a function
* A function can return data as a result

> **Why we need Function** ?

* Whenever you've repetitive logic in your code then instead of repeating logic in different places , we're going to write that logic at one place and give that some name , giving name simply means defining a Fucntion.
* Code Reusability
* Improve Modularity

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

**Ex -**
```py
import os
import time
import platform

def mycode(cmd1 , cmd2):
	print("Please wait. Cleaning the screen....")
	time.sleep(2)
	os.system(cmd1)
	print("Please wait finding the list of dir and files")
	time.sleep(2)
	os.system(cmd2)
	return None

if platform.system() == "Windows":
	mycode("cls" , "dir")
else:
	mycode("clear" , "ls -lrt")
```
Let's understand it in terms of Mathematics :

`f(x) = 3x + 7`

Here :
* f = mycode
* x = cmd1 , cmd2
* 3x +7 = logic

Now you'll get answer as per the value of x , if x = 2 then <br>
f(x) = 13 if x = 1 then f(x) = 10.
