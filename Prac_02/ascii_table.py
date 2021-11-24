LOWER = 33
UPPER = 127

char = input("Enter a character: ")
print(f'The ASCII code for {char} is {ord(char)}')
num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while num < 33 or num > 127:
    num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
print(f'The character code for {char} is {ord(char)}')

for i in range(LOWER, UPPER + 1):
    print(f"{i:>3} {chr(i)}")
