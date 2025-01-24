#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Dict, Set, Optional, Protocol, TypeVar
import collections
import functools


def longest_sequence(
    values: Set[int],
    known_lengths: Dict[int, int],
    current_value: int,
) -> int:
    if current_value in known_lengths:
        return known_lengths[current_value]

    if current_value not in values:
        return 0

    next_value = 1 + current_value
    if next_value in values:
        known_lengths[next_value] = longest_sequence(
            values,
            known_lengths,
            next_value,
        )
        return 1 + known_lengths[next_value]
    else:
        known_lengths[current_value] = 1
        return known_lengths[current_value]


def solution_dp_top_down(input: List[int]) -> int:
    if not input:
        return 0

    values = set(input)
    known_lengths = dict({})

    return max(
        [
            longest_sequence(values, known_lengths, current_value)
            for current_value in values
        ],
    )


def solution_hashset(input: List[int]) -> int:
    known = set(input)
    longest = 0
    for i in known:
        value = i
        length = 1
        while value + 1 in known:
            value += 1
            length += 1
        longest = max(length, longest)
    return longest


def solution_dp_bottom_up(input: List[int]) -> int:
    if not input:
        return 0

    # Memoisation cache where the key is an integer from the input,
    # and the value is the length of the consecutive sequence that
    # includes that integer.
    dp = collections.defaultdict(int)

    for current_value in input:
        if dp[current_value]:
            continue

        previous_value = current_value - 1
        next_value = current_value + 1
        dp[current_value] = dp[previous_value] + 1 + dp[next_value]

        start_of_sequence = current_value - dp[previous_value]
        end_of_sequence = current_value + dp[next_value]
        dp[start_of_sequence] = dp[current_value]
        dp[end_of_sequence] = dp[current_value]

    return max(dp.values())


def main(args):
    return solution_hashset(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Neetcode 2024, arrays and strings, "
            "problem 8 longest consecutive sequence."
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
