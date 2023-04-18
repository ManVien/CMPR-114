# Continue project #3, add the address, city, and state with the zip code.

class PI:
                    # passing three parameters
    def GetInformation(self, LN, FN, Age, Address, City, State, ZC):
        return LN + " , " + FN + " , " + str(Age) + " , " + \
                Address + " , " + City + " , " + State + " , " + ZC

PersonalInformation = PI()
PersonalInformation.Lastname = input("Enter the lastname: ") 
PersonalInformation.Firstname = input("Enter the firstname: ")
PersonalInformation.Age = int(input("Enter the age: "))
PersonalInformation.Address = input("Enter the address: ")
PersonalInformation.City = input("Enter the city: ")
PersonalInformation.State = input("Enter the state: ")
PersonalInformation.Zipcode = input("Enter the zip code: ")

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname,
                                         PersonalInformation.Age, PersonalInformation.Address, 
                                         PersonalInformation.City, PersonalInformation.State, 
                                         PersonalInformation.Zipcode))
