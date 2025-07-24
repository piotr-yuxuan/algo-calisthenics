#!/usr/bin/env python

import numpy as np
import numpy.linalg as linalg

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_straightforward(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

    for i in range(len(text1)):
        for j in range(len(text2)):

            if text1[i] == text2[j]:
                prior_ij = dp[i - 1][j - 1] if (0 <= j - 1 and 0 <= j - 1) else 0
                dp[i][j] = 1 + prior_ij
            else:
                prior_i = dp[i - 1][j] if 0 <= i - 1 else 0
                prior_j = dp[i][j - 1] if 0 <= j - 1 else 0

                dp[i][j] = max(prior_i, prior_j)
    return dp[-1][-1]


def solution_less_assignment_cost(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + (dp[i - 1][j - 1] if (0 <= j - 1 and 0 <= j - 1) else 0)
            else:
                dp[i][j] = max(
                    (dp[i - 1][j] if 0 <= i - 1 else 0),
                    (dp[i][j - 1] if 0 <= j - 1 else 0),
                )
    return dp[-1][-1]


def solution(a: str, b: str) -> int:
    la, lb = len(a) + 1, len(b) + 1
    p1 = [0] * lb
    p2 = [0] * lb
    for i in range(1, la):
        for j in range(1, lb):
            p2[j] = p1[j - 1] + 1 if a[i - 1] == b[j - 1] else max(p1[j], p2[j - 1])
        p1, p2 = p2, p1
    return p1[-1]


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
