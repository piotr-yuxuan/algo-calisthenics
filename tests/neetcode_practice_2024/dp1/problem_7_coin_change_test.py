from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_7_coin_change as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(
    st.lists(
        st.integers(
            min_value=1,
            max_value=2**31 - 1,
        ),
        min_size=1,
        max_size=10,
    ),
    st.integers(
        min_value=0,
        max_value=10,
        # max_value=10e3,
    ),
)
def test_solution(nums, target_sum):

    assert (
        problem.solution_from_neet_code(nums, target_sum)
        == problem.solution_top_down(nums, target_sum)
    )


def test_solution_hard_coded():
    assert 3 == problem.solution_top_down([1, 5, 10], 12)
    assert -1 == problem.solution_top_down([2], 3)
    assert 0 == problem.solution_top_down([2], 0)
    assert 0 == problem.solution_top_down([], 3)
