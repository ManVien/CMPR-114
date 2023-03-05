# Distance Traveled
# This program asks the user to enter the speed and 
# number of hours it traveled and displays the distance 
# traveled for each hour by using a loop.

# get the speed in miles per hour
speed = int(input('What is the speed of the vehicle in mph? '))

# get the number of hours it has traveled
time = int(input('How many hours has it traveled? '))

print('\nHour\t\tDistance Traveled')
print('---------------------------------')

# use a loop to display the distance has traveled 
# for each hour of that time period
for number in range(1,time+1):
    # calculate the distance traveled
    distance = speed * number
    print(f'{number}\t\t\t{distance}')


