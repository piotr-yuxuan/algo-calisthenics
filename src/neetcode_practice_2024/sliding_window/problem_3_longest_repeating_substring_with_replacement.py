#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_brute_force(input: str, k: int) -> int:
    n = len(input)
    if n <= k + 1:
        return True

    # Keep track of these values:
    max_length = 0

    def criterion(substring: str, k: int) -> bool:
        if len(substring) <= k + 1:
            return True
        # This is not linear time since we iterate over the substring
        # every time.
        frequencies = collections.Counter(substring)
        max_frequency = max(frequencies.values())
        return len(substring) - max_frequency <= k

    for left_bound in range(n):
        for right_bound in range(left_bound, n + 1):
            substring = input[left_bound:right_bound]
            if not criterion(substring, k):
                break

            length = len(substring)
            max_length = max(max_length, length)

    return max_length


def solution_sliding_window_first(input: str, k: int) -> int:
    n = len(input)
    if n <= k + 1:
        return True

    # Keep track of these values:
    max_length = 0

    def criterion(substring: str, k: int) -> bool:
        if len(substring) <= k + 1:
            return True
        frequencies = collections.Counter(substring)
        max_frequency = max(frequencies.values())
        return len(substring) - max_frequency <= k

    left_bound, right_bound = 0, 0
    while right_bound <= n:
        substring = input[left_bound:right_bound]
        if criterion(substring, k):
            length = len(substring)
            max_length = max(max_length, length)
            right_bound += 1
        elif left_bound < right_bound:
            left_bound += 1

    return max_length


def solution_sliding_window_second(input: str, k: int) -> int:
    n = len(input)
    if n <= k + 1:
        return True

    # Keep track of these values:
    max_length = 0

    def criterion(substring: str, k: int, frequencies) -> bool:
        if len(substring) <= k + 1:
            return True
        max_frequency = max(frequencies.values())
        return len(substring) - max_frequency <= k

    left_bound, right_bound = 0, 1
    frequencies = collections.defaultdict(int)
    while right_bound < n + 1:
        frequencies[input[right_bound - 1]] += 1
        while not criterion(input[left_bound:right_bound], k, frequencies):
            if not left_bound < right_bound:
                break
            frequencies[input[left_bound]] -= 1
            left_bound += 1

        length = len(input[left_bound:right_bound])
        max_length = max(max_length, length)
        right_bound += 1

    return max_length


def solution_sliding_window_third(input: str, k: int) -> int:
    n = len(input)
    if n <= k + 1:
        return True

    # Keep track of these values:
    max_length = 0
    max_frequency = 0

    def criterion(substring: str, k: int, max_frequency) -> bool:
        return len(substring) - max_frequency <= k

    left_bound, right_bound = 0, 1
    frequencies = collections.defaultdict(int)
    while right_bound < n + 1:
        head_character = input[right_bound - 1]
        frequencies[head_character] += 1
        max_frequency = max(max_frequency, frequencies[head_character])

        while not criterion(input[left_bound:right_bound], k, max_frequency):
            if not left_bound < right_bound:
                break
            frequencies[input[left_bound]] -= 1
            left_bound += 1

        length = len(input[left_bound:right_bound])
        max_length = max(max_length, length)
        right_bound += 1

    return max_length


def solution(input):
    return True


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=", ".join(
            "Neetcode 2024",
            "XXX",
            "problem XXX.",
        )
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda s: [int(i) for i in s.split(",")],
        required=True,
        help="The input array as a comma-separated list of integers: `1,2,3`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
