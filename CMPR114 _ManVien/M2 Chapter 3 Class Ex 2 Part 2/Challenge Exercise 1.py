# Roulette Wheel Colors

# This program determines whether the pocket is green, red, or black.

# Get the pocket number
pocket = int(input('Enter a pocket number, from 0-36: '))

# Determine the color of the pocket.
if pocket == 0:
    print('The pocket is green.')
elif pocket >=1 and pocket <= 10:
    # the pocket is even number
    if (pocket % 2) == 0: 
        print('The pocket is black.')
    # the pocket is odd number
    else:
        print('The pocket is red.')
elif pocket >= 11 and pocket <= 18:
    if (pocket % 2) == 0:
        print('The pocket is red.')
    else:
        print('The pocket is black.')
elif pocket >= 19 and pocket <= 28:
    if (pocket % 2) == 0:
        print('The pocket is black.')
    else:
        print('The pocket is red.')
elif pocket >= 29 and pocket <= 36:
    if (pocket % 2) == 0:
        print('The pocket is red.')
    else:
        print('The pocket is black.')
else:
    # error message if the user enters a number that is outside the range of 0 through 36
    print('Invalid entry, try again.')

