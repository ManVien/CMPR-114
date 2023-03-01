# Project # 1 
# creating lists
evenNumbers = [2,4,6,8,10]
print (evenNumbers)

names = ["ian","jason","molly"]
print (names)

info = ["ally",27,1550.87]
print (info)

# print the number 5, 5x
numbers = [5] * 5
print (numbers)

# using a for loop to print numbers in a list
LoopNumbers = [1,2,3,4,5,6,7] #1-7 are the elements in the list
for n in LoopNumbers:
    print (n)

# using a while loop and incrementing by 1
index = 0
while index < 4:
    print(LoopNumbers[index])
    index += 1

# the len function counts how many numbers there are in the list
size = len(LoopNumbers)
print ("there are " + str(size) + " numbers in the list.")

# specify which number in a list to print using indexes
evenNumbers = [2,4,6,8,10]
print (evenNumbers[0])

# sum the list of numbers using a for loop
sum = 0
evenNumbers = [2,4,6,8,10]
for a in evenNumbers:
    sum += a #adds the numbers in the list
print (evenNumbers[0])
print("total sum " + str(sum))


