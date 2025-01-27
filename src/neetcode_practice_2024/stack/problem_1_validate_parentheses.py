#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution(input: str):
    delimiter_stop_match = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    delimiter_start = set(delimiter_stop_match.values())

    stack = list([])
    for character in input:
        if character in delimiter_start:
            stack.append(character)
        elif not stack or delimiter_stop_match.get(character, None) != stack.pop():
            return False
    return not stack


def solution_from_neet_code(s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


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
