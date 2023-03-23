# This program asks the user to enter the full name, with the grade of the midterm and final exam. 
# Write the average grade with letter grade into a text file.
# Use the table as a guide. Use also the try statement for this application. 
# Make sure to append the data and read the content of the file also.

from multiprocessing import Value


def main():
    # Get the test scores from the user.
    name, midterm, final = get_scores()

    # Get the total of the test scores.
    total = get_total(midterm, final)
    
    # Calculate the average. 
    average = total / 2.0

    # Display the average.
    print(f'Average grade: {average:.2f}')

    # Open a file in append mode
    outfile = open('average_and_letter_grade.txt','a')

    # Write the output to the file
    outfile.write(f'The average grade: {average:.2f}\n')

    # Close the file
    outfile.close()

    # Display the letter grade.
    letter_grade(average)

    print('Data recorded.\n')

    # Read the content of the file
    Read()

# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference to the list is returned.
def get_scores():

    while True:
        try: # try the batch of code below, if there are no errors than disregard the except
            # Get a score and add it to the list.
            name = input('Enter the full name: ')
            midterm_score = float(input('Enter the grade of the midterm: '))
            final_exam_score = float(input('Enter the grade of final exam: '))

            # Return values
            return name, midterm_score, final_exam_score

        except Exception as err: # built-in Exception error processing
                print(err)

# The get_total function accepts a list as an 
# argument and returns the total of the values in
# the list.
def get_total(midterm, final):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total
    total = midterm + final

    # Return the total.
    return total

def letter_grade(average):
    # Open a file in append mode
    outfile = open('average_and_letter_grade.txt','a')

    if average >= 90 and average <= 100: 
        print('Letter grade A')
        outfile.write('Letter grade A\n')
    elif average >= 80 and average <= 89:
        #lgrade = 'B'  
        print('Letter grade B')
        outfile.write('Letter grade B\n')
    elif average >= 70 and average <= 79:
        #lgrade = 'C'
        print('Letter grade C')
        outfile.write('Letter grade C\n')
    elif average >= 60 and average <= 69:
        #lgrade = 'D'
        print('Letter grade D')
        outfile.write('Letter grade D\n')
    elif average >= 0 and average < 60:
         #lgrade = 'F'       
        print('Letter grade F')
        outfile.write('Letter grade F\n')
    else:
        print('The average grade cannot be less than 0 or higher than 100. Please try again.')
        outfile.write('The average grade cannot be less than 0 or higher than 100. Please try again.\n')

    # Close the file
    outfile.close()

def Read():

    grades_file = open('average_and_letter_grade.txt','r')

    # Read the first line from the file
    line = grades_file.readline()

    while line != '': # as long as an empty string is NOT returned
        # Strip the \n from the line
        line_content = line.rstrip('\n')
        # Display the record.
        print(line_content)
        # Read the next line
        line = grades_file.readline()

    grades_file.close()

# Call the main function.
if __name__ == '__main__':
    main()