class Employee:
    company = "Google"

    def getsalary(self, signature):
        print(f"Salary of this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Mornig,Sir")

    @staticmethod
    def time():
        print(f"The time is 9AM in the Morning")

harry = Employee()
harry.salary = 100
print(harry.company)
harry.getsalary("Thanks!")
harry.greet()
harry.time()
 