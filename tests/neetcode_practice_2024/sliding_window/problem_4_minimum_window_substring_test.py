from hypothesis import given, strategies as st
import neetcode_practice_2024.sliding_window.problem_4_minimum_window_substring as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(
    st.from_regex(r"^[a-z]+$", fullmatch=True),
    st.from_regex(r"^[a-z]+$", fullmatch=True),
)
def test_solution_low_constraints(s, t):
    assert (
        problem.solution(s, t)
        == problem.solution_suboptimal(s, t)
        == problem.solution_from_neet_code(s, t)
        == problem.my_solution_updated_by_chatgpt(s, t)
    )


@given(
    st.from_regex(r"^[a-h]{40}$", fullmatch=True),
    st.from_regex(r"^[a-h]{4}$", fullmatch=True),
)
def test_solution_small_constraints(s, t):
    assert (
        problem.solution(s, t)
        == problem.solution_suboptimal(s, t)
        == problem.solution_from_neet_code(s, t)
        == problem.my_solution_updated_by_chatgpt(s, t)
    )


@given(
    st.from_regex(r"^[a-z]{500}$", fullmatch=True),
    st.from_regex(r"^[a-h]{1,5}$", fullmatch=True),
)
def test_solution_larger_s_smaller_t(s, t):
    assert (
        problem.solution(s, t)
        == problem.solution_suboptimal(s, t)
        == problem.solution_from_neet_code(s, t)
        == problem.my_solution_updated_by_chatgpt(s, t)
    )


def test_solution_hard_coded():
    assert "YXAZ" == problem.solution_suboptimal(s="OUZODYXAZV", t="XYZ")
    assert "xyz" == problem.solution_suboptimal(s="xyz", t="xyz")
    assert "xyz" == problem.solution_suboptimal(s="aaxbbycczaxyzeee", t="xyz")
