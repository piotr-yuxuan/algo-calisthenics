from hypothesis import given, strategies as st
import {{ xxx_module_path }} as problem
import random


@given(st.text(min_size=1))
def test_solution():
    assert (
        True
        == problem.solution(s, s)
    )
