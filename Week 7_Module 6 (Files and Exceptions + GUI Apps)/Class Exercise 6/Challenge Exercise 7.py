# This program asks the user to enter the full name, with the grade of the midterm and final exam. 
# Write the average grade with letter grade into a text file.
# Use the table as a guide. Use also the try statement for this application. 
# Make sure to append the data and read the content of the file also.

def main():
    try:
        # Get the full name, midterm, and final grade from the user.
        name, midterm, final = get_values()

        # Get the total of the test scores.
        average = get_calculations(midterm, final)
    
        write(name, average)

        # Display the letter grade.
        letter_grade(average)

        print('Data recorded.')

        # Read the content of the file
        read()

    except Exception as err:  # built-in Exception error processing
        print(err)

def get_values():
    while True:
        try: # try the batch of code below, if there are no errors than disregard the except
            name = input('Enter the full name: ')
            midterm_score = float(input('Enter the grade of the midterm: '))
            final_exam_score = float(input('Enter the grade of final exam: '))

            # Return values
            return name, midterm_score, final_exam_score

        except Exception as err:
            print(err)

def get_calculations(midterm, final):
    try:
        # Create a variable to use as an accumulator.
        total = 0.0
        # Calculate the total and average
        total = midterm + final
        average = total / 2
        # Return the average.
        return average

    except Exception as err:
        print(err)

def letter_grade(average):
    try:
        # Open a file in append mode
        outfile = open('average_and_letter_grade.txt','a')

        if average >= 90 and average <= 100: 
            outfile.write('Letter grade A\n\n')
        elif average >= 80 and average <= 89:
            outfile.write('Letter grade B\n\n')
        elif average >= 70 and average <= 79:
            outfile.write('Letter grade C\n\n')
        elif average >= 60 and average <= 69:
            outfile.write('Letter grade D\n\n')
        elif average >= 0 and average < 60:
            outfile.write('Letter grade F\n\n')
        else:
            outfile.write('The average grade cannot be less than 0 or higher than 100.' 
            + 'Please try again.\n')

        # Close the file
        outfile.close()

    except Exception as err:
        print(err)

def write(name, average):
    try:
        # Open a file in append mode
        outfile = open('average_and_letter_grade.txt','a')

        # Write to the file
        outfile.write(f'Name: {name}' + '\n' + f'The average grade: {average:.2f}\n')

        # Close the file
        outfile.close()

    except Exception as err:
        print(err)

def read():
    print('\nReading from the file')
    try:
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

    except Exception as err:
        print(err)

# Call the main function.
if __name__ == '__main__':
    main()