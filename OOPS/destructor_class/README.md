# Destructor of a Class
* Destructors is a Method and are called when an object gets destroyed
* In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

```py
class Person(object):
    def __init__(self):
        print("An object has been created")
        return None
    def __del__(self):
        print("Object has been deleted")
        return None

per1 = Person()

OUTPUT :

An object has been created
Object has been deleted
```
