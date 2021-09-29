class Student:
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printDetail(self):
            print(f"name is {self.name} salary is {self.salary} and role is {self.role}")
    
    def __add__(self,other):
        return self.salary + other.salary


s1 = Student("Sandeep", 500, "programmer")
s2 = Student("Koushal", 600, "Student")

print(s1.printDetail())
print(s1 + s2)
        