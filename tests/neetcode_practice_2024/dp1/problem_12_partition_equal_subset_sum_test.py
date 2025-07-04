from hypothesis import given, strategies as st
import neetcode_practice_2024.dp1.problem_12_partition_equal_subset_sum as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert problem.solution(input) is True
