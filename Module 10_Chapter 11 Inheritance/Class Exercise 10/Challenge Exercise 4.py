# Continuing from project #2, add the number of doors for each car, 
# be sure to add a mutator and an accessor for the door description.

import vehicles

def main():

    used_car1 = vehicles.Automobiles('Audi', 2022, 45000, 80000.0, 4)

    print('Make: ', used_car1.get_make())
    print('Model: ', used_car1.get_model())
    print('Mileage: ', used_car1.get_mileage())
    print('Price: ', used_car1.get_price())
    print('Doors: ', used_car1.get_doors())

    print("\n")

    used_car2 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0, 4)

    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print('Price: ', used_car2.get_price())
    print('Doors: ', used_car2.get_doors())

main()