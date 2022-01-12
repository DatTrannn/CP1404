import os
import shutil


def main():
    os.chdir('FilesToSort')
    for file in os.listdir("."):
        if os.path.isdir(file):
            continue
        extension = file.split('.')[1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(file, extension + '/' + file)


if __name__ == '__main__':
    main()
