# class Employee:
#     def __init__(self, name, id):
#         self.name=name
#         self.id =id

#     def showDetails(self):
#         print(f"The name of Employee: {self.name} is {self.id}")

# class Programmer(Employee):
#     def showlanguages(self):
#         print("The Defualt language is Python")

# e1=Employee("Tejas", 200)
# e1.showDetails()
# e2=Programmer("Abhi", 300)
# e2.showDetails()
# e2.showlanguages()


class animal:
    def __init__(self,name,species):
        self.name =name
        self.species= species

    def make_sound(self):
        print("Sound made by the animal") 

class Dog(animal):
    def __init__(self,name,bread):
        animal.__init__(self,name,species="Dog") 
        self.bread=bread

    def make_sound(self):
        print("Bark")

a= animal("Tomy", "Dog")
a.make_sound()

a= Dog("GOG", "Dog")
a.make_sound()
              