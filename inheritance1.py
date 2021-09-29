class Person():

    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname

    def printDetails(self):
        print(f"First name is {self.fname} and Last name is {self.lname}")

class Student(Person):
    pass

s = Student('Sandeep','Tomar')
r = Student('Ravindra','Chouhan')

s.printDetails()
r.printDetails()