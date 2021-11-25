import random

random_file = open('temps_input.txt', 'w')

for i in range(20):
    print(random.uniform(-200, +201), file=random_file)

random_file.close()
