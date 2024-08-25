from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_6_string_encode_and_decode as problem

import importlib

importlib.reload(problem)


@given(st.lists(st.text(min_size=1), min_size=1))
def test_round_trip(input):
    assert input == problem.decode(problem.encode(input))


def test_hard_coded():
    input = ["aze", "zer", "ert", "rty", "tyu"]
    assert "3:aze3:zer3:ert3:rty3:tyu" == problem.encode(input)
    assert input == problem.decode(problem.encode(input))
