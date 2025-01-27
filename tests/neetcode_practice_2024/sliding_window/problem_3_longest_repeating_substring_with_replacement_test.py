from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.problem_3_longest_repeating_substring_with_replacement as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert problem.solution(input) is True


def test_hard_coded():
    assert 4 == problem.solution_brute_force("XYYX", k=2)
    assert 5 == problem.solution_brute_force("AAABABB", k=1)
