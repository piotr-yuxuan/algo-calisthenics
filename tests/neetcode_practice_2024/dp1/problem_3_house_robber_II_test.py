from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_3_house_robber_II as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.lists(st.integers(min_value=1), min_size=1))
def test_solution(nums):
    assert (
        problem.solution_from_neet_code(nums)
        == problem.solution_first_attempt(nums)
        == problem.solution_second_attempt(nums)
        == problem.solution_third_attempt(nums)
    )


def test_solution_hard_coded():
    assert problem.solution_first_attempt([2, 9, 8, 3, 6]) == 15
    assert problem.solution_first_attempt([3, 4, 3]) == 4
