def main():
    input_file = open("temps_input.txt", 'r')
    output_file = open("temps_output.txt", 'w')
    for line in input_file:
        celsius = fahrenheit_to_celsius(float(line))
        print(celsius, file=output_file)
    input_file.close()
    output_file.close()


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
