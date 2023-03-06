# Quarter of the Year

# This program displays the quarter of a month based on user input.

# Prompt the user to enter a month
month = int(input('Enter a month as a number between 1 and 12: '))
   
# Determine which quarter the month is in
if month >= 1 and month <= 3:
    print('The month is in the first quarter.')
elif month >= 4 and month <= 6:
    print('The month is in the second quarter.')
elif month >= 7 and month <= 9: 
    print('The month is in the third quarter.')
elif month >= 10 and month <= 12:
    print('The month is in the fourth quarter.')
else:
    # display an error message if the number is not between 1 and 12
    print('Invalid entry. Please enter a number between 1 and 12. Try again.')


