# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
names_file = open("name.txt", 'w')
name = input("Enter your name: ")
print(name, file=names_file)
names_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
names_file = open("name.txt", 'r+')
name = names_file.read()
print(f"Your name is {name}", file=names_file)
names_file.close()

# 3. Write code that opens "numbers.txt", reads only the first two numbers
# and adds them together then prints the result, which should be... 59.
numbers_file = open("numbers.txt", "r")
total = 0
for i in range(2):
    number = int(numbers_file.readline())
    total += number
print("Sum:", total)
numbers_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
numbers_file = open("numbers.txt", "r")
total = 0
for line in numbers_file:
    total += int(line)
    print(total)
