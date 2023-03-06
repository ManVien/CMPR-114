# Grade Calculator

# Prompt the user to enter the score for test 1
test1 = int(input('Enter point for test 1: '))

# Determine if test 1 score is between 0 and 25
if test1 >= 0 and test1 <= 25:
    # Prompt the user to enter the score for test 2
    test2 = int(input('Enter point for test 2: '))
    # Determine if test 2 score is between 0 and 25
    if test2 >= 0 and test2 <= 25:
        # Prompt the user to enter the score for main exam
        exam = int(input('Enter point for main exam: '))
        # Determine if main exam score is between 0 and 50
        if exam >= 0 and exam <= 50:
            # calculate student's total score
            totalScore = test1 + test2 + exam
            # determine if main exam score is less than 25 or the total score is less than 50
            if exam < 25 or totalScore < 50:
                print('The total points: ', totalScore)
                print('The grade: Fail')
            else:
                # student's total score is more than 80
                if totalScore > 80:
                    print('The total points: ', totalScore)
                    print('The grade: Distinction')
                # student's total score is less than 80 but more than 60
                elif totalScore >= 60 and totalScore <= 80:
                    print('The total points: ', totalScore)
                    print('The grade: Credit')
                # student's total score is less than 60
                elif totalScore < 60:
                    print('The total points: ', totalScore)
                    print('The grade: Pass')
        else:
            # error message when exam score is not between 0 and 50
            print("Invalid entry. The main exam score is not between 0 and 50. Try again.")
    else:
        # error message when test score is not between 0 and 25
        print("Invalid entry. The test score is not between 0 and 25. Try again.")
else:
    # error message when test score is not between 0 and 25
    print('Invalid entry. The test score is not between 0 and 25. Try again.')

                




