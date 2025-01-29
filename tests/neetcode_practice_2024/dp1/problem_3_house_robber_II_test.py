from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_3_house_robber_II as problem
import random
import itertools
import string

import importlib
importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert (
        problem.solution(input) is True
    )


def test_solution_hard_coded():
    assert problem.solution_first_attempt([2, 9, 8, 3, 6]) == 15
    assert problem.solution_first_attempt([3, 4, 3]) == 4
