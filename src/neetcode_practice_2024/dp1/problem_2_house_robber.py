#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools

counter = 0


def solution_first_attempt(nums: List[int]) -> int:
    n = len(nums)

    def dfs(i):
        if n <= i:
            return 0
        else:
            return nums[i] + max(
                dfs(i + 2),
                dfs(i + 3),
            )

    return max(dfs(0), dfs(1))


def solution_second_attempt(nums: List[int]) -> int:
    n = len(nums)
    global counter
    counter = 0

    @functools.lru_cache(maxsize=n)
    def dfs(i):
        global counter
        counter += 1
        if n <= i:
            return 0
        else:
            return nums[i] + max(
                dfs(i + 2),
                dfs(i + 3),
            )

    return max(dfs(0), dfs(1))


def solution_third_attempt(nums: List[int]) -> int:
    n = len(nums)

    @functools.lru_cache(maxsize=n)
    def dfs(i):
        global counter
        counter += 1
        if n <= i:
            return 0
        else:
            return max(
                dfs(i + 1),
                nums[i] + dfs(i + 2),
            )

    return dfs(0)



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
