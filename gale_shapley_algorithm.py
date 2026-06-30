# Adapted from Gale-Shapley example here:
# https://stackoverflow.com/questions/75877980/how-to-implement-gale-shapely-algorithm-in-python
import numpy as np

employer_prefs = {
    "A": ["2", "1", "3", "4"],
    "B": ["4", "1", "2", "3"],
    "C": ["1", "3", "2", "4"],
    "D": ["2", "3", "1", "4"],
}

applicant_prefs = {
    "1": ["A", "C", "B", "D"],
    "2": ["C", "D", "A", "B"],
    "3": ["D", "B", "C", "A"],
    "4": ["C", "B", "A", "D"],
}

unfilled_positions = list(employer_prefs.keys())
filled_positions = {}

while unfilled_positions:
    job = unfilled_positions.pop(0)  # get first unfilled position
    prefs = employer_prefs[job]  # get applicant preferences for that position

    for applicant in prefs:
        current_applicant_prefs = applicant_prefs[applicant]
        current_applicant_job = filled_positions.get(applicant)
        if current_applicant_job is None:
            filled_positions[applicant] = job
            break
        elif current_applicant_prefs.index(
            current_applicant_job
        ) > current_applicant_prefs.index(job):
            filled_positions[applicant] = job
            unfilled_positions.append(current_applicant_job)
            break
