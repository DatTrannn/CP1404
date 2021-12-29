from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     current_guitar = Guitar(name, year, cost)
    #     print(current_guitar, "added")
    #     guitars.append(current_guitar)
    #     print()
    #     name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            print(f"Guitar {i}: {guitar.name:>19} ({guitar.year}), worth $ {guitar.cost:>9,.2f} (vintage)")
        else:
            print(f"Guitar {i}: {guitar.name:>19} ({guitar.year}), worth $ {guitar.cost:>9,.2f}")


main()
