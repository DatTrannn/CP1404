# used_cars.py
from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Limo", 100)
    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
    # Print the amount of fuel in the car.
    print("fuel =", limo.fuel)
    # Attempt to drive the car 115 km using the drive method.
    limo.drive(15)
    # Print the car's odometer reading.
    print("odo =", limo.odometer)
    # In your used_cars.py program, just print your car object/s to make sure that the __str__ method is working as expected.
    print(limo)


main()
