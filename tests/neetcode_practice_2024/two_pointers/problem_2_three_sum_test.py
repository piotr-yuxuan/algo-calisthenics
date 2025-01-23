from hypothesis import given, strategies as st
import neetcode_practice_2024.two_pointers.problem_2_three_sum as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(
    st.lists(
        st.integers(
            min_value=-15,
            max_value=15,
        ),
        min_size=10,
        max_size=15,
    )
)
def test_solution_few_duplicates(input):
    assert (
        problem.solution_three_loops(input)
        == problem.solution_two_loops(input)
        == problem.solution_two_loops_sorted(input)
        == problem.solution_two_pointers(input)
    )


@given(
    st.lists(
        st.integers(
            min_value=-5,
            max_value=5,
        ),
        min_size=50,
        max_size=75,
    )
)
def test_solution_more_duplicates(input):
    assert (
        problem.solution_three_loops(input)
        == problem.solution_two_loops(input)
        == problem.solution_two_loops_sorted(input)
        == problem.solution_two_pointers(input)
    )


def test_hard_coded():
    input = [-1, 0, 1, 2, -1, -4]
    expected = {(-1, 0, 1), (-1, -1, 2)}
    assert expected == problem.solution_three_loops(input)
    assert expected == problem.solution_two_loops(input)
    assert expected == problem.solution_two_loops_sorted(input)
    assert expected == problem.solution_two_pointers(input)
