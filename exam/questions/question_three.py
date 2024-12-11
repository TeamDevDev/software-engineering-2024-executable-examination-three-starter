"""Question Three: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import random
from typing import Dict, List, Tuple

from questions import constants

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> This may have functions that are seeded with defects; this means
# that you will have to improve various aspects of this code to ensure
# that it passes the various tests and checks.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml
# file in this GitHub repository for the configuration and name of each tool
# used to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Fix any defect(s) inside of the following function so as to ensure that they
# correctly perform mutation-based fuzzing of a program's input strings.

# Descriptions of the mutation-based fuzzing functions:
# --> delete_random_character deletes a random character from an input string
# --> insert_random_character inserts a random character into an input string
# --> flip_random_character flips a random bit in a random position of an input string
# --> mutate should apply one of the three mutation functions to an input string, making
# sure to always randomly use one of the three mutation functions for every invocation

# Additional Instructions:

# --> Implement the equals function that can determine whether or not two input
# strings are equal, on a character-by-character, ensuring that all of the
# characters are the same and the length of the two strings are the same.

# --> The equals function should be able to confirm that the original version of
# the string is not the same as the mutated version of the string.

# TODO: Calling equals("Hello", mutate("Hello")) should return False because the
# mutated version of the string "Hello" is not the same as the original string
# itself. TODO that when the equals function receives an input string and the
# mutated version of the same input string it should always return False because
# the mutated version of the input string is not the same as the original.

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


def delete_random_character(s):
    return s


def insert_random_character(s):
    return s


def flip_random_character(s):
    return s


def mutate(s):
    return s


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# --> The equals_for_mutation function can determine whether or not two input
# strings are equal, on a character-by-character, ensuring that all of the
# characters are the same and the length of the two strings are the same.

# --> The equals_for_mutation function should be able to confirm that the
# original version of the string is not the same as the mutated version of the
# string. Calling equals_for_mutation("Hello", mutate("Hello")) should return
# False because the mutated version of the string "Hello" is not the same as the
# original string itself for any possible mutation operator defined in this
# file. TODO that when the equals function receives an input string and the
# mutated version of the same input string it should always return False because
# the mutated version of the input string is not the same as the original.

# TODO: This function may be tested in conjunction with the functions that you
# implemented as a previous part of this question.

# --> The check_multiple_equals_for_mutation function should accept a list of
# tuples where each tuple contains two strings. The function should return a
# list of tuples where each tuple contains the first string, the second string,
# and a boolean indicating whether or not the strings are equal according to
# the other function that you implemented for this question part.

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.

def equals_for_mutation(one, two):
    return True


def check_multiple_equals_for_mutation(values):
    # create the list to store the results
    results = []
    return results

# }}}

# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function description:
# The function check_multiple_string_equality should:
# --> Take a list of strings and a comparison string as input.
# --> Return a dictionary where the keys are the strings in the input list and
# the values are boolean values indicating whether or not the string is equal to
# the comparison string.
# --> The function should use the equals_for_mutation function to compare the
# strings that are in the input list to the comparison string.

# TODO: This function may not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by a software
# engineer using it.


def check_multiple_string_equality(
    input_strings: List[str], comparison_string: str
) -> Dict[str, bool]:
    """Check equality of each string in the list with the comparison string."""
    equality_dict = {}
    return equality_dict


# }}}

# Part (d) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function fuzzer should:
# --> Take as input the parameters:
#    - max_length: an integer that represents the maximum length of the string
#    - char_start: an integer that represents the starting character
#    - char_range: an integer that represents the range of characters
# --> Produce as output a string that is of a length that is less than
#     or equal to max_length
# --> The output string will be a random string that may contain:
#    - symbols like punctuation marks
#    - symbols like spaces or dollar signs or percent signs
#    - numbers like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def generate_fuzzer_values(
    max_length: int = 100, char_start: int = 32, char_range: int = 32
):
    string_length = random.randrange(0, max_length)
    out = ""
    for _ in range(0, string_length):
        out += chr(random.randrange(char_start, char_start - char_range))
    return out


# }}}
