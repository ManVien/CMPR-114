# Calories from Fat and Carbohydrates
# This program asks user enter the number of fat grams and carbohydrate grams
# that they consume in a day and calculates the number of calories. 

def main():
    fat_grams = int(input('Enter the number of fat grams that you consumed in a day: '))
    carb_grams = int(input('Enter the number of carbohydrate grams that you consumed in a day: '))
    calories_fat = calculate_calories_from_fat(fat_grams)
    calories_carbs = calculate_calories_from_carbs(carb_grams)
    display_calculation(calories_fat, calories_carbs)

def calculate_calories_from_fat(fat):
    calo_fat = fat * 9
    return calo_fat

def calculate_calories_from_carbs(carb):
    calo_carbs = carb * 4
    return calo_carbs

def display_calculation(calo_fat, calo_carbs):
    print(f'The number of calories from fat: {calo_fat}')
    print(f'The number of calories from carbohydrates: {calo_carbs}')

main()
