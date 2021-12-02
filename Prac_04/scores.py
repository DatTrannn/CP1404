"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_by_subjects = convert_to_score_by_subjects(score_values)
    scores_file.close()
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in scores_by_subjects[i]:
            print(score)
        print("Max:", max(scores_by_subjects[i]))
        print("Min:", min(scores_by_subjects[i]))
        print("Avg:", sum(scores_by_subjects[i]) / len(scores_by_subjects[i]))


def convert_to_score_by_subjects(score_values):
    scores_by_subjects = []
    for i in range(5):
        scores_by_a_subject = []
        for scores in score_values:
            scores_by_a_subject.append(scores[i])
        scores_by_subjects.append(scores_by_a_subject)
    return scores_by_subjects


main()
