from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_4_longest_palindromic_substring as problem
from neetcode_practice_2024.dp1.problem_4_longest_palindromic_substring import (
    _is_palindrome,
    _is_palindrome_index,
)
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert problem.solution_brute_force(input) == problem.solution_neet_code(input)


@given(st.text(min_size=1))
def test__is_palindrome(input: str):
    expected = _is_palindrome(input)
    assert expected == _is_palindrome_index(input, 0, len(input))
    assert expected == _is_palindrome_index(input + input, 0, len(input))
    assert expected == _is_palindrome_index(input + input, len(input), 2 * len(input))
    assert expected == _is_palindrome_index("_" + input, 1, 1 + len(input))
    assert expected == _is_palindrome_index(input + "_", 0, len(input))
