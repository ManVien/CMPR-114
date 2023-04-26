# An object is inheriting from two different classes.

class AnimalType:
    def eats(self):
        print("This animal likes to eat?")

class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")

class birds(rabbits):
    def munch1(self):
        print(" seeds ")

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

# here we have the Bird Object inheriting 
# from two different classes
BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()