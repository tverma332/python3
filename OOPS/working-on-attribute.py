class emp:
    count = 0
    def get_name_age_salary(self,name,age,salary):
        self.name = name 
        self.age = age
        self.salary = salary
        #self.display_details()
        self.increase_count()
        return None
    def increase_count(self):
        emp.count = emp.count + 1
        
        return None
    def display_details(self):
        print(f'The name is {self.name}\nThe age is {self.age}\nThe salary is {self.salary}')
        return None

def main():
    emp1 = emp()
    emp2 = emp()

    emp1.get_name_age_salary("JOhn",33,54000)
    emp2.get_name_age_salary("ok",45,454545)

    print(emp.count)
 


if __name__ == "__main__":
   main()