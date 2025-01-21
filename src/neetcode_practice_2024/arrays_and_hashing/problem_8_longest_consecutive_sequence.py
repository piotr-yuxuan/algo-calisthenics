#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_hashset(input: List[int]) -> int:
    known = set(input)
    longest = 0
    for i in input:
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
