from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.problem_4_minimum_window_substring as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution(input):
    assert 1 == 1


def test_solution_hard_coded():
    assert "YXAZ" == problem.solution_suboptimal(s="OUZODYXAZV", t="XYZ")
    assert "xyz" == problem.solution_suboptimal(s="xyz", t="xyz")
    assert "xyz" == problem.solution_suboptimal(s="aaxbbycczaxyzeee", t="xyz")
