import random


def main():
    scores_num = int(input("Enter number of score: "))
    for i in range(scores_num):
        score = random.randint(0, 100)
        print(f"{score} is {get_grade_classification(score)}")


def get_grade_classification(score):
    if score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
