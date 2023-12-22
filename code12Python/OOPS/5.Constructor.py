class Employee:

    def __init__(self, name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit= subunit

    def getDetails(self):
        print(f"the name of Employee is {self.name}")
        print(f"the Salary of Employee is {self.salary}")
        print(f"The sununit of Employee is {self.subunit}")

a =Employee("sachin",200,"youtube")
a.getDetails()            



class Person:
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"Person name is{self.name} is a {self.occ}")

a=Person("sachin","Devops")
a.info()     