from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def printArea(self):
        pass

class Rectangle(Shape):

    def __init__(self,bredth,length):
        self.bredth = bredth
        self.length = length

    def printArea(self):
        return self.bredth*self.length

class Circle(Shape):

    def __init__(self,r):
        self.r = r

    def printArea(self):
        return (22/7)*self.r*self.r

r = Rectangle(6,8)
c = Circle(7)

print(r.printArea())
print(c.printArea())