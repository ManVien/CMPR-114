# This program sorts a tuple by the list total

input_tup = ([2, 20], [44, 1], [3, 13])

sorted_tup = tuple(sorted(input_tup,key = sum))

print('Sort this tuple by the list total')
print(sorted_tup)