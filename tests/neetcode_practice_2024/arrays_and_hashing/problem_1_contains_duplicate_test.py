from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_1_contains_duplicate as problem
from faker import Faker
from operator import itemgetter
import random


@given(st.lists(st.integers(), min_size=10))
def test_merge_sort_random_list_of_integers(l):
    original_list = list(l)
    random.shuffle(l)
    assert (
        sorted(original_list)
        == problem.merge_sort(l)
        == problem.merge_sort_bottom_up(l)
        == problem.merge_sort_dynamic_programming_tabulation(l)
    ), "list is poorly sorted"


@given(st.lists(st.integers(), min_size=10))
def test_merge_sort_random_list_of_integers_already_sorted(l):
    original_list = list(l)
    random.shuffle(l)
    assert (
        sorted(original_list)
        == problem.merge_sort(l)
        == problem.merge_sort_bottom_up(l)
        == problem.merge_sort_dynamic_programming_tabulation(l)
    ), "list is poorly sorted"


fake = Faker()


name_age_dict = st.fixed_dictionaries(
    {
        "name": st.builds(fake.name),
        "age": st.integers(
            min_value=0,
            max_value=100,
        ),
    }
)


@given(st.lists(name_age_dict, min_size=10))
def test_merge_sort_custom_key(l):
    original_list = list(l)
    random.shuffle(l)

    # Not stable sort? At least mapping on age focus on what we want to test.
    assert [
        person["age"] for person in sorted(original_list, key=itemgetter("age"))
    ] == [
        person["age"] for person in problem.merge_sort(l, key=itemgetter("age"))
    ], "list is poorly sorted"


@given(st.sets(st.integers(), min_size=10))
def test_solution_not_optimal(s):
    list_unique_items = list(s)
    list_duplicate_items = list(s)
    list_duplicate_items.append(list_duplicate_items[0])

    assert (
        True
        == problem.solution_not_optimal(list_unique_items)
        == problem.solution(list_unique_items)
    )
    assert (
        False
        == problem.solution_not_optimal(list_duplicate_items)
        == problem.solution(list_duplicate_items)
    )


def test_benchmark_solution_10(benchmark):
    benchmark(problem.solution, list(range(10)))


def test_benchmark_solution_100(benchmark):
    benchmark(problem.solution, list(range(100)))


def test_benchmark_solution_1000(benchmark):
    benchmark(problem.solution, list(range(100)))
