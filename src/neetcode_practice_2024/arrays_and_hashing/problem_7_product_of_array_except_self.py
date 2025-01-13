#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_brute_force(input: List[int]) -> List[int]:
    n = len(input)
    output = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                output[i] *= input[j]

    return output


def solution_divide_by_self(input: List[int]) -> List[int]:
    n = len(input)
    total = functools.reduce(lambda x, acc: x * acc, input, 1)

    return [int(total / input[i]) for i in range(n)]


def solution_affix(input: List[int]) -> List[int]:
    n = len(input)
    l = [1] * n
    r = [1] * n

    for i in range(1, n):
        l[i] = l[i - 1] * input[i - 1]

    for i in range(n - 2, -1, -1):
        r[i] = r[i + 1] * input[i + 1]

    return [l[i] * r[i] for i in range(n)]


def solution_greedy(input: List[int]) -> List[int]:
    n = len(input)
    output = [1] * n

    tmp = 1
    for i in range(0, n):
        # Multiplication with 1 * is easier to read.
        output[i] *= tmp
        tmp *= input[i]

    tmp = 1
    for i in range(n - 1, -1, -1):
        output[i] *= tmp
        tmp *= input[i]

    return output


def solution(input: List[int]) -> List[int]:
    return input


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, product of array except self, problem 7."
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
