from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.longest_repeating_substring_with_replacement as problem
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
