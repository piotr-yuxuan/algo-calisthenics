#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar, Dict
import collections
import functools


def solution_suboptimal(s, t) -> str:
    n = len(s)
    target_frequencies = collections.Counter(t)

    # Keep track of these values:
    frequencies = collections.defaultdict(int)
    min_length = n + 1
    min_substring = ""

    def is_valid_substring(
        target_frequencies: Dict[str, int],
        frequencies: Dict[str, int],
    ) -> bool:
        """Work in progress, add complexity but should be simplified later."""
        if set() != set(target_frequencies.keys()) - set(frequencies.keys()):
            return False
        for k, v in target_frequencies.items():
            if not v <= frequencies[k]:
                return False
        return True

    left_bound, right_bound = 0, 0
    while right_bound < n:
        head = s[right_bound]
        frequencies[head] += 1

        while is_valid_substring(target_frequencies, frequencies):
            length = right_bound - left_bound + 1
            if length < min_length:
                min_length = length
                min_substring = s[left_bound : right_bound + 1]

            tail = s[left_bound]
            if frequencies[tail] - 1 < target_frequencies[tail]:
                break
            frequencies[tail] -= 1
            left_bound += 1

        right_bound += 1

    return min_substring


def solution(s, t) -> str:
    n = len(s)

    target_frequencies = collections.Counter(t)
    remaining_characters = set(target_frequencies.keys())

    # Keep track of these values:
    frequencies = collections.defaultdict(int)
    min_length = n + 1
    min_substring = ""

    left_bound, right_bound = 0, 0
    while right_bound < n:
        head = s[right_bound]
        frequencies[head] += 1
        if (
            head in remaining_characters
            and target_frequencies.get(head, 0) <= frequencies[head]
        ):
            remaining_characters.remove(head)

        while 0 == len(remaining_characters):
            length = right_bound - left_bound + 1
            if length < min_length:
                min_length = length
                min_substring = s[left_bound : right_bound + 1]

            tail = s[left_bound]
            if frequencies[tail] - 1 < target_frequencies[tail]:
                break
            frequencies[tail] -= 1
            left_bound += 1

        right_bound += 1

    return min_substring


def main(args):
    return solution_suboptimal(args.s1, args.s2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=", ".join(
            "Neetcode 2024",
            "sliding window",
            "problem 4 minimum window substring",
        )
    )
    parser.add_argument(
        "--s1",
        "-s",
        type=str,
        required=True,
        help="The first string, `s`.",
    )
    parser.add_argument(
        "--s2",
        "-t",
        type=str,
        required=True,
        help="The second string, `t`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
