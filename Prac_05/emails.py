def main():
    email = input("Email: ")
    name_to_email = {}
    while email != '':
        name_part = email.split("@")[0].split('.')
        guess_name = ' '.join(name_part).title()
        print(guess_name)
        check = input(f"Is your name {guess_name}? (Y/n) ").lower()
        if check == 'n' or check == 'no':
            name = input("Name: ")
        elif check == 'y' or check == '' or check == 'yes':
            name = guess_name
        name_to_email[name] = email
        email = input("Email: ")
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


main()
