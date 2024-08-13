import argparse
from typing import Counter
import argcomplete
import functools


def solution(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    d = dict()
    for i in s1:
        d[i] = d.get(i, 0) + 1
    for i in s2:
        d[i] = d.get(i, 0) - 1
        if d[i] == 0:
            d.pop(i)
    return not d


def solution_with_counters(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def solution_with_sorted(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def solution_constant_space_sum(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sum(map(ord, s1)) == sum(map(ord, s2))


def solution_constant_space_xor(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    acc = 0
    for c1, c2 in zip(s1, s2):
        acc ^= ord(c1)
        acc ^= ord(c2)
    return 0 == acc


def solution_constant_space_xor_reduce(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    xor = lambda x, y: x ^ y
    return 0 == functools.reduce(
        xor,
        map(ord, s1),
        functools.reduce(
            xor,
            map(ord, s2),
        ),
    )


def main(args):
    return solution(args.string_one, args.string_two)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, arrays and string, problem 2: valid anagram."
    )
    parser.add_argument(
        "--string-one",
        "-1",
        type=str,
        required=True,
        help="The first string.",
    )
    parser.add_argument(
        "--string-two",
        "-2",
        type=str,
        required=True,
        help="The second string.",
    )
    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
