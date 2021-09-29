# A simple class with init mathod.

class Person:

	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Sandeep')
p.say_hi()
