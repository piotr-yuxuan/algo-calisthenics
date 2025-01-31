from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_6_decode_ways as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.from_regex(r"[0-9]+", fullmatch=True))
def test_solution(input):
    assert problem.solution_from_neet_code(input) == problem.solution_top_down(input)
