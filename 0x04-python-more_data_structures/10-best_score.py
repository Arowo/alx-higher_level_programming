#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    high_score = 0
    score_owner = None
    for keys, value in a_dictionary.items():
        if value > high_score:
            score_owner = keys
            high_score = value
    return score_owner
