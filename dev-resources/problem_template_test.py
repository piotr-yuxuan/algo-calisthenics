from hypothesis import given, strategies as st
import neetcode_practice_2024.XXX as problem
import random


@given(st.text(min_size=1))
def test_solution):
    assert (
        True
        == problem.solution(s, s)
    )
