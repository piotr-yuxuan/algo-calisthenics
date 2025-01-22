from hypothesis import given, strategies as st
import neetcode_practice_2024.two_pointers.problem_1_valid_palindrom as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution_valid(half):
    input = half + "".join(reversed(half))
    assert problem.solution(input) is True


@given(st.text(min_size=1))
def test_solution_invalid(half):
    input = half + "".join(reversed(half)) + "__"
    assert problem.solution(input) is False


def test_solution_hardcoded():
    assert problem.solution("") is True
    assert problem.solution("a") is True
    assert problem.solution("aa") is True
    assert problem.solution("aba") is True
    assert problem.solution("abba") is True
    assert problem.solution("abab") is False
    assert problem.solution("a ") is False
    assert problem.solution(" a") is False
