#!/usr/bin/env python

import numpy as np
import numpy.linalg as linalg

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


import functools


# Beats 88.82 %.
def solution_from_(s: str, t: str) -> int:
    m, n = len(t), len(s)
    if m > n:
        return 0

    dp = [0] * (m + 1)
    dp[0] = 1  # empty t is subsequence of any s

    for i in range(n):
        for j in range(m, 0, -1):
            if s[i] == t[j - 1]:
                dp[j] += dp[j - 1]

    return dp[m]


# Beats 79.07 %.
def solution_padding_and_space_optimised(s: str, t: str) -> int:
    _s, _t = len(s), len(t)

    if _s < _t:
        return 0

    prev = [0] * (_s + 1)
    curr = [0] * (_s + 1)

    # Base case: filling first row for t[0]
    for j in range(1, _s + 1):
        prev[j] = prev[j - 1]
        if t[0] == s[j - 1]:
            prev[j] += 1

    # Fill the rest
    for i in range(1, _t):
        curr[0] = 0
        for j in range(1, _s + 1):
            curr[j] = curr[j - 1]
            if t[i] == s[j - 1]:
                curr[j] += prev[j - 1]
        prev, curr = curr, prev

    return prev[_s]


# Beats 35.20 %.
def solution_bottom_up_padding(s: str, t: str) -> int:
    _s, _t = len(s), len(t)

    if _s < _t:
        return 0

    dp = [[0 for _ in range(_s + 1)] for _ in range(_t + 1)]

    for j in range(1, _s + 1):
        dp[1][j] = dp[1][j - 1]
        if t[0] == s[j - 1]:
            dp[1][j] += 1

    for i in range(2, _t + 1):
        for j in range(1, _s + 1):
            dp[i][j] = dp[i][j - 1]
            if t[i - 1] == s[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]

    return dp[-1][-1]


def solution_top_down(s: str, t: str) -> int:
    _s, _t = len(s), len(t)

    if _s < _t:
        return 0

    @functools.cache
    def dfs(i, j):
        if _t == j:
            return 1
        if _s == i:
            return 0

        return dfs(i + 1, j) + (dfs(i + 1, j + 1) if s[i] == t[j] else 0)

    return dfs(0, 0)


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
