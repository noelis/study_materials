 #!/usr/local/bin/python
 # coding: utf-8

import random

""" Scope  of problem:

    Write a function that generates a string that is 27 characters long by choosing random
    letters from the 26 letters in the alphabet plus the space.

    We’ll write another function that will score each generated string by comparing the
    randomly generated string to the goal.
    
    A third function will repeatedly call generate and score, then if all of the letters 
    are correct we are done. If the letters are not correct then we will generate a whole new string.

    To make it easier to follow your program’s progress this third function should 
    print out the best string generated so far and its score every 1000 tries."""


def generate_string():
    """Generates a string that is 27 characters long by choosing random letters 
    from the 26 letters in the alphabet plus a space."""

    characters = "abcdefghijklmnopqrstuvwxyz "

    return "".join([random.choice(characters) for i in range(28)])


def score_string(test_str):
    """ Scores each generated string by comparing the randomly generated string to the goal. """

    string_goal = "methinks it is like a weasel"

    count_correct = 0

    for i in range(28):
        if test_str[i] == string_goal[i]:
            count_correct += 1

    return count_correct/28.0


def repeat_again():
    """A third function will repeatedly call generate and score, then if all of the letters 
    are correct we are done. If the letters are not correct then we will generate a whole new string."""
 
    best = 0
    test_str = generate_string()
    score = score_string(test_str)
    count = 0

    while score < 1:
        count += 1
        if count % 1000 == 0:
            print test_str, best
        elif score > best:
            print score, test_str
            best = score
        test_str = generate_string()
        score = score_string(test_str)



print repeat_again()