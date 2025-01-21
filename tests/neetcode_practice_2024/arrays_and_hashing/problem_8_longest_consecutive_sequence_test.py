from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_8_longest_consecutive_sequence as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(
    st.sets(
        st.integers(
            min_value=0,
            max_value=15,
        ),
        min_size=10,
    )
)
def test_solution(input_set):
    input = list(input_set)
    sorted(input)

    assert problem.solution_hashset(input)


def test_solution_hard_coded():
    assert 0 == problem.solution_hashset([])
    assert (
        1
        == problem.solution_hashset([0])
        == problem.solution_hashset([1])
        == problem.solution_hashset([0, 2])
        == problem.solution_hashset([2, 4, 6])
    )
    assert (
        2
        == problem.solution_hashset([1, 2])
        == problem.solution_hashset([0, 1])
        == problem.solution_hashset([0, 2, 3, 5])
        == problem.solution_hashset([0, 2, 4, 5])
        == problem.solution_hashset([0, 1, 3, 4, 6, 7])
    )
    assert (
        3
        == problem.solution_hashset([1, 2, 3])
        == problem.solution_hashset([0, 1, 2])
        == problem.solution_hashset([6, 7, 8])
    )
