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
