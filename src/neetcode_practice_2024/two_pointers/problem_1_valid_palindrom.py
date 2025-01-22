#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_stack(input: str) -> bool:
    n = len(input)
    if n <= 1:
        return True
    stack = []
    stack.extend(input[: n // 2])
    for i in range((n + 1) // 2, n):
        item = stack.pop()
        if item != input[i]:
            return False
    return True


def solution_straightforward(input: str) -> bool:
    left, right = 0, len(input) - 1
    while left < right:
        if input[left] != input[right]:
            return False
        left += 1
        right -= 1
    return True


def main(args):
    return solution_straightforward(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, two pointers, problem 1 valid palindrom."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="The input string: `abc`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
