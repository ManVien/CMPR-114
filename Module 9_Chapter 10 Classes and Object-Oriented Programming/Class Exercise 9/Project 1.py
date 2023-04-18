# This class is an example of creating objects and using the self-keyword 
# to access variables within this class. 

class Students:
    # the keyword (self)
    # it is used to access variables that belong to that class.
    def GetInformation(self):
        print("Student Lastname is " + self.Lastname)
        print("Student Firstname is " + self.Firstname)
        print("Student Address name is " + self.Address)
        print("Student City name is " + self.City)
        print("Student State name is " + self.State)
        print("Student Zipcode name is " + self.Zipcode)

# create the Student1 object
Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1.City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345\n"

# create the Student2 object
Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2.City = "Garden Grove"
Student2.State = "CA"
Student2.Zipcode = "67890"

# Calling the function
Student1.GetInformation()
Student2.GetInformation()
