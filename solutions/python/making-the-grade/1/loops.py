"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students (score <= 40)."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Return a list of scores that are >= threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """
    Given the highest possible score, create threshold cutoffs for D, C, B, A.

    Failing score = 40
    Grades start from 41.
    The range between 41 and highest is divided into 4 equal intervals.
    """
    step = (highest - 40) // 4
    return [41 + step * i for i in range(4)]


def student_ranking(student_scores, student_names):
    """
    Return ranking list such as:
    ["1. Alice: 99", "2. Bob: 90", ...]
    """
    ranking = []
    for idx, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking.append(f"{idx}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    """Return first [name, 100] student or [] if none."""
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
