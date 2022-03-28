class Emp(object):
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
        return None

    def display(self):
        print(f'The name is: {self.name}\nThe salary is: {self.salary}')
        return None


def main():
    emp1 = Emp("john",4343)
    emp1.display()

if __name__ == "__main__":
    main()
