#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution(input) -> bool:
    left, right = 0, len(input) - 1
    while left < right:
        if input[left] != input[right]:
            return False
        left += 1
        right -= 1
    return True


def main(args):
    return solution(args.input)


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
