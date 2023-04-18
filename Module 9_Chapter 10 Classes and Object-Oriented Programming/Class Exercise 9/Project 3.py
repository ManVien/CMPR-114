# This class is an example of passing parameters and
# accessing those parameters to get an output.

class PI:
                    # passing three parameters
    def GetInformation(self, LN, FN, Age):
        return LN + " , " + FN + " , " + str(Age)

PersonalInformation = PI()
PersonalInformation.Lastname = input("Enter the lastname: ") 
PersonalInformation.Firstname = input("Enter the firstname: ")
PersonalInformation.Age = int(input("Enter the age: "))

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname,
                                         PersonalInformation.Age))
