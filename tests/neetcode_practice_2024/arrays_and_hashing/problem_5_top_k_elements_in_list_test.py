from typing import Counter
from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_5_top_k_elements_in_list as problem

import importlib

importlib.reload(problem)


@given(
    st.lists(st.integers(), min_size=6),
    st.integers(min_value=1, max_value=5),
)
def test_all_implementations_agree(array, k):
    # Remove elements that appear at the same frequency.
    single_value_per_frequency = {freq: i for i, freq in Counter(array).items()}
    input = [i for i in array if i in single_value_per_frequency.values()]
    assert (
        set(problem.solution(input, k))
        == set(problem.solution_std_minheap(input, k))
        == set(problem.solution_stdlib(input, k))
    )


def test_hard_coded_example():
    input = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7]
    assert (
        set(problem.solution_std_minheap(input, 2))
        == set(problem.solution_stdlib(input, 2))
        == set(problem.solution(input, 2))
    )


@given(st.lists(st.integers(), min_size=6))
def test_trie_implementation(numbers):
    heap = []
    for i in numbers:
        problem.heap_insert(heap, i)
    actual = []
    while heap:
        value = problem.heap_extract(heap)
        actual.append(value)
    assert sorted(numbers) == actual
