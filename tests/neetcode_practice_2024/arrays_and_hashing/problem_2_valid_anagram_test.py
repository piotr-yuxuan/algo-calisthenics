from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_2_valid_anagram as problem
import random


@given(st.text(min_size=1))
def test_solutions_anagram(s):
    assert (
        True
        == problem.solution(s, s)
        == problem.solution_constant_space_sum(s, s)
        == problem.solution_constant_space_xor(s, s)
        == problem.solution_with_counters(s, s)
        == problem.solution_with_sorted(s, s)
        == problem.solution_constant_space_xor_reduce(s, s)
    )

    s_prime = list(s)
    i = random.randint(0, len(s) - 1)
    s_prime[i] = chr(ord(s_prime[i]) + 1)
    t = "".join(s_prime)

    assert (
        False
        == problem.solution(s, t)
        == problem.solution_constant_space_sum(s, t)
        == problem.solution_constant_space_xor(s, t)
        == problem.solution_with_counters(s, t)
        == problem.solution_with_sorted(s, t)
        == problem.solution_constant_space_xor_reduce(s, t)
    )
