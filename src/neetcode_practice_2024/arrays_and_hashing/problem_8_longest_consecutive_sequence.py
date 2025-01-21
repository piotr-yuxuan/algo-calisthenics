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
    current_length: int,
) -> int:
    next_value = 1 + current_value
    if current_value in known_lengths:
        pass
    elif next_value in known_lengths:
        known_lengths[current_value] = 1 + known_lengths[next_value]
    elif next_value in values:
        return longest_sequence(
            values,
            known_lengths,
            next_value,
            1 + current_length,
        )
    elif current_value in values:
        known_lengths[current_value] = 1
    else:
        return current_length

    return current_length + known_lengths[current_value]


def solution_hashmap_dynamic_programming_top_down(input: List[int]) -> int:
    values = set(input)
    known_lengths = dict({})
    current_length = 0
    longest = 0

    for current_value in values:
        longest = max(
            longest,
            longest_sequence(
                values,
                known_lengths,
                current_value,
                current_length,
            ),
        )
    return longest


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


def main(args):
    return solution_hashset(args.input)


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
