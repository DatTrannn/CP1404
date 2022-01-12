"""
CP1404/CP5632 Practical
Demos of various os module examples
"""


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, char in enumerate(filename):
        if char.isupper() and filename[i - 1:i].islower():
            new_name += f'_{char}'
        elif filename[i - 1:i] == ' ':
            new_name += ''
        elif (filename[i - 1:i] == '_' or filename[i - 1:i] == '(') and char.islower():
            new_name += char.upper()
        else:
            new_name += char
    return new_name


print(get_fixed_filename("ItIsWell (oh my soul).txt"))
