# This example uses the super keyword to inherit
# attributes and arguments.

class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

# the student class is inheriting from the person class
class Student(person):
    def __init__(self, name, age, studentID, GPA):

        # prompt to enter information
        name = input('enter the name: ')
        age = input('enter the age: ')
        studentID =  input('enter the Student ID: ')
        GPA = input('enter the GPA: ')

        # the super keyword is calling the super class
        # which is the person class and passing name and age

        super().__init__(name, age)

        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, TeacherID, ClassTeaching):
        super().__init__(name, age)

        # prompt to enter information
        name = input('enter the name: ')
        age = input('enter the age: ')
        TeacherID =  input('enter the Teacher ID: ')
        ClassTeaching = input('enter the name of the course teaching: ')

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student('Jane Doe', 25, 777, 3.8)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)

print("\n")

teacher = Teacher("Ms. Cantor", 45, 7, "Python")
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)