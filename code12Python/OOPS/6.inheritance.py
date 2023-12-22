class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language = "Python"
    company= "Youtube"

    def getlanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

a= Employee()
a.showDetails()
c=Programmer()
c.getlanguage()
c.showDetails()
print(a.company)

