# Modules in Python
* Module is a file/python program or python script which consists of your python logic
* Modules consists of function , classes & variable

`Use` : 

1. Reusability purpose 
2. We use modules to break down large programs into small manageable and organized files

## Create a Module :

To create a module just save the code you want in a file with the file extension .py:

Save this code in a file named mymodule.py
```
def greeting(name):
  print("Hello, " + name)
```
## Use a Module :


Now we can use the module we just created, by using the import statement:

```
import mymodule
mymodule.greeting("Jonathan")
```

