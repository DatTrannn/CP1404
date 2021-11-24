try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
1. A ValueError occurs when input type is string
2. A ZeroDivisionError occurs when denominator input is 0 --> can't divided by 0
3. Using while loop to ask the user reenter the denominator if the input is 0
"""
