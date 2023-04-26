# Continuing from project #1 (B) add to the super constructor (see line 23)
# and add the address, city, state, and zip code for the Student and Teacher.
class person: 
    def __init__(self, name, age, address, city, state, zipcode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

# the student class is inheriting from the person class
class Student(person):
    def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):

        # prompt to enter information
        name = input('enter the name: ')
        age = input('enter the age: ')
        address = input('enter the address: ')
        city = input('enter the city: ')
        state = input('enter the state: ')
        zipcode = input('enter the zip code: ')
        studentID =  input('enter the Student ID: ')
        GPA = input('enter the GPA: ')
        print()

        # the super keyword is calling the super class
        # which is the person class and passing name and age

        super().__init__(name, age, address, city, state, zipcode)

        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, address, city, state, zipcode, TeacherID, ClassTeaching):
        super().__init__(name, age, address, city, state, zipcode)

        # prompt to enter information
        name = input('enter the name: ')
        age = input('enter the age: ')
        address = input('enter the address: ')
        city = input('enter the city: ')
        state = input('enter the state: ')
        zipcode = input('enter the zip code: ')
        TeacherID =  input('enter the Teacher ID: ')
        ClassTeaching = input('enter the name of the course teaching: ')
        print()

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student('Jane Doe', 25, "111 St", "Orange", "CA", 11111, 777, 3.8)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student Address: ", student.address)
print("Student City: ", student.city)
print("Student State: ", student.state)
print("Student Zip Code: ", student.zipcode)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)

print("\n")

teacher = Teacher("Ms. Cantor", 45, "345 St", "Santa Ana", "CA", 22222, 7, "Python")
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher Address: ", teacher.address)
print("Teacher City: ", teacher.city)
print("Teacher State: ", teacher.state)
print("Teacher Zip Code: ", teacher.zipcode)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)
