#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_first_attempt(nums: List[int]) -> int:
    def tabulation(nums: List[int]):
        n = len(nums)
        if 0 == n:
            return 0
        elif 1 == n:
            return nums[0]
        elif 2 == n:
            max(nums)

        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(0, n):
            dp[i] = max(
                dp[i - 1],
                nums[i] + dp[i - 2],
            )

        return dp[n - 1]

    return max(
        tabulation(nums[1:]),
        tabulation(nums[:-1]),
    )


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


def solution_from_neet_code(nums: List[int]) -> int:
    """This serves for testing solutions above."""

    def helper(nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
