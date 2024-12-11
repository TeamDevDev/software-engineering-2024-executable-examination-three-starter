"""Confirm the correctness of functions in question_four."""

import pytest

# ruff: noqa: PLR2004
from questions.question_four import (
    FunctionDetails,
    Module,
    calculate_average_cyclomatic_complexity,
    calculate_maximum_cyclomatic_complexity,
    calculate_minimum_cyclomatic_complexity,
    determine_looks_good_to_merge_cyclomatic_complexity,
    determine_looks_good_to_merge_human_approval,
    get_approved_functions,
    get_not_approved_functions,
)


@pytest.mark.question_four_part_a
def test_get_approved_functions():
    """Test for a question part."""
    # create a list of function details
    functions = [
        FunctionDetails(id=1, name="func1", approved=True),
        FunctionDetails(id=2, name="func2", approved=False),
        FunctionDetails(id=3, name="func3", approved=True),
        FunctionDetails(id=4, name="func4", approved=False),
    ]
    # create a module with the list of functions
    module = Module(functions=functions)
    # get the approved functions
    approved_functions = get_approved_functions(module)
    # check the number of approved functions
    assert len(approved_functions) == 2, "Should return 2 approved functions"
    # check the first approved function
    assert approved_functions[0].id == 1, "First approved function should have id 1"
    assert (
        approved_functions[0].name == "func1"
    ), "First approved function should have name 'func1'"
    assert (
        approved_functions[0].approved is True
    ), "First approved function should be approved"
    # check the second approved function
    assert approved_functions[1].id == 3, "Second approved function should have id 3"
    assert (
        approved_functions[1].name == "func3"
    ), "Second approved function should have name 'func3'"
    assert (
        approved_functions[1].approved is True
    ), "Second approved function should be approved"


@pytest.mark.question_four_part_a
def test_get_not_approved_functions():
    """Test for a question part."""
    # create a list of function details
    functions = [
        FunctionDetails(id=1, name="func1", approved=True),
        FunctionDetails(id=2, name="func2", approved=False),
        FunctionDetails(id=3, name="func3", approved=True),
        FunctionDetails(id=4, name="func4", approved=False),
    ]
    # create a module with the list of functions
    module = Module(functions=functions)
    # get the approved functions
    not_approved_functions = get_not_approved_functions(module)
    # check the number of not approved functions
    assert len(not_approved_functions) == 2, "Should return 2 not approved functions"
    # check the first not approved function
    assert (
        not_approved_functions[0].id == 2
    ), "First not approved function should have id 2"
    assert (
        not_approved_functions[0].name == "func2"
    ), "First not approved function should have name 'func2'"
    assert (
        not_approved_functions[0].approved is False
    ), "First not approved function should not be approved"
    # check the second not approved function
    assert (
        not_approved_functions[1].id == 4
    ), "Second not approved function should have id 4"
    assert (
        not_approved_functions[1].name == "func4"
    ), "Second not approved function should have name 'func4'"
    assert (
        not_approved_functions[1].approved is False
    ), "Second not approved function should not be approved"


@pytest.mark.question_four_part_b
def test_determine_if_module_looks_good_to_merge_no_way():
    """Test for a question part."""
    # create a list of function details
    functions = [
        FunctionDetails(id=1, name="func1", approved=True),
        FunctionDetails(id=2, name="func2", approved=False),
        FunctionDetails(id=3, name="func3", approved=True),
        FunctionDetails(id=4, name="func4", approved=False),
    ]
    # create a module with the list of functions
    module = Module(functions=functions)
    # get the approved functions
    not_merge_candidate = determine_looks_good_to_merge_human_approval(module)
    assert not_merge_candidate is False, "Module should not look good to merge"


@pytest.mark.question_four_part_b
def test_determine_if_module_looks_good_to_merge_yes_way():
    """Test for a question part."""
    # create a list of function details
    functions = [
        FunctionDetails(id=1, name="func1", approved=True),
        FunctionDetails(id=2, name="func2", approved=True),
        FunctionDetails(id=3, name="func3", approved=True),
        FunctionDetails(id=4, name="func4", approved=True),
    ]
    # create a module with the list of functions
    module = Module(functions=functions)
    # get the approved functions
    not_merge_candidate = determine_looks_good_to_merge_human_approval(module)
    assert not_merge_candidate is True, "Module should look good to merge"


@pytest.mark.question_four_part_c
def test_cyclomatic_complexity_functions():
    """Test for a question part."""
    # create a list of function details with cyclomatic complexity
    functions = [
        (1, "func1", 5),
        (2, "func2", 3),
        (3, "func3", 7),
        (4, "func4", 2),
        (5, "func5", 4),
    ]
    # test minimum cyclomatic complexity
    min_complexity = calculate_minimum_cyclomatic_complexity(functions)
    assert min_complexity == 2, "Minimum cyclomatic complexity should be 2"
    # test average cyclomatic complexity
    avg_complexity = calculate_average_cyclomatic_complexity(functions)
    assert avg_complexity == pytest.approx(
        4.2, 0.01
    ), "Average cyclomatic complexity should be 4.2"
    # test maximum cyclomatic complexity
    max_complexity = calculate_maximum_cyclomatic_complexity(functions)
    assert max_complexity == 7, "Maximum cyclomatic complexity should be 7"
    # test with an empty list
    empty_functions = []
    with pytest.raises(ValueError, match="The list of functions is empty"):
        calculate_minimum_cyclomatic_complexity(empty_functions)


@pytest.mark.question_four_part_d
def test_cyclomatic_complexity_functions_approved_for_merge():
    """Test for a question part."""
    # create a list of function details with cyclomatic complexity
    functions = [
        (1, "func1", 5),
        (2, "func2", 3),
        (3, "func3", 7),
        (4, "func4", 2),
        (5, "func5", 4),
    ]
    merge = determine_looks_good_to_merge_cyclomatic_complexity(functions, 1)
    assert not merge, "Cannot merge when the threshold is set to 1"
    merge = determine_looks_good_to_merge_cyclomatic_complexity(functions, 7)
    assert not merge, "Cannot merge when the threshold is set to 7"
    merge = determine_looks_good_to_merge_cyclomatic_complexity(functions, 8)
    assert merge, "Can merge when the threshold is set to 8"
    merge = determine_looks_good_to_merge_cyclomatic_complexity(functions, 10)
    assert merge, "Can merge when the threshold is set to 10"
    # test with an empty list
    empty_functions = []
    with pytest.raises(ValueError, match="The list of functions is empty"):
        determine_looks_good_to_merge_cyclomatic_complexity(empty_functions, 1000)
