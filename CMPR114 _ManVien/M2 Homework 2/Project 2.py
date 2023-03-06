# Hot Dog Cookout Calculator

# This program displays the number of packages of hot dogs and hot dog buns required 
# and the number of hot dogs and hot dog buns that will be left over.

HOTDOGS_PER_PACK = 10
HOTDOG_BUNS_PER_PACK = 8

# Get the number of people attending the cookout
people = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs each person will have 
hotdog = int(input('Enter the number of hot dogs each person will be given: '))
hotdog_buns = hotdog

# Calculate the total hot dogs required 
total_hotdog = people * hotdog
total_hotdog_bun = total_hotdog

# The number of hot dogs and hot dog buns that will be left over is zero.
if (total_hotdog % HOTDOGS_PER_PACK) == 0 and (total_hotdog_bun % HOTDOG_BUNS_PER_PACK) == 0:
    print('The minimum number of packages of hot dogs required: ', 
          total_hotdog // HOTDOGS_PER_PACK)
    print('The minimum number of packages of hot dog buns required: ', 
          total_hotdog_bun // HOTDOG_BUNS_PER_PACK)
    print('The number of hot dogs that will be left over: ', 
          total_hotdog % HOTDOGS_PER_PACK)
    print('The number of of hot dog buns that will be left over: ', 
          total_hotdog_bun % HOTDOG_BUNS_PER_PACK)
# The number of left over hot dogs is zero, and the number of left over hot dog buns is not zero.
elif (total_hotdog % HOTDOGS_PER_PACK) == 0 and (total_hotdog_bun % HOTDOG_BUNS_PER_PACK) != 0:
    print('The minimum number of packages of hot dogs required: ', 
          total_hotdog // HOTDOGS_PER_PACK)
    print('The minimum number of packages of hot dog buns required: ', 
          (total_hotdog_bun // HOTDOG_BUNS_PER_PACK) + 1)
    print('The number of hot dogs that will be left over: ', 
          total_hotdog % HOTDOGS_PER_PACK)
    print('The number of of hot dog buns that will be left over: ', 
          ((total_hotdog_bun // HOTDOG_BUNS_PER_PACK) + 1) * HOTDOG_BUNS_PER_PACK - total_hotdog_bun)
# The number of left over hot dogs is not zero, and the number of left over hot dog buns is zero.
elif (total_hotdog % HOTDOGS_PER_PACK) != 0 and (total_hotdog_bun % HOTDOG_BUNS_PER_PACK) == 0:
    print('The minimum number of packages of hot dogs required: ', 
          (total_hotdog // HOTDOGS_PER_PACK) + 1)
    print('The minimum number of packages of hot dog buns required: ', 
          total_hotdog_bun // HOTDOG_BUNS_PER_PACK)
    print('The number of hot dogs that will be left over: ', 
          ((total_hotdog // HOTDOGS_PER_PACK) + 1) * HOTDOGS_PER_PACK - total_hotdog)
    print('The number of of hot dog buns that will be left over: ', 
          total_hotdog_bun % HOTDOG_BUNS_PER_PACK)
# The number of left over hot dogs is not zero, and the number of left over hot dog buns is not zero.
else:
    print('The minimum number of packages of hot dogs required: ', 
          (total_hotdog // HOTDOGS_PER_PACK) + 1)
    print('The minimum number of packages of hot dog buns required: ', 
          (total_hotdog_bun // HOTDOG_BUNS_PER_PACK) + 1)
    print('The number of hot dogs that will be left over: ', 
          ((total_hotdog // HOTDOGS_PER_PACK) + 1) * HOTDOGS_PER_PACK - total_hotdog)
    print('The number of of hot dog buns that will be left over: ', 
          ((total_hotdog_bun // HOTDOG_BUNS_PER_PACK) + 1) * HOTDOG_BUNS_PER_PACK - total_hotdog_bun)


