def main():
    strings = []
    string = input("Enter a string: ")
    strings.append(string)
    while string != '':
        string = input("Enter a string: ")
        strings.append(string)
    strings.sort()
    duplicate_strings = []
    for i in range(len(strings) - 2):
        if strings[i] == strings[i + 1]:
            if strings[i] not in duplicate_strings:
                duplicate_strings.append(strings[i])
    for string in duplicate_strings:
        print("Strings repeated:", string)


main()
