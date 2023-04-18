# Continue project # 2, add a second object for Teacher2 
# and add any teacher name, room #, and course assigned.

class Teacher:
    # using init to create a customized constructor
    # here we have three arguments
    def __init__(self, name, classRoom, course):
        self.name = name
        self.classRoom = classRoom
        self.course = course

    def GetProfessor(self):
        print("Professor Name is " + self.name)
        print("Professor assigned class is " + self.classRoom)
        print("Professor is teaching " + self.course)

                    # calling the three arguments
Teacher1 = Teacher("Prof. Sim","A206","Python Programming")
Teacher2 = Teacher("Prof. Med","A106","Java Programming")

Teacher1.GetProfessor()
print()
Teacher2.GetProfessor()

