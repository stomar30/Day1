class Student:
    def __init__(self,name,marks):

        self.marks = marks
        self.name = name

    def msg(self):
        print(f"{self.name} got {self.marks} marks")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100)) 

s1 = Student("sandeep","95")
marks = "566"
name = "Pradeep"

s2 = Student.get_per(name,marks)
s2.msg()