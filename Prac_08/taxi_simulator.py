from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    get_choice(current_taxi, taxis)
    print("Taxis are now:")
    print_taxis(taxis)


def get_choice(current_taxi, taxis):
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                bill_to_date += current_taxi.get_fare()
        elif choice == "c":
            print("Taxis available")
            print_taxis(taxis)
            try:
                taxi_num = int(input("Choose taxi: "))
                if taxi_num < 0 or taxi_num >= len(taxis):
                    print("Invalid choice")
                else:
                    current_taxi = taxis[taxi_num]
            except ValueError:
                print("Invalid choice")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date}")


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi.__str__()}')


if __name__ == '__main__':
    main()
