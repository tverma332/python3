#--------------------------Variable---------------------------------------------

'''
class Person():
    def assign_name_and_age(self , name ,age):
        self.name = name 
        self.__age = age
        
        return None
    def display(self):
        print(self.name , self.__age)
        
        return None

per1 = Person()

per1.assign_name_and_age("john" , 32)
per1.display()
'''

#-------------------------Method-----------------------------------------------


class Person():
    def assign_name_and_age(self , name ,age):
        self.name = name 
        self.__age = age
        self.__display()
        return None
    def __display(self):
        print(self.name , self.__age)
        
        return None

per1 = Person()

per1.assign_name_and_age("john" , 32)