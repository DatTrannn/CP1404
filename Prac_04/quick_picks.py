import random

NUMBERS_NUM = 6
MIN_NUM = 1
MAX_NUM = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        line = []
        for j in range(NUMBERS_NUM):
            number = random.randint(MIN_NUM, MAX_NUM)
            while number in line:
                number = random.randint(MIN_NUM, MAX_NUM)
            line.append(number)

        line.sort()
        print(' '.join(f"{num:2}" for num in line))


main()
