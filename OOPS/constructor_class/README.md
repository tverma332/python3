# Constructor of a Class
* A constructor is a special method that is called by default whenever you create an object from a class
* Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created
* Means anything you define in __init__ method it will display even if we're not calling that

```py
class Emp:
    def __init__(self):
        print("This is a init method")
        return None

emp1 = Emp()
emp2 = Emp()

OUTPUT : 

This is a init method
This is a init method
```