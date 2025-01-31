#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_two_pointers_even_palindromes_only(input: str) -> int:
    n = len(input)

    # Track these values:
    palindrom_count = 0

    for i in range(n):
        l, r = i, i

        while 0 <= l and r < n and input[l] == input[r]:
            palindrom_count += 1

            l -= 1
            r += 1

    return palindrom_count


def solution_two_pointers(input: str) -> int:
    n = len(input)

    # Track these values:
    palindrom_count = 0

    def _while_palindrome(l, r):
        nonlocal palindrom_count

        while 0 <= l and r < n and input[l] == input[r]:
            palindrom_count += 1

            l -= 1
            r += 1

    for i in range(n):
        _while_palindrome(i, i)
        _while_palindrome(i, i + 1)

    return palindrom_count


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
