# This program asks the user to enter the first, last name 
# with the age, write the contents to a file, and read from 
# the file.  

def WriteInformation():

    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    age = input('Enter the age: ')

    InformationFile = open('personalInformation.txt','w') # writing

    InformationFile.write(first_name + '\n')
    InformationFile.write(last_name + '\n')
    InformationFile.write(age + '\n')

    InformationFile.close()

    print('personal information recorded.\n')

WriteInformation()

def read():
    infile = open('personalInformation.txt','r') # reading

    fileContents = infile.read()

    infile.close()

    print(fileContents)

read()