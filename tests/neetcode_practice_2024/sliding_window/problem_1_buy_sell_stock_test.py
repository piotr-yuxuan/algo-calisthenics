from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.problem_1_buy_sell_stock as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.lists(st.integers(min_value=-15)))
def test_solution(input):
    assert (
        problem.solution_brute_force(input)
        == problem.solution_intuitive(input)
        == problem.solution(input)
    )


def test_hard_coded():
    assert 6 == problem.solution_brute_force([10, 1, 5, 6, 7, 1])
    assert 0 == problem.solution_brute_force([10, 8, 7, 5, 2])
