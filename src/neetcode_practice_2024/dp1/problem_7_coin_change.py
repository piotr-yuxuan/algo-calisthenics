#!/usr/bin/env python

from math import gcd

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution(input):
    return True
def solution_top_down_fail(nums: List[int], target_sum: int) -> int:
    not_found = -1

    if len(nums) < 1:
        return not_found

    def dfs(path_length: int, path_sum: int):
        if target_sum < path_sum:
            return not_found
        elif target_sum == path_sum:
            return path_length
        else:
            return min(dfs(1 + path_length, path_sum + i) for i in nums)

    return dfs(0, 0)


def solution_top_down_too_many_things(nums: List[int], target_sum: int) -> int:
    not_found = -1
    min_path_length = -1

    if len(nums) < 1:
        return not_found

    def dfs(path_length: int, path_sum: int):
        nonlocal min_path_length

        if target_sum < path_sum:
            return not_found
        elif target_sum == path_sum:
            min_path_length = (
                path_length
                if -1 == min_path_length
                else min(min_path_length, path_length)
            )
            return path_length
        else:
            return min(dfs(1 + path_length, path_sum + i) for i in nums)

    dfs(0, 0)

    return min_path_length


def solution_top_down(nums: List[int], target_sum: int) -> int:
    not_found = -1

    if len(nums) < 1:
        return 0
    elif 0 == target_sum:
        return 0
    elif 0 != target_sum % functools.reduce(gcd, nums):
        return not_found

    # Keep track of these values:
    min_path_length = float("inf")

    def dfs(path_length: int, path_sum: int):
        nonlocal min_path_length

        if target_sum == path_sum:
            min_path_length = min(min_path_length, path_length)
        elif path_sum < target_sum:
            for i in nums:
                dfs(1 + path_length, path_sum + i)

    dfs(0, 0)

    return -1 if min_path_length == float("inf") else min_path_length
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


def solution_from_neet_code(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    q = collections.deque([0])
    seen = [False] * (amount + 1)
    seen[0] = True
    res = 0

    while q:
        res += 1
        for _ in range(len(q)):
            cur = q.popleft()
            for coin in coins:
                nxt = cur + coin
                if nxt == amount:
                    return res
                if nxt > amount or seen[nxt]:
                    continue
                seen[nxt] = True
                q.append(nxt)

    return -1
