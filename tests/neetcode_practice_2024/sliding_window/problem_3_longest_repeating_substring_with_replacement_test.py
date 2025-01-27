from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.problem_3_longest_repeating_substring_with_replacement as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)

input_regex = r"^[a-z]*$"


@given(
    st.from_regex(r"^[a-z]{30}$", fullmatch=True),
    st.integers(min_value=1, max_value=2),
)
def test_solution_constrained_small_k(input, k):
    assert (
        problem.solution_brute_force(input, k)
        == problem.solution_sliding_window_first(input, k)
        == problem.solution_sliding_window_second(input, k)
    )


@given(
    st.from_regex(r"^[a-z]{30}$", fullmatch=True),
    st.integers(min_value=3, max_value=6),
)
def test_solution_constrained_larger_k(input, k):
    assert (
        problem.solution_brute_force(input, k)
        == problem.solution_sliding_window_first(input, k)
        == problem.solution_sliding_window_second(input, k)
    )


@given(
    st.from_regex(input_regex, fullmatch=True),
    st.integers(min_value=1),
)
def test_solution(input, k):
    assert (
        problem.solution_brute_force(input, k)
        == problem.solution_sliding_window_first(input, k)
        == problem.solution_sliding_window_second(input, k)
    )


def test_hard_coded():
    assert 4 == problem.solution_brute_force("XYYX", k=2)
    assert 5 == problem.solution_brute_force("AAABABB", k=1)
    assert 5 == problem.solution_brute_force("AAABABBBCD", k=1)
    assert 6 == problem.solution_brute_force("AAABABBBCD", k=2)
    assert 4 == problem.solution_brute_force("ABCDEFGH", k=3)
