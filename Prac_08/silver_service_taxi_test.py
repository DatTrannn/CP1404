from silver_service_taxi import SilverServiceTaxi


def main():
    uber = SilverServiceTaxi("Uber", 100, 2)
    uber.drive(18)
    uber.get_fare()
    print(uber.get_fare())


if __name__ == '__main__':
    main()
