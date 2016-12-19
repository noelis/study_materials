 #!/usr/local/bin/python
 # coding: utf-8

import random

""" Write a function that generates a string that is 27 characters long by choosing random
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

    # new_str = ""

    # for i in range(28):
    #     new_str += random.choice(characters)

    # return new_str

    return "".join([random.choice(characters) for i in range(28)])

def score_string(test_str):
    string_goal = "methinks it is like a weasel"

    if test_str == string_goal:
        return True
    else:
        return "boo!"

test = generate_string()
print test
print score_string(test)

