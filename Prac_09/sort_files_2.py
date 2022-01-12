import os
import shutil


def main():
    extension_to_category = {}
    os.chdir('FilesToSort')
    for file in os.listdir("."):
        if os.path.isdir(file):
            continue
        extension = file.split('.')[1]
        if extension not in extension_to_category:
            category = input(f"What category would you like to sort {extension} files into? ")
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(file, extension_to_category[extension] + '/' + file)


if __name__ == '__main__':
    main()
