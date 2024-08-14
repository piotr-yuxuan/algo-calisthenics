from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_4_anagram_groups as problem
import itertools


@given(st.sets(st.text(min_size=1, max_size=5), min_size=1, max_size=5))
def test_solution(l):
    input = ["".join(x) for s in l for x in list(itertools.permutations(s))]
    expected = [
        sorted(["".join(x) for x in list(itertools.permutations(s))]) for s in l
    ]
    actual = [sorted(i) for i in problem.solution(input)]

    expected.sort()
    actual.sort()
    assert expected == actual
