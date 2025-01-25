from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.longest_substring_without_duplicates as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert (
        problem.solution_intuitive(input)
        == problem.solution_brute_force(input)
        == problem.solution_brute_force_unique_chars(input)
        == problem.solution_optimal(input)
    )


def test_solution_hard_coded():
    assert 3 == problem.solution_brute_force("zxyzxyz")
    assert 1 == problem.solution_brute_force("xxxx")
