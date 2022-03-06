# Identity Operator

In Python identity operators are used to determine whether a value is of a certain class or type. They are usually used to determine the type of data a certain variable contains. 
There are different identity operators such as 

1. ‘is’ operator – Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
```py
# Python program to illustrate the use
# of 'is' identity operator
x = 5
if (type(x) is int):
	print("true")
else:
	print("false") 

```
`OUTPUT` : True

2. ‘is not’ operator – Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
```py
# Python program to illustrate the
# use of 'is not' identity operator
x = 5.2
if (type(x) is not int):
	print("true")
else:
	print("false")

```
`OUTPUT` : True