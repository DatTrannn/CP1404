LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    print(f'The ASCII code for {char} is {ord(char)}')
    num = get_number(LOWER, UPPER)
    print(f'The character code for {num} is {chr(num)}')
    for i in range(LOWER, UPPER + 1):
        print(f"{i:>3} {chr(i)}")


def get_number(lower, upper):
    num = int(input(f"Enter a number between {lower} and {upper}: "))
    while num < 33 or num > 127:
        print("Please enter a valid number!")
        num = int(input(f"Enter a number between {lower} and {upper}: "))
    return num


main()
