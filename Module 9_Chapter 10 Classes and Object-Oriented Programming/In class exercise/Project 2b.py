import Project2

def changeName(c):
    c.setName('Cat')

def main():
    #penny = Coin()
    #penny.setName('Penny')
    #penny.setColor('Bronze')
    #penny.setValue(1)
    #print(penny.getName(), str(penny.getValue()), penny.getColor())

    animal1 = Project2.Animal(4,"Dog",5)
    #print(str(animal1.getLegs()), animal1.getName(), str(animal1.getAge()))
    print(animal1)
    changeName(animal1)
    print(animal1)
    print("--End--")

if __name__ == "__main__":
    main()