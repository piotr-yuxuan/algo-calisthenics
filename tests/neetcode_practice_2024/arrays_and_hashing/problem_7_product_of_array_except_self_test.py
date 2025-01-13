from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_7_product_of_array_except_self as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)
problem.solution_brute_force([1, 2, 3, 4])


@given(st.lists(st.integers(min_value=1, max_value=15), max_size=6))
def test_solution(input):
    assert (
        problem.solution_brute_force(input)
        == problem.solution_divide_by_self(input)
        == problem.solution_affix(input)
        == problem.solution_greedy(input)
    )


def test_hard_code_solution_brute_force():
    assert [1] == problem.solution_brute_force([1])
    assert [12, 6, 4, 6, 12] == problem.solution_brute_force([1, 2, 3, 2, 1])
    assert [6, 12, 24, 8] == problem.solution_brute_force([4, 2, 1, 3])
