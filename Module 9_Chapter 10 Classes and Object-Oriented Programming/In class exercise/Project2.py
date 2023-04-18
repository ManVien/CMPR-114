class Animal(object):
    def __init__(self,legs,name,age):
        self.__legs = legs
        self.__name = name
        self.__age = age

    def __str__(self):
        return str(self.__legs) + " , " + self.__name + " , " + str(self.__age)

    def setLegs(self,l):
        self.__legs = l

    def getLegs(self):
        return self.__legs

    def setName(self,n):
        self.__name = n

    def getName(self):
        return self.__name

    def setAge(self,a):
        self.__age = a

    def getAge(self):
        return self.__age

