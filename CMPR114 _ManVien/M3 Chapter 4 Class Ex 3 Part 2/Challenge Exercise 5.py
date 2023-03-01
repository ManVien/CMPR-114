# Lap Times
# This program asks user to enter the number of times they have run
# around a racetrack and the lap time for each of their laps. 
# It will display the time of theit fastest lap, the time of their slowest lap,
# and their average lap time.

# Get the number of times they have run around a racetrack.
number = int(input('Enter the number of times you have run around a racetrack: '))

# Declare variables 
fastest_lap_time = None
slowest_lap_time = None
total = 0.0

# Use a for loop to prompt the user to enter the lap time for each of their laps.
for lap in range(number):
    lap_time = float(input(f'\nEnter the lap time for lap {lap + 1} (minutes): '))
    total += lap_time
   
    # Determine the time of their fastest lap.
    if fastest_lap_time == None or lap_time > fastest_lap_time:
        fastest_lap_time = lap_time
    # Determine the time of their slowest lap.
    elif slowest_lap_time == None or lap_time < slowest_lap_time:
        slowest_lap_time = lap_time

# Calculate the average lap time.
average = total / number

# Display the results
print(f'\nThe time of your fastest lap is {fastest_lap_time}.')
print(f'\nThe time of your slowest lap is {slowest_lap_time}.')
print(f'\nYour average lap time is {average:.2f}.\n')


