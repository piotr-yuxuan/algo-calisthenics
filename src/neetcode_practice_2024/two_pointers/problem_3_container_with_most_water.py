#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_brute_force(input: List[int]) -> int:
    n = len(input)
    # Keep track of these values:
    max_volume = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            distance = j - i
            left_bar = input[i]
            right_bar = input[j]
            volume = distance * min(left_bar, right_bar)
            max_volume = max(max_volume, volume)

    return max_volume


def solution_brute_force_comp(input: List[int]) -> int:
    n = len(input)

    if n < 2:
        return 0

    return max(
        [
            (j - i) * min(input[i], input[j])
            for i in range(n - 1)
            for j in range(i + 1, n)
        ]
    )


def solution_two_pointers(input: List[int]) -> int:
    n = len(input)

    if n < 2:
        return 0

    l, r = 0, n - 1
    # Keep track of these values:
    max_volume = 0

    while l < r:
        distance = r - l
        left_bar = input[l]
        right_bar = input[r]

        volume = distance * min(left_bar, right_bar)
        print(volume)
        max_volume = max(max_volume, volume)

        if left_bar <= right_bar:
            l += 1
        if right_bar <= left_bar:
            r -= 1

    return max_volume


def solution(input: List[int]) -> int:
    pass


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Neetcode 2024, XXX, problem XXX.")
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="XXX",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
