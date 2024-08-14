from hypothesis import given, strategies as st
import neetcode_practice_2024.arrays_and_hashing.problem_4_anagram_groups as problem
import itertools

import string
import importlib

importlib.reload(problem)


@given(
    st.sets(
        st.text(
            alphabet=st.characters(min_codepoint=ord("a"), max_codepoint=ord("z")),
            min_size=1,
            max_size=5,
        ),
        min_size=1,
        max_size=5,
    )
)
def test_solution(l):
    input = ["".join(x) for s in l for x in list(itertools.permutations(s))]
    expected = [
        sorted(["".join(x) for x in list(itertools.permutations(s))]) for s in l
    ]
    expected.sort()

    actual = [sorted(i) for i in problem.solution(input)]
    actual.sort()

    actual2 = [sorted(i) for i in problem.solution_naive(input)]
    actual2.sort()

    actual3 = [sorted(i) for i in problem.solution_character_counting(input)]
    actual3.sort()

    actual4 = [sorted(i) for i in problem.solution_trie_based(input)]
    actual4.sort()

    assert expected == actual
    assert expected == actual2
    assert expected == actual3
    assert expected == actual4


def test_trie_node():
    node = problem.Node()
    assert isinstance(node, problem.Node)
    assert isinstance(node.children["_"], problem.Node)
    node.values.append(1)
    assert node.values == [1]


def test_trie():
    t = problem.Trie()
    for path, v in [
        (
            list(range(i)),
            string.ascii_lowercase[i],
        )
        for i in range(len(string.ascii_lowercase))
    ]:
        t.insert(path, v)
    for path, values in [
        (
            list(range(i)),
            list(map(lambda x: [x], string.ascii_lowercase[i:])),
        )
        for i in range(len(string.ascii_lowercase))
    ]:
        assert t.values_under(path) == values
