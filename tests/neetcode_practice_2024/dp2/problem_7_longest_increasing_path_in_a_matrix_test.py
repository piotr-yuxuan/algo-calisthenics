from hypothesis import given, strategies as st
import neetcode_practice_2024.dp2.problem_7_longest_increasing_path_in_a_matrix as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert problem.solution(input) is True
