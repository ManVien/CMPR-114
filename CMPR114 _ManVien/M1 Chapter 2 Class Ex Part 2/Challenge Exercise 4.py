males = int(input('Enter the number of males registered in a class: '))
females = int(input('Enter the number of females registered in a class: '))
total_students = males + females
males_percentage = males / total_students
females_percentage = females / total_students
print(f'The percentage of males in the class is {males_percentage:.2f}' 
      + ',' + ' or' + f'{males_percentage: .0%}')
print(f'The percentage of females in the class is {females_percentage:.2f}' 
      + ',' + ' or' + f'{females_percentage: .0%}')
