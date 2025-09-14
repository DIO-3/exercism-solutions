"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    beta = [round(score) for score in student_scores]
    return beta    
    
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """


def count_failed_students(student_scores):
    alpha = round_scores(student_scores)
    gamma = [score for score in alpha if score <= 40]
    return len(gamma)
    
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    pass


def above_threshold(student_scores, threshold):
    rounded_scores = round_scores(student_scores)
    top = [score for score in rounded_scores if score >= threshold]
    print(top)
    return top
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

import math

def letter_grades(highest):
    high = highest-1 
    alpha = high-40
    beta = alpha/4 
    F = 40 
    D = math.ceil(41) 
    C = math.ceil(D+beta)
    B = math.ceil(C+beta)
    A = math.ceil(B+beta)
    results = [D,C,B,A]
    return results
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    


def student_ranking(student_scores, student_names):
    rank = list(range(1, len(student_names) + 1))
    answer = [f"{num}. {name}: {score}" for num, name, score in zip(rank, student_names, student_scores)]
    return answer
    
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """



def perfect_score(student_info):
    for record in student_info:
        if record[1] == 100:
            print(record)  # Print the record for verification
            return record  # Return the sublist if a score of 100 is found
    print("[]")  # Print empty list if no 100 is found
    return []  
            
            
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

