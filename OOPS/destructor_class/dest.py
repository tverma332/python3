class Person(object):
    def __init__(self):
        print("An object has been created")
        return None
    def __del__(self):
        print("Object has been deleted")
        return None

per1 = Person()