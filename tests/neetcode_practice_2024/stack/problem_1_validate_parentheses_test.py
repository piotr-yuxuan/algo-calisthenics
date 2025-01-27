from hypothesis import given, strategies as st
import neetcode_practice_2024.stack.problem_1_validate_parentheses as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.from_regex(r"[\[\(\{\}\)\]]*"))
def test_solution(input):
    assert problem.solution(input) == problem.solution_from_neet_code(input)


def test_solution_hard_coded():
    assert problem.solution("[]") is True
    assert problem.solution("([{}])") is True
    assert problem.solution("[(])") is False
