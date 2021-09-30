class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    @property
    def msg(self):
        return self.name + "got grade" + self.grade

    
s1 = Student("sandeep","A")
s1.grade= "B"
print("Name: ", s1.name)
print("grade: ", s1.grade)
print(s1.msg)