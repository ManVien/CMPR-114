high_score = 95

# Get the test scores from user
test1 = int(input('enter test score 1:  '))
test2 = int(input('enter test score 2:  '))
test3 = int(input('enter test score 3:  '))

# Calculate the average of the test scores
average = (test1 + test2 + test3) / 3

# f means format the average
print('the average score is ' + str(average))

if average >= high_score:
    print('congrats')
else:
    print('try harder next time')

