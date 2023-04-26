# Continuing from project #2, print out another car’s description.

import vehicles

def main():

    used_car1 = vehicles.Automobiles('Audi', 2022, 45000, 80000.0)

    print('Make: ', used_car1.get_make())
    print('Model: ', used_car1.get_model())
    print('Mileage: ', used_car1.get_mileage())
    print('Price: ', used_car1.get_price())

    print("\n")

    used_car2 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0)

    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print('Price: ', used_car2.get_price())

main()