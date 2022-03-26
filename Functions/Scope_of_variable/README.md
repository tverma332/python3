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