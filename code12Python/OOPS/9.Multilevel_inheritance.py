# class Animal:
#     def __init__(self,name,species):
#         self.name= name
#         self.species=species

#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"species: {self.species}")

# class Dog(Animal):
#     def __init__(self,name,bread):
#         Animal.__init__(self,name,species="Dog") 
#         self.bread = bread

#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Bread: {self.bread}") 

# class GoldenRetriever(Dog):
#     def __init__(self,name,color):
#         Dog.__init__(self,name,bread="Rotvilar")
#         self.color=color

#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = GoldenRetriever("Tommy" , "Black")  
# o.show_details()     


class Person:
    country = "India"
    def takebreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "US"

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takebreath(self):
        print("I am Employee so I am luckly breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getsalary(self):
        print(f"No salary to Programmers")

    def takebreath1(self):
        print("I am a Programmer so I am breathing..")

p = Person()
p.takebreath()

q =Employee()
q.takebreath()

r = Programmer()
r.takebreath()
              
