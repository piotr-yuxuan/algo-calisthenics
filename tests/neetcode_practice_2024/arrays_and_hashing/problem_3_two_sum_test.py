from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_3_two_sum as problem
import random


@given(st.sets(st.integers(), min_size=2))
def test_solution(s):
    input = list(s)
    i, j = random.sample(range(len(input)), 2)
    problem.solution(input, input[i] + input[j])
    assert i, j == problem.solution(input, input[i] + input[j])
