class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person....\n")

    def takebreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "US"
    
    def __init__(self):
        super().__init__()
        print("Initiaizating Employee..\n")

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takebreath(self):
        print("I am Employee so I am luckly breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self):
        super().__init__()
        print("Initiaizating Programmer..\n")

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
              
# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print(f"Species: {self.species}")

# Derived class inheriting from Animal
class Mammal(Animal):
    def __init__(self, species, mammal_type):
        super().__init__(species)
        self.mammal_type = mammal_type

    def show_mammal_type(self):
        print(f"Mammal Type: {self.mammal_type}")

# Further derived class inheriting from Mammal
class Dog(Mammal):
    def __init__(self, species, mammal_type, breed):
        super().__init__(species, mammal_type)
        self.breed = breed

    def show_breed(self):
        print(f"Breed: {self.breed}")

# Creating an instance of the most derived class
my_dog = Dog("Canine", "Domestic", "Labrador")

# Accessing methods from different levels of inheritance
my_dog.show_species()  # Output: Species: Canine
my_dog.show_mammal_type()  # Output: Mammal Type: Domestic
my_dog.show_breed()  # Output: Breed: Labrador
