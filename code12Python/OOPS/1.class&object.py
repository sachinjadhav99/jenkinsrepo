# class Railwayform:
#     formtype ="Railwayform"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"train is {self.train}")

# harrapplication =Railwayform()
# harrapplication.name ="Harry"
# harrapplication.train = "train1"
# print(harrapplication.formtype)
# harrapplication.printData()        

class Student:
    class1 = "12th"
    def __init__ (self,name,age,marks):
        self.name = name
        self.age = age
        self.marks= marks

    def details(self):
        print(f"The student name is {self.name} , age : {self.age} and marks: {self.marks}")

a= Student("Yash",20, 30)
b= Student("Dipak", 30, 40)
a.details()    
b.details()
print(a.class1)        