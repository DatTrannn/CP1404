import random


def main():
    print("Welcome to the Gopher Population Simulator!\nStarting population: 1000\nYear 1")
    population = 1000
    year = 1
    while population >= 4:
        born = int(population * (random.randint(10, 20) / 100))
        died = int(population * (random.randint(5, 25) / 100))
        population = population + born - died
        year += 1
        print(f"\n{born} gophers were born. {died} died.\nPopulation: {population}\nYear {year}")
    print("End program!")


main()
