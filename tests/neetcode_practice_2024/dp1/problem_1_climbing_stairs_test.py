from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_1_climbing_stairs as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.integers(min_value=1, max_value=20))
def test_solution(n):
    assert (
        problem.solution_first(n)
        == problem.solution_second(n)
        == problem.solution_third(n)
        == problem.solution_bottom_up_first(n)
        == problem.solution_bottom_up_second(n)
        == problem.solution(n)
    )
