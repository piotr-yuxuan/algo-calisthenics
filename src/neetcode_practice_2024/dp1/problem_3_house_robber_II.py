#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_first_attempt(nums: List[int]) -> int:
    def tabulation(nums: List[int]):
        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(0, n):
            dp[i] = max(
                dp[i - 1],
                nums[i] + dp[i - 2],
            )

        return dp[n - 1]

    n = len(nums)
    if 0 == n:
        return 0
    elif 1 == n:
        return nums[0]
    elif 2 == n:
        # Litigious.
        return max(nums)
    else:
        return max(
            tabulation(nums[1:]),
            tabulation(nums[:-1]),
        )


def solution_second_attempt(nums: List[int]) -> int:
    def dfs(memo, nums, i):
        if i in memo:
            return memo[i]
        elif len(nums) <= i:
            return 0
        else:
            memo[i] = max(
                dfs(memo, nums, i + 1),
                nums[i] + dfs(memo, nums, i + 2),
            )
            return memo[i]

    n = len(nums)
    if 0 == n:
        return 0
    elif 1 == n:
        return nums[0]
    elif 2 == n:
        # Litigious.
        return max(nums)
    else:
        return max(
            dfs(dict(), nums[1:], 0),
            dfs(dict(), nums[:-1], 0),
        )


def solution_third_attempt(nums: List[int]) -> int:
    def dfs(memo, nums, i):
        if i in memo:
            return memo[i]
        elif len(nums) <= i:
            return 0
        else:
            memo[i] = max(
                dfs(memo, nums, i + 1),
                nums[i] + dfs(memo, nums, i + 2),
            )
            return memo[i]

    n = len(nums)
    if 0 == n:
        return 0
    elif 1 == n:
        return nums[0]
    elif 2 == n:
        # Litigious.
        return max(nums)
    else:
        return max(
            dfs(dict(), nums[1:], 0),
            dfs(dict(), nums[:-1], 0),
        )


def solution_fourth_attempt(nums: List[int]) -> int:
    n = len(nums)
    if 0 == n:
        return 0
    elif 1 == n:
        return nums[0]
    elif 2 == n:
        return max(nums)

    @functools.lru_cache(maxsize=n)
    def dfs(start, end, i):
        if i < start:
            return 0
        elif end <= i:
            return 0
        else:
            return max(
                dfs(start, end, i + 1),
                nums[i] + dfs(start, end, i + 2),
            )

    return max(
        dfs(1, n, 1),
        dfs(0, n - 1, 0),
    )


def solution(nums: List[int]) -> int:
    def dfs(nums):
        prev2, prev1 = 0, 0

        for num in nums:
            prev2, prev1 = prev1, max(prev2 + num, prev1)
        return prev1

    return max(
        nums[0],
        dfs(nums[1:]),
        dfs(nums[:-1]),
    )


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
