# Exception Handling
* Exception is an Error
* A python progam terminates as soon as it encounters an error 
* Error are of two types in Python:
1. `Syntax Errors` : No way to handle syntax errors
2. `Run-time Errors --> Exceptions` : There is a way to handle exceptions/Runtime errors

## Catching Specific Exceptions in Python
A *try* clause can have any number of *except* clauses to handle different exceptions, however, only one will be executed in case an exception occurs.

We can use a tuple of values to specify multiple exceptions in an *except* clause. Here is an example pseudo code.
```py
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
```
![](./imgs/except.PNG)

## Python try...finally

The *try* statement in Python can have an optional *finally* clause. This clause is executed no matter what, and is generally used to release external resources.

For example, we may be connected to a remote data center through the network or working with a file or a Graphical User Interface (GUI).

In all these circumstances, we must clean up the resource before the program comes to a halt whether it successfully ran or not. These actions (closing a file, GUI or disconnecting from network) are performed in the *finally* clause to guarantee the execution.

Here is an example of file operations to illustrate this.

```py
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```

## Difference between try except else & try except finally block
`finally` will always executes and `else` only executes when there is no exception in try block
```py
try:
  a = 9
  print(a)
except NameError:
  print("Variable is not defined")
except Exception as e:
  print("Exception occured:",e)
else:
  print("This will execute if there is not exceptions in try block")
finally:
  print("This will executes always")
```