
class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def n(self):
		print("In Class2")


class Class3(Class2, Class1):
	def o(self):
		print("In Class3")
	
obj = Class3()
obj.m()
obj.n()
obj.o()
