#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import functools


def solution(input: List[int], target: int):
    seen = dict()
    for i, j in enumerate(input):
        if target - j in seen:
            return seen[target - j], i
        else:
            seen[j] = seen.setdefault(j, i)
    return False


def main(args):
    return solution(args.input, args.target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, arrays and hashing, problem 3 two sum."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda x: list(map(int, x.split(","))),
        required=True,
        help="Input array",
    )
    parser.add_argument(
        "--t",
        "-t",
        type=int,
        required=True,
        help="Target integer",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
