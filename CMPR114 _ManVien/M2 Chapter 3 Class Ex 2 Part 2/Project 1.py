#1 
#Python allows you to compare strings. This allows you to create decision 
#structures that test the value of a string
name1 = 'Mary'
name2 = 'Mark'
if name1 == name2:
    print('The names are the same.')
else:
    print('The names are NOT the same.')

#2
#This program compares two strings. Get a password from the user.
password = input('Enter the password: ')

#Determine whether the correct password was entered.
if password == 'sac123':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')


#3
#This program compares strings with the < operator. Get two names from the user.
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')

#Display the names in alphabetical order.
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)


