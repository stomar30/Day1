# Instance and Class variables.

class Dog:
    animal = 'dog'  # class variable

    def __init__(self,breed,color):

        self.breed = breed          # Instance variable
        self.color = color
    
    def DogDetails(self):
        print(f"Breed is {self.breed} and color is {self.color}")

tommy = Dog('pug','brown')
bruno = Dog('bulldog','black')

tommy.DogDetails()
bruno.DogDetails()