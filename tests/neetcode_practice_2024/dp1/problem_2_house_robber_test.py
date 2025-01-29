from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_2_house_robber as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(
    st.lists(
        st.integers(min_value=1),
        min_size=1,
    )
)
def test_solution(input):
    assert (
        problem.solution_first_attempt(input)
        == problem.solution_second_attempt(input)
        == problem.solution_third_attempt(input)
        == problem.solution(input)
    )


def solution_hard_coded(input):
    assert 16 == problem.solution_first_attempt([2, 9, 8, 3, 6])
    assert 4 == problem.solution_first_attempt([1, 1, 3, 3])
