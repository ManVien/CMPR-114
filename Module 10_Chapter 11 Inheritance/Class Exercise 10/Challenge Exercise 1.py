# continuing from project #1 (A), add the 3rd animal.

class AnimalType:
    def eats(self):
        print("This animal likes to eat?")

class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")

class birds(rabbits):
    def munch1(self):
        print(" seeds ")

class cows(birds):
    def munch2(self):
        print(" grasses ")

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

# here we have the Bird Object inheriting 
# from two different classes
BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()

# the Cow Object inheriting from 
# three different classes.
CowObject = AnimalType()
CowObject = cows()
CowObject.eats()
CowObject.munch2()
