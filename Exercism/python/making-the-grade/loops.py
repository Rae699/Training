"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_scores = []
    for grade in student_scores:
        rounded_grade = round(grade)
        rounded_scores.append(rounded_grade)
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failing_count = 0
    for grade in student_scores:
        if grade <= 40:
            failing_count += 1
    return failing_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    # Return a list of the int scores that are >= threshold
    
    top_scores = []
    for score in student_scores:
        if score >= threshold:
            top_scores.append(score)
    return top_scores


def letter_grades(highest):
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
    
    interval = (highest - 40) // 4
    
    # Calculate thresholds starting from 41
    d_threshold = 41
    c_threshold = d_threshold + interval
    b_threshold = c_threshold + interval
    a_threshold = b_threshold + interval

    return [d_threshold, c_threshold, b_threshold, a_threshold]



def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    
    ranked_students = []
    
    for rank, name in enumerate(student_names):
        ranked_students.append(f"{rank + 1}. {name}: {student_scores[rank]}")
    
    return ranked_students


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    
    for student in student_info:
        if student[1] == 100:
            return student
    return []