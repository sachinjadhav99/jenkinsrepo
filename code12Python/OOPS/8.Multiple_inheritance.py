class Employee:
    def __init__(self,name):
        self.name=name

    def show1(self):
        print(f"The name is {self.name}")  

class Dancer:
    def __init__(self, dance):
        self.dance=dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, name,dance):
        self.name= name
        self.dance=dance

a = DancerEmployee("Kathak", "shivani")
print(a.name)
print(a.dance)                    
a.show1()              
a.show()

