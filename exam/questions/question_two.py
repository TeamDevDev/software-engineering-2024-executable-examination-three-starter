"""Question Two: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import ast
from typing import Dict, List

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

# Implement the following function(s) that perform a configurable linting
# analysis of Python source code using the Abstract Syntax Tree (AST) module.

# Function description:
# The function count_print_functions_linter should:
# --> Accept a single parameter, source_code, which is a string that contains
#     valid Python source code of a function subject to static analysis.
# --> Return an integer that represents the number of print function calls
#     that are present in the given Python source code.
# --> If the source code does not contain the print function call, then
#     the function should return 0 to indicate the absence of print calls.
# --> If the source code contains the word "print" but it is not a function
#     call, then it should not be counted.
# --> Overall, this function acts as one part of a configurable linter that
#     counts the number of print function calls in a given Python source code.
#     For many projects, it is accepted that a function should not have any
#     print statements inside of a function beyond those designated for the
#     command-line interface (CLI) or text-based user interface (TUI).

# Function description:
# The function detect_print_function_violation_linter should:
# --> Accept a parameter, source_code, which is a string that contains
#     valid Python source code of a function subject to static analysis.
# --> Accept an optional parameter, max_prints, which is an integer that
#     designates the maximum number of print function calls that are allowed
#     inside of the provided Python source code.
# --> Return a boolean value that indicates whether the given Python source
#     code contains print function calls beyond the provided maximum number.
#     If the number of print function calls is greater than the maximum number,
#     then the function should return True to indicate a violation. Otherwise,
#     then the function returns False to indicate that there is no violation.

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


def count_print_functions_linter(source_code):
    print_count = 0
    return print_count


def detect_print_function_violation_linter(source_code, max_prints):
    return False


# }}}

# Part (b) {{{

# Instructions: Implement the following functions so that they adhere to all
# aspects of the following specification.

# Function description:
# The function count_operator_in_assignments should:
# --> Accept a single parameter, source_code, which is a string that contains
#     valid Python source code of a function subject to static analysis.
# --> Accept a parameter, operator_type, which is a type that represents the
#     specific operator to count in assignment statements.
# --> Return an integer that represents the number of times the specified
#     operator is used in assignment statements in the given Python source code.
# --> If the source code does not contain the specified operator in assignment
#     statements, then the function should return 0 to indicate the absence.
# --> Overall, this function acts as one part of a configurable linter that
#     counts the number of specific operator uses in assignment statements.

# Function description:
# The function count_plus_operator_in_assignments should:
# --> Accept a single parameter, source_code, which is a string that contains
#     valid Python source code of a function subject to static analysis.
# --> Return an integer that represents the number of times the + operator is
#     used in assignment statements in the given Python source code.
# --> If the source code does not contain the + operator in assignment
#     statements, then the function should return 0 to indicate the absence.
# --> Overall, this function acts as one part of a configurable linter that
#     counts the number of + operator uses in assignment statements.

# Function description:
# The function count_minus_operator_in_assignments should:
# --> Accept a single parameter, source_code, which is a string that contains
#     valid Python source code of a function subject to static analysis.
# --> Return an integer that represents the number of times the - operator is
#     used in assignment statements in the given Python source code.
# --> If the source code does not contain the - operator in assignment
#     statements, then the function should return 0 to indicate the absence.
# --> Overall, this function acts as one part of a configurable linter that
#     counts the number of - operator uses in assignment statements.

# TODO: The count_plus_operator_in_assignments and count_minus_operator_in_assignments
# functions should call the count_operator_in_assignments function with the
# appropriate operator type, using one of the options from the ast module. For
# instance, Ast.Add for the + operator and Ast.Sub for the - operator.

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.

def count_operator_in_assignments(source_code: str, operator_type: type) -> int:
    operator_count = 0
    return operator_count


def count_plus_operator_in_assignments(source_code: str) -> int:
    return 0


def count_minus_operator_in_assignments(source_code: str) -> int:
    return 0

# }}}

# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function description:
# The function check_print_violations_in_functions should:
# --> Accept a single parameter, source_code_list, which is a list of strings,
#     each representing the source code of a Python function.
# --> Accept a parameter, max_prints, which is an integer that represents the
#     maximum number of print statements allowed in the function. The default
#     value for max_prints is 0.
# --> Call the detect_print_function_violation_linter function for each source
#     code string in the list.
# --> Create a dictionary where the key is the provided source code as a string
#     and the value is the boolean value that was the output of the detect
#     function.
# --> Return the dictionary containing the source code strings and their
#     corresponding boolean violation results.

# Function description:
# The function count_print_violations_in_functions should:
# --> Accept a single parameter, source_code_list, which is a list of strings,
#     each representing the source code of a Python function.
# --> Call the count_print_function_violation_linter function for each source
#     code string in the list.
# --> Create a dictionary where the key is the provided source code as a string
#     and the value is the integer value that was the output of the counting
#     function.
# --> Return the dictionary containing the source code strings and their
#     corresponding integer count violation results.

# TODO: These function(s) may not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by a software engineer
# using it.

def check_print_violations_in_functions(source_code_list, max_prints):
    violations_dict = {}
    return violations_dict


def count_print_violations_in_functions(source_code_list):
    violations_dict_count_mapping = {}
    return violations_dict_count_mapping

# }}}

# Part (d) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function description:
# The function get_overall_print_violation_linter should:
# --> Accept a single parameter, violations_dict, which is a dictionary where
#     the key is a string representing the source code of a Python function and
#     the value is a boolean indicating whether there is a print function
#     violation.
# --> Return a list of strings that represent the source code strings that have
#     overall print violations. A source code segment should appear in the list
#     if it is marked as having an overall print violation. Otherwise, it should
#     not appear in the list that is returned by this function.

# Function description:
# The function has_overall_print_violation_linter should:
# --> Accept a single parameter, violations_dict, which is a dictionary where
#     the key is a string representing the source code of a Python function and
#     the value is a boolean indicating whether there is a print function
#     violation.
# --> Iterate through the dictionary to check if there is at least one boolean
#     value of True.
# --> If there is at least one boolean value that is True, return True to
#     indicate that there is an overall violation in the program.
# --> If all of the values inside the dictionary are False, return False to
#     indicate that there are no overall violations in the program.

# TODO: The has_overall_print_violation_linter function should ensure that it
# correctly checks the dictionary values and returns the appropriate boolean
# result.

# TODO: These function(s) may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so that
# the function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


def get_overall_print_violation_linter(violations_dict):
    return [""]


def has_overall_print_violation_linter(violations_dict):
    return False


# }}}
