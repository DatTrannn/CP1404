COLOR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                 "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                 "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0"}

color = input("Enter a color: ").lower()
while color != '':
    for name in COLOR_TO_CODE.keys():
        if color == name.lower():
            print(f"{color} is {COLOR_TO_CODE[name]}")
    color = input("Enter a color: ").lower()
