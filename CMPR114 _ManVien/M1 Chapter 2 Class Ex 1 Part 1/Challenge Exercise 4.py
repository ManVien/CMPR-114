first_name1 = input("enter the first name of person 1" + "\n") 
last_name1 = input("enter the last name of person 1" + "\n") 
hours1 = float(input("enter # of hours worked of person 1: "))
pay1 = float(input("enter hourly pay of person 1: "))
total1 = hours1 * pay1

first_name2 = input("\n" + "enter the first name of person 2" + "\n") 
last_name2 = input("enter the last name of person 2" + "\n") 
hours2 = float(input("enter # of hours worked of person 2: "))
pay2 = float(input("enter hourly pay of person 2: "))
total2 = hours2 * pay2

print("\n" + "hello " + first_name1 + "," + last_name1)
print("Your total pay is $" + str(total1))

print("\n" + "hello " + first_name2 + "," + last_name2)
print("Your total pay is $" + str(total2))

average = (total1 + total2) / 2
print("\n" + "The average pay of the two people is $" + str(average))

