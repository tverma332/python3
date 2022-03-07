# range( )

Python range( ) function returns the sequence of the given number between the given range
* Built-in function in python
* Generated integer as a list

**Python range syntax :** 
```py
range(stop)

range(start, stop, step)
```

**range() Parameters :**

range() takes mainly three arguments having the same use in both definitions:

`start` - integer starting from which the sequence of integers is to be returned

`stop` - integer before which the sequence of integers is to be returned.
The range of integers ends at stop - 1.

`step` (Optional) - integer value which determines the increment between each integer in the sequence

`NOTE : By default start = 0 | step = 1`

`range(stop)` :

* Returns a sequence of numbers starting from 0 to stop - 1

* Returns an empty sequence if stop is negative or 0