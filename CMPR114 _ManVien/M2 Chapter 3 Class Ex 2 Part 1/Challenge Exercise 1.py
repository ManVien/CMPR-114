# get the test scores from user
t1 = int(input('enter test 1 score '))
t2 = int(input('enter test 2 score '))
t3 = int(input('enter test 3 score '))

# calculate the average of three test scores
average = (t1+t2+t3)/3

# display the average score
print('the average score is ', round(average))

# determine whether the letter grade is
if average >=90 and average <=100:
    print('letter grade A', round(average))
elif average >=80 and average <=89:
    print('letter grade B', round(average))
elif average >=70 and average <=79:
    print('letter grade C', round(average))
elif average >=60 and average <=69:
    print('letter grade D', round(average))
elif average > 100:
    print('the average cannot be over 100, try again')
elif average < 0:
    print('the average cannot be less than 0, try again')
else:
    print('letter grade F', round(average))


#write to the text file
f = open("Grade.txt", "a")
f.write('\nthe average score is ' + str(round(average)))
f.close()

#read from the text file
f = open("Grade.txt", "r")
print(f.read())


