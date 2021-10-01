class Parent():
    def first(self):
        print('Parent function')
        
class Child(Parent):
    def second(self):
        print('Child function')

object1 = Child()
object1.first()
object1.second()