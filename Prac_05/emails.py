def main():
    email = input("Email: ")
    name_to_email = {}
    store_email_and_name(email, name_to_email)
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def store_email_and_name(email, name_to_email):
    while email != '':
        name_part = email.split("@")[0].split('.')
        guess_name = ' '.join(name_part).title()
        print(guess_name)
        check = input(f"Is your name {guess_name}? (Y/n) ").lower()
        name = guess_name
        if check == 'n' or check == 'no':
            name = input("Name: ")
        name_to_email[name] = email
        email = input("Email: ")


main()
