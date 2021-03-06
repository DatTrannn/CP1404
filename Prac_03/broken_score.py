"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    print(get_grade_classification(score))
    random_score = random.randint(0, 100)
    print(f"The score {random_score} is {get_grade_classification(random_score)}")


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
