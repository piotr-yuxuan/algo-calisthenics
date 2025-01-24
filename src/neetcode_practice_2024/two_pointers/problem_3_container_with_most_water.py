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

    def volume_between_two_bars(input, left_position, right_position):
        distance = right_position - left_position
        return distance * min(input[right_position], input[left_position])

    return max(
        [
            volume_between_two_bars(input, i, j)
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

    def volume_between_two_bars(l, r, left_bar, right_bar):
        distance = r - l
        return distance * min(left_bar, right_bar)

    while l < r:
        left_bar = input[l]
        right_bar = input[r]

        max_volume = max(
            max_volume,
            volume_between_two_bars(
                l,
                r,
                left_bar,
                right_bar,
            ),
        )

        if left_bar <= right_bar:
            l += 1
        if right_bar <= left_bar:
            r -= 1

    return max_volume


def solution(input: List[int]) -> int:
    return solution_two_pointers(input)


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
