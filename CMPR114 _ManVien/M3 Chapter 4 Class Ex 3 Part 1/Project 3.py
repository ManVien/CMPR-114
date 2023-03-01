# Project #2
# A program that will ask to enter the temperature 
# by using the while loop.

# Named constant, a named constant is a variable that does not change.
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the temperature for today: "))

# As long as necessary, instruct the user to adjust the thermostat.
while temperature > MAX_TEMP:
    print('The temperature is too high.') 
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

# Remind the user to check the temperature again 
# in 15 minutes.
    print('The temperature is acceptable.')    
    print('Check it again in 15 minutes.')

