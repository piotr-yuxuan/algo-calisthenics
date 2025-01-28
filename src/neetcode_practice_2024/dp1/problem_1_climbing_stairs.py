#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_first(n: str):
    def dfs(counter: int):
        """Traverse the decision tree with a depth-first search."""
        if n == counter:
            return 1
        elif n < counter:
            return 0
        else:
            return dfs(counter + 1) + dfs(counter + 2)

    return dfs(0)


def solution_second(n: str):
    @functools.lru_cache(maxsize=n)
    def dfs(counter: int):
        if n <= counter:
            return 1 if n == counter else 0
        else:
            return dfs(counter + 1) + dfs(counter + 2)

    return dfs(0)


def solution_third(n: str):
    dp = dict({})

    def dfs(counter: int):
        if cached := dp.get(counter, None):
            return cached
        elif n == counter:
            return 1
        elif n < counter:
            return 0
        else:
            result = dfs(counter + 1) + dfs(counter + 2)
            dp[counter] = result
            return result

    return dfs(0)


def solution_bottom_up_first(n: str):
    dp = [0 for _ in range(n + 1)]
    if 1 <= n:
        dp[1] = 1
    if 2 <= n:
        dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def solution_bottom_up_second(n: str):
    dp = [0, 1, 2] + [0 for _ in range(3, n + 1)]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def solution(n: int) -> int:
    def dfs(i):
        if i >= n:
            return i == n
        return dfs(i + 1) + dfs(i + 2)

    return dfs(0)


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=", ".join(
            "Neetcode 2024",
            "dynamic programming",
            "problem 1 climbing stairs",
        )
    )
    parser.add_argument(
        "--number",
        "-n",
        type=int,
        required=True,
        help="The input array as a comma-separated list of integers: `1,2,3`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
