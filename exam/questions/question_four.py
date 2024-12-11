"""Question Four: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import List

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

# Using the provided implementation of the FunctionDetails and Module classes,
# implement the following function called get_approved_functions. This function
# should take a Module instance as an argument and return a list of approved
# functions from the module. You should also implement a function called
# get_not_approved_functions that takes a Module instance as an argument and
# returns a list of functions that are not approved.

# TODO: These function(s) may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


class FunctionDetails:
    """A class to represent details about a function in a module."""

    def __init__(self, id: int, name: str, approved: bool):
        """Initialize the function details with the provided values."""
        self.id = id
        self.name = name
        self.approved = approved

    def __repr__(self):
        """Return a string representation of the function details."""
        return f"FunctionDetails(id={self.id}, name='{self.name}', approved={self.approved})"

    def __str__(self):
        """Return a string representation of the function details."""
        return self.__repr__()


class Module:
    """A class to represent a module with a list of function details."""

    def __init__(self, functions: List[FunctionDetails]):
        """Initialize the module with a list of function details."""
        self.functions = functions

    def __repr__(self):
        """Return a string representation of the module."""
        return f"Module(functions={self.functions})"

    def __str__(self):
        """Return a string representation of the module."""
        return self.__repr__()

    def add_function(self, function: FunctionDetails):
        """Add a function to the module."""
        self.functions.append(function)

    def get_function_by_id(self, id: int) -> FunctionDetails:
        """Get a function by its unique identifier."""
        for function in self.functions:
            if function.id == id:
                return function
        raise ValueError(f"Function with id {id} not found")

    def get_approved_functions(self) -> List[FunctionDetails]:
        """Get a list of approved functions."""
        return [function for function in self.functions if function.approved]


def get_approved_functions(module: Module) -> List[FunctionDetails]:
    return []


def get_not_approved_functions(module: Module) -> List[FunctionDetails]:
    return []


# }}}

# Part (b) {{{

# Instructions: Implement a function called determine_looks_good_to_merge that
# takes as an argument a Module instance and returns a boolean value indicating
# whether the module looks good to merge. A module is considered "good to merge"
# if all of the functions in the module are approved.

# TODO: These function(s) may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.

def determine_looks_good_to_merge_human_approval(module):
    total_functions = len(module.functions)
    approved_functions = []
    return len(approved_functions) == total_functions

# }}}

# Part (c) {{{

# Instructions: Implement the following functions so that they adhere to all
# aspects of the following specification.

# --> calculate_minimum_cyclomatic_complexity: This function should take a list
# of function details as an argument and return the minimum cyclomatic complexity
# of the functions in the list.
# --> calculate_average_cyclomatic_complexity: This function should take a list
# of function details as an argument and return the average cyclomatic complexity
# of the functions in the list.
# --> calculate_maximum_cyclomatic_complexity: This function should take a list
# of function details as an argument and return the maximum cyclomatic complexity
# of the functions in the list.

# TODO: All of the aforementioned functions should accept as input a list of
# tuples where the components of the tuple are as follows:
# 1. The unique identifier of the function.
# 2. The name of the function.
# 3. The cyclomatic complexity of the function.
# Note that the elements of the tuple will always appear in the order that they
# appear in the above listing of values.

# TODO: These functions may not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by a software engineer
# using it.

def calculate_minimum_cyclomatic_complexity(functions):
    return 10


def calculate_average_cyclomatic_complexity(functions):
    return 10.0


def calculate_maximum_cyclomatic_complexity(functions):
    return 100.0

# }}}

# Part (d) {{{

# Instructions: Implement the function called
# determine_looks_good_to_merge_cyclomatic that confirms whether or not all of
# the provided functions have a cyclomatic complexity value that is strictly
# less than a specified threshold. The function should return True if all of the
# functions have a cyclomatic complexity value that is strictly less than the
# specified threshold and return False otherwise.

# TODO: The aforementioned function should accept as input a list of
# tuples where the components of the tuple are as follows:
# 1. The unique identifier of the function.
# 2. The name of the function.
# 3. The cyclomatic complexity of the function.
# Note that the elements of the tuple will always appear in the order that they
# appear in the above listing of values.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def determine_looks_good_to_merge_cyclomatic_complexity(functions, threshold):
    # this is like the person who approves every pull
    # request without carefully looking at the complexity of the code!
    return True


# }}}
