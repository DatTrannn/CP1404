from unreliable_car import UnreliableCar


def main():
    car_1 = UnreliableCar("Prius 1", 100, 45)
    car_1.drive(50)
    print(car_1.name, car_1.drive(30))


if __name__ == '__main__':
    main()
