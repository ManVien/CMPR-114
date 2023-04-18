class Coin:
    def __init__(self,name,color,val):
        self.__color = color
        self.__name = name
        self.__val = val

    def __str__(self):
        return self.__name + " , " + self.__color + " , " + str(self.__val)

    def setValue(self,v):
        self.__val = v

    def getValue(self):
        return self.__val

    def setColor(self,c):
        self.__color = c

    def getColor(self):
        return self.__color

    def setName(self,n):
        self.__name = n

    def getName(self):
        return self.__name

def main():
    #penny = Coin()
    #penny.setName('Penny')
    #penny.setColor('Bronze')
    #penny.setValue(1)
    #print(penny.getName(), str(penny.getValue()), penny.getColor())

    nickle = Coin("Nik","Silver",5)
    #print(nickle.getName(), str(nickle.getValue()), nickle.getColor())
    print(nickle)
    print("--End--")

if __name__ == "__main__":
    main()