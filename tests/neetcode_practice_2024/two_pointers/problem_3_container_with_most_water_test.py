from hypothesis import given, strategies as st
import neetcode_practice_2024.two_pointers.problem_3_container_with_most_water as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.lists(st.integers(min_value=1)))
def test_solution(input):
    assert (
        problem.solution_brute_force(input)
        == problem.solution_brute_force_comp(input)
        == problem.solution_two_pointers(input)
    )
