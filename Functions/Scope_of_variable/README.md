# Scope of Variable

* The location where we can find a variable and also access it if required is called the scope of a variable
* A variable is only available from inside the region it is created. This is called scope

## Local Scope

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function
```py
def myfunc():
  x = 300
  print(x)

myfunc()
```

### Function Inside Function

As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
```py
The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
```

## Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local

```py
A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
```

## Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global

```py
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

def main():
	global x
	x = 10 # This is global variable
	myfunction1()

main()

# NOTE : IF we don't use global x in main() then x would also be considered as local variable
```