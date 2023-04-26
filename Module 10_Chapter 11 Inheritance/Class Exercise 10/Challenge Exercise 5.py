# The Insect class is the main or the superclass.
class Insect:
    def __init__(self, species, color):
        self.__species = species
        self.__color = color

    def get_species(self):
        return self.__species

    def get_color(self):
        return self.__color

# The Bumblebee is a subclass of the Insect class.
class Bumblebee(Insect):
    def __init__(self, species, color, sting):
        super().__init__(species, color)
        self.__sting = sting

    def set_sting(self, sting):
        self.__sting = sting

    def get_sting(self):
        return self.__sting
     
# The Grasshopper is a subclass of the Insect class.
class Grasshopper(Insect):
    def __init__(self, species, color, jump):
        super().__init__(species, color)
        self.__jump = jump

    def set_jump(self, jump):
        self.__jump = jump

    def get_jump(self):
        return self.__jump

def main():
    # display characteristics of bumblebee.
    bee = Bumblebee("Bumblebee", "yellow and black", "sting")
    print("Insect Name: ", bee.get_species())
    print("Insect Color: ", bee.get_color())
    print("Insect Ability: ", bee.get_sting())
    print("\n")

    # display characteristics of grasshopper.
    grasshopper = Grasshopper("Grasshopper", "green", "jump")
    print("Insect Name: ", grasshopper.get_species())
    print("Insect Color: ", grasshopper.get_color())
    print("Insect Ability: ", grasshopper.get_jump())

main()