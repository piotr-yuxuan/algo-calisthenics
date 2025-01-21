from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_8_longest_consecutive_sequence as problem
import random
import itertools
import string

from typing import List, Set

import importlib

importlib.reload(problem)


@given(st.lists(st.integers()))
def test_solution(input):
    assert problem.solution_hashset(input) == problem.solution_hashmap(input)


def test_solution_hard_coded():
    assert 0 == problem.solution_hashset([])
    assert (
        1
        == problem.solution_hashset([0])
        == problem.solution_hashset([1])
        == problem.solution_hashset([0, 2])
        == problem.solution_hashset([2, 4, 6])
    )
    assert (
        2
        == problem.solution_hashset([1, 2])
        == problem.solution_hashset([0, 1])
        == problem.solution_hashset([0, 2, 3, 5])
        == problem.solution_hashset([0, 2, 4, 5])
        == problem.solution_hashset([0, 1, 3, 4, 6, 7])
    )
    assert (
        3
        == problem.solution_hashset([1, 2, 3])
        == problem.solution_hashset([0, 1, 2])
        == problem.solution_hashset([6, 7, 8])
    )


class TestLongestSequence:
    @given(st.integers(), st.integers(max_value=50))
    def test_non_existing_current_value_returns_current_length(
        self,
        current_length,
        current_value,
    ):
        assert current_length == problem.longest_sequence(
            values=set([]),
            known_lengths=dict(),
            current_value=current_value,
            current_length=current_length,
        )

        assert current_length == problem.longest_sequence(
            values=set(range(current_value)),
            known_lengths=dict(),
            current_value=current_value,
            current_length=current_length,
        )

    @given(st.sets(st.integers(), min_size=1))
    def test_retrieve_known_length(self, values_set: Set[int]):
        values = list(values_set)
        known_lengths = {values[i]: i for i in range(len(values))}
        current_value = random.choice(values)

        assert known_lengths[current_value] == problem.longest_sequence(
            values=set(values),
            known_lengths=known_lengths,
            current_value=current_value,
            current_length=0,
        )

    @given(st.sets(st.integers(), min_size=1), st.integers())
    def test_retrieve_known_length_with_current_length(
        self,
        values_set: Set[int],
        current_length,
    ):
        values = list(values_set)
        known_lengths = {values[i]: i for i in range(len(values))}
        current_value = random.choice(values)

        assert known_lengths[
            current_value
        ] + current_length == problem.longest_sequence(
            values=set(values),
            known_lengths=known_lengths,
            current_value=current_value,
            current_length=current_length,
        )

    @given(
        st.integers(min_value=3, max_value=50),
        st.integers(min_value=1),
    )
    def test_longest_sequence_one_long_range(
        self,
        upper_bound,
        current_length,
    ):
        values = list(range(upper_bound))
        random.shuffle(values)
        current_value = random.choice(values)
        result = problem.longest_sequence(
            values=set(values),
            known_lengths=dict({}),
            current_value=current_value,
            current_length=current_length,
        )

        assert upper_bound - current_value + current_length == result
