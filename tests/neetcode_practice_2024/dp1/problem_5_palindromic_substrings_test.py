from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_5_palindromic_substrings as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert problem.solution(input) == problem.solution_from_neet_code(input)


def test_solution_hard_coded():
    assert 6 == problem.solution_two_pointers("aaa")
    assert 3 == problem.solution_two_pointers("abc")
