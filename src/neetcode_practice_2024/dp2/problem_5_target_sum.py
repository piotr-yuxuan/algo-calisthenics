#!/usr/bin/env python

import argparse
import argcomplete

from typing import List
import functools
import collections


def solution_tabular_pruning(nums: List[int], target: int) -> int:
    diff = sum(nums) - target
    if diff < 0 or 1 == diff % 2:
        return 0

    # previous, current
    p = dict({0: 1})

    for n in nums:
        c = dict({})
        for j, v in p.items():
            c[j + n] = c.get(j + n, 0) + v
            c[j - n] = c.get(j - n, 0) + v
        p = c
    return c.get(target, 0)


def solution_dict_space_optimised(self, nums: List[int], target: int) -> int:
    # previous, current
    p = collections.defaultdict(int)
    p[0] = 1
    c = collections.defaultdict(int)

    for i in range(len(nums)):
        c = collections.defaultdict(int)
        for j in p.keys():
            c[j + nums[i]] += p[j]
            c[j - nums[i]] += p[j]
        p = c
    return c[target]


def solution_standard_bottom_up(self, nums: List[int], target: int) -> int:
    # Number of ways to reach this results from the prior subarray.
    dp = [collections.defaultdict(int) for _ in range(len(nums) + 1)]
    dp[0][nums[0]] = 1
    dp[0][-nums[0]] += 1

    for i in range(1, len(nums)):
        for j in dp[i - 1].keys():
            dp[i][j + nums[i]] += dp[i - 1][j]
            dp[i][j - nums[i]] += dp[i - 1][j]
    return dp[len(nums) - 1][target]


def solution(nums: List[int], target: int) -> int:
    @functools.cache
    def dfs(i, current):

        if len(nums) == i:
            if target == current:
                return 1
            else:
                return 0
        if len(nums) < i:
            return 0

        # Instead of using a list as a memoisation key, let's splice it in the space exploration strategy.
        return dfs(i + 1, current + nums[i]) + dfs(i + 1, current - nums[i])

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
